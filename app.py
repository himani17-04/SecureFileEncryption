
import streamlit as st

# Configure the application page
st.set_page_config(
    page_title="Secure File Encryption",
    page_icon="🔐",
    layout="centered"
)

# Display the application title
st.title("Secure File Encryption System")

# Display a short introduction
st.write(
    "Welcome! This application will help you "
    "encrypt and decrypt files securely."
)

# Display project information
st.subheader("Project Information")

st.info(
    "Cryptography & Network Security Mini Project"
)

st.write("Programming Language: Python")
st.write("Interface: Streamlit")
st.write("Encryption Algorithm: AES")

# Create a simple file uploader
uploaded_file = st.file_uploader(
    "Choose a file to test file upload",
    type=None
)

# Display the selected file name
if uploaded_file is not None:
    st.success(
        f"File selected successfully: {uploaded_file.name}"
    )

    st.write(
        f"File size: {uploaded_file.size} bytes"
    )
