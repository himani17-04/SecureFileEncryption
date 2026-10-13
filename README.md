# Secure File Encryption System

## 1. Project Title

**Secure File Encryption System Using AES-256-GCM**

A Python-based Cryptography and Network Security mini project that provides password-based file encryption and decryption through a simple Streamlit web interface.

## 2. Problem Statement

Digital files often contain sensitive information that may be exposed when stored or shared without proper security. Unauthorized individuals may access confidential documents, images, and other files if appropriate protection is not used.

The Secure File Encryption System addresses this problem by encrypting files using AES-256-GCM and deriving encryption keys from user passwords using Scrypt. It also verifies the integrity and authenticity of encrypted data during decryption, helping detect incorrect passwords and unauthorized modifications.

## 3. Objectives

- To implement secure file encryption using the AES-256-GCM algorithm.
- To derive a 256-bit encryption key from a user-provided password using Scrypt.
- To allow users to decrypt encrypted files using the correct password.
- To detect incorrect passwords and modified or corrupted encrypted files.
- To provide a simple and user-friendly interface using Streamlit.
- To demonstrate important cryptography and network security concepts through a practical application.

## 4. Technologies Used

## 4. Technologies Used

| **Technology** | **Purpose** |
|:---|:---|
| Python | Main programming language used to develop the application. |
| Streamlit | Creates the interactive web interface for file encryption and decryption. |
| Cryptography Library | Provides cryptographic functions for secure file processing. |
| AES-256-GCM | Encrypts files and verifies data authenticity and integrity. |
| Scrypt | Derives a 256-bit encryption key from the user's password. |
| Git | Tracks changes and manages versions of the source code. |
| GitHub | Hosts the source code and project documentation online. |
| Visual Studio Code | Used to write, edit, and manage the project code. |

## 5. Python Libraries Used

### 5.1 Streamlit

Streamlit is used to create the web interface, accept file uploads, collect passwords, display messages, and provide download buttons.

### 5.2 Cryptography

The `cryptography` library provides the AES-GCM encryption functionality, Scrypt key derivation, and authentication error handling.

### 5.3 OS

Python's built-in `os` module is used to generate cryptographically secure random bytes for salts and nonces and to handle file names.

### 5.4 Required Dependencies

The project uses the following Python packages, listed in `requirements.txt`:

```text
streamlit
cryptography
```

The modules `os` and other standard-library functionality do not require separate installation.

## 6. Cryptography/Network Security Concepts Used

### 6.1 Symmetric Encryption

Symmetric encryption uses the same secret key for encryption and decryption. In this project, the encryption key is derived from a password and used for both operations.

### 6.2 AES-256-GCM

Advanced Encryption Standard (AES) with a 256-bit key is used in Galois/Counter Mode (GCM). AES-GCM provides confidentiality and authenticated encryption, allowing the application to detect unauthorized changes to encrypted data.

### 6.3 Password-Based Key Derivation

Scrypt converts the user's password into a 256-bit encryption key. It is designed to make password guessing more computationally and memory intensive.

### 6.4 Random Salt

A random 16-byte salt is generated for every encryption operation. The salt is used during key derivation so that the same password can produce different encryption keys for different files.

### 6.5 Random Nonce

A random 12-byte nonce is generated for each encryption operation. AES-GCM requires nonce uniqueness for a given key; this implementation generates a fresh random salt and nonce for each file encryption.

### 6.6 Data Integrity and Authentication

AES-GCM generates an authentication tag with the encrypted data. During decryption, the tag is verified. If the password is incorrect or the encrypted data has been modified, authentication fails and the application rejects the decryption.

### 6.7 Confidentiality

The original file contents are converted into ciphertext, making them unreadable without the correct encryption key.

## 7. Key Features

- **File Upload:** Users can select files for encryption or decryption.
- **Password-Based Encryption:** Users create a password of at least 12 characters and confirm it before encryption.
- **Secure File Encryption:** Files are encrypted using AES-256-GCM.
- **Encrypted File Download:** Encrypted files are provided with the `.sfe` extension.
- **File Decryption:** Users can restore the original contents using the correct password.
- **Incorrect Password Detection:** Failed authentication prevents decryption with an incorrect password.
- **Tampering Detection:** Modified or corrupted encrypted data is rejected when authentication fails.
- **Input Validation:** The application checks for missing files, empty passwords, and mismatched confirmation passwords.
- **Simple User Interface:** Separate tabs make encryption and decryption easy to use.
- **Download Support:** Users can download the resulting encrypted and decrypted files.

## 8. System Requirements

### Hardware Requirements

- Computer or laptop.
- Sufficient memory and storage for Python, project dependencies, and the files being processed.
- Internet connection for installing the dependencies.

### Software Requirements

- Operating system: Windows, Linux, or macOS.
- Python 3.13 or a compatible Python version supported by the installed dependencies.
- Visual Studio Code or another Python-compatible editor.
- pip, the Python package installer.
- A modern web browser.
- Git (optional for local execution, required for the documented Git workflow).

