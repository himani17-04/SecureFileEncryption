
import os
import streamlit as st
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.hazmat.primitives.kdf.scrypt import Scrypt
from cryptography.exceptions import InvalidTag

# Application settings
st.set_page_config(
    page_title="Secure File Encryption",
    page_icon="🔐",
    layout="centered"
)

# File format constants
MAGIC = b"SFE1"
SALT_SIZE = 16
NONCE_SIZE = 12
KEY_SIZE = 32
SCRYPT_N = 2**14
SCRYPT_R = 8
SCRYPT_P = 1


def derive_key(password, salt):
    """Derive a 256-bit encryption key from the password."""
    kdf = Scrypt(
        salt=salt,
        length=KEY_SIZE,
        n=SCRYPT_N,
        r=SCRYPT_R,
        p=SCRYPT_P
    )
    return kdf.derive(password.encode("utf-8"))


def encrypt_file(file_data, password):
    """Encrypt file bytes using AES-256-GCM."""
    salt = os.urandom(SALT_SIZE)
    nonce = os.urandom(NONCE_SIZE)

    key = derive_key(password, salt)
    aesgcm = AESGCM(key)

    encrypted_data = aesgcm.encrypt(
        nonce,
        file_data,
        MAGIC
    )

    # Format: header + salt + nonce + encrypted data and tag
    return MAGIC + salt + nonce + encrypted_data


def decrypt_file(encrypted_data, password):
    """Decrypt a file created by this application."""
    header_size = len(MAGIC) + SALT_SIZE + NONCE_SIZE

    if len(encrypted_data) < header_size + 16:
        raise ValueError("The encrypted file is too small or incomplete.")

    if not encrypted_data.startswith(MAGIC):
        raise ValueError(
            "Invalid file format. Select a file encrypted by this application."
        )

    salt_start = len(MAGIC)
    nonce_start = salt_start + SALT_SIZE
    data_start = nonce_start + NONCE_SIZE

    salt = encrypted_data[salt_start:nonce_start]
    nonce = encrypted_data[nonce_start:data_start]
    ciphertext = encrypted_data[data_start:]

    key = derive_key(password, salt)
    aesgcm = AESGCM(key)

    # AES-GCM verifies the password and detects tampering
    return aesgcm.decrypt(nonce, ciphertext, MAGIC)


# Application interface
st.title("🔐 Secure File Encryption System")
st.write(
    "Protect your files with password-based AES-256-GCM encryption."
)

st.info(
    "Your files are processed by this application. "
    "Keep your password safe: it cannot be recovered if forgotten."
)

encrypt_tab, decrypt_tab = st.tabs(["Encrypt File", "Decrypt File"])

with encrypt_tab:
    st.subheader("Encrypt a file")

    file_to_encrypt = st.file_uploader(
        "Choose a file to encrypt",
        key="encrypt_upload"
    )

    encrypt_password = st.text_input(
        "Create an encryption password",
        type="password",
        key="encrypt_password"
    )

    confirm_password = st.text_input(
        "Confirm encryption password",
        type="password",
        key="confirm_password"
    )

    if st.button("Encrypt File", type="primary"):
        if file_to_encrypt is None:
            st.error("Please choose a file first.")
        elif len(encrypt_password) < 12:
            st.error("Use a password with at least 12 characters.")
        elif encrypt_password != confirm_password:
            st.error("The passwords do not match.")
        else:
            try:
                original_data = file_to_encrypt.getvalue()
                encrypted_data = encrypt_file(
                    original_data,
                    encrypt_password
                )

                original_name = os.path.basename(file_to_encrypt.name)
                encrypted_name = original_name + ".sfe"

                st.session_state["encrypted_data"] = encrypted_data
                st.session_state["encrypted_name"] = encrypted_name

                st.success("File encrypted successfully.")

            except Exception:
                st.error("Encryption failed. Please try a smaller file.")

    if "encrypted_data" in st.session_state:
        st.download_button(
            "Download Encrypted File",
            data=st.session_state["encrypted_data"],
            file_name=st.session_state["encrypted_name"],
            mime="application/octet-stream",
            key="download_encrypted"
        )

with decrypt_tab:
    st.subheader("Decrypt a file")

    file_to_decrypt = st.file_uploader(
        "Choose an .sfe encrypted file",
        key="decrypt_upload"
    )

    decrypt_password = st.text_input(
        "Enter the encryption password",
        type="password",
        key="decrypt_password"
    )

    if st.button("Decrypt File", type="primary"):
        if file_to_decrypt is None:
            st.error("Please select an encrypted file.")
        elif not decrypt_password:
            st.error("Please enter the password.")
        else:
            try:
                encrypted_data = file_to_decrypt.getvalue()
                decrypted_data = decrypt_file(
                    encrypted_data,
                    decrypt_password
                )

                encrypted_name = os.path.basename(
                    file_to_decrypt.name
                )
                original_name = (
                    encrypted_name[:-4]
                    if encrypted_name.lower().endswith(".sfe")
                    else "decrypted_file"
                )

                st.session_state["decrypted_data"] = decrypted_data
                st.session_state["decrypted_name"] = original_name

                st.success("File decrypted successfully.")

            except (InvalidTag, ValueError):
                st.error(
                    "Decryption failed. The password may be incorrect, "
                    "or the file may be damaged or unsupported."
                )
            except Exception:
                st.error("An unexpected error occurred during decryption.")

    if "decrypted_data" in st.session_state:
        st.download_button(
            "Download Decrypted File",
            data=st.session_state["decrypted_data"],
            file_name=st.session_state["decrypted_name"],
            mime="application/octet-stream",
            key="download_decrypted"
        )

st.divider()
st.caption("Cryptography & Network Security Mini Project")
st.caption("Algorithm: AES-256-GCM | Key derivation: Scrypt")