## 9. How to Install and Run

### Step 1: Install Python

Install a compatible Python version from:

https://www.python.org/downloads/

Verify the installation:

```bash
python --version
```

### Step 2: Clone the GitHub Repository

Open a terminal and execute:

```bash
git clone https://github.com/himani17-04/SecureFileEncryption.git
```

### Step 3: Open the Project Directory

```bash
cd SecureFileEncryption
```

### Step 4: Create a Virtual Environment

```bash
python -m venv venv
```

### Step 5: Activate the Virtual Environment

**Windows PowerShell:**

```powershell
.\venv\Scripts\Activate.ps1
```

**Windows Command Prompt:**

```cmd
venv\Scripts\activate.bat
```

**Linux/macOS:**

```bash
source venv/bin/activate
```

### Step 6: Install Dependencies

```bash
python -m pip install -r requirements.txt
```

### Step 7: Run the Application

```bash
streamlit run app.py
```

### Step 8: Open the Application

Open the local URL displayed in the terminal, usually:

http://localhost:8501

### How to Encrypt a File

1. Open the **Encrypt File** tab.
2. Select the file you want to encrypt.
3. Enter a password containing at least 12 characters.
4. Enter the same password in the confirmation field.
5. Click **Encrypt File**.
6. Download the generated `.sfe` file.

### How to Decrypt a File

1. Open the **Decrypt File** tab.
2. Select the `.sfe` file generated by the application.
3. Enter the original encryption password.
4. Click **Decrypt File**.
5. If decryption succeeds, download the restored file.

**Important:** Keep the encryption password safe. The application does not provide password recovery. Losing the password may make the encrypted file unrecoverable.

## 10. Screenshots

Add screenshots of your running application to a folder named `screenshots` in the project directory.

Recommended folder structure:

```text
SecureFileEncryption/
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
└── screenshots/
    ├── home.png
    ├── encryption_success.png
    ├── decryption_success.png
    └── incorrect_password.png
```

Insert the actual screenshots into this section using the following Markdown:

### 10.1 Application Home Page

![Secure File Encryption System Home Page](screenshots/home.png)

### 10.2 Successful File Encryption

![Successful File Encryption](screenshots/encryption_success.png)

### 10.3 Successful File Decryption

![Successful File Decryption](screenshots/decryption_success.png)

### 10.4 Incorrect Password Error

![Incorrect Password Error](screenshots/incorrect_password.png)

**Note:** Replace these image references with your actual screenshot files using the specified names. The images will appear on GitHub after you add and push the screenshot files.

## 11. Project Demonstration

The project demonstrates how cryptographic techniques can protect files from unauthorized access.

### Demonstration Workflow

1. The user selects a file and enters a password.
2. The application generates a random salt and nonce.
3. Scrypt derives a 256-bit key from the password and salt.
4. AES-256-GCM encrypts the file contents and generates authentication information.
5. The application combines a file-format header, salt, nonce, and encrypted data into an `.sfe` file.
6. The user downloads the encrypted file.
7. For decryption, the application extracts the salt, nonce, and ciphertext from the encrypted file.
8. Scrypt derives the key again using the entered password and stored salt.
9. AES-GCM verifies the authentication tag and decrypts the file only if authentication succeeds.
10. The application provides the decrypted file for download when decryption is successful.

### Testing

| Test Case | Expected Result |
|---|---|
| Encrypt a valid file | Encrypted `.sfe` file is generated. |
| Decrypt using the correct password | Original file contents are restored. |
| Decrypt using an incorrect password | Decryption fails with an error message. |
| Select an ordinary unencrypted file | The file is rejected as an invalid format. |
| Modify or corrupt the encrypted data | Decryption fails if authentication verification fails. |

### Demonstration Video

If a demonstration video is recorded, upload it to a suitable platform and insert its link here.

**Video Link:** Add your demonstration video URL here.

## 12. GitHub Repository Link

The complete project source code and documentation are available at:

**Repository:** https://github.com/himani17-04/SecureFileEncryption

The repository contains the application code, dependency list, project documentation, and Git configuration files.

## Limitations

- Forgotten passwords cannot be recovered by the application.
- The current prototype processes uploaded files in application memory, so very large files may require substantial memory.
- Random nonces have a small theoretical probability of collision; this implementation is intended for an educational demonstration.
- The application does not include user accounts, cloud storage, or password recovery.
- The project is an educational prototype and has not undergone a formal security audit.

## Conclusion

The Secure File Encryption System demonstrates the practical use of AES-256-GCM and Scrypt to encrypt and decrypt files through a simple Streamlit interface. It illustrates confidentiality, password-based key derivation, random salts and nonces, and authentication-based integrity verification. The project provides a foundation for understanding how cryptographic techniques can be applied to file protection.
