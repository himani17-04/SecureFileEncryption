
# Secure File Encryption System

## 1. Introduction
A Python-based Cryptography and Network Security mini project that protects files using password-based encryption.

## 2. Problem Statement
Files containing sensitive information can be exposed when stored or shared without encryption. This project demonstrates how cryptography can protect file confidentiality and detect unauthorized modifications.

## 3. Objectives
- Encrypt files using AES-256-GCM.
- Derive encryption keys from passwords using Scrypt.
- Decrypt files using the correct password.
- Detect incorrect passwords and modified encrypted data.
- Provide a simple interface using Streamlit.

## 4. Technologies Used
- Python
- Streamlit
- Cryptography library
- AES-256-GCM
- Scrypt key derivation

## 5. Features
- File upload
- Password-based encryption
- Encrypted file download
- File decryption
- Incorrect password and tampering detection

## 6. Project Structure
- app.py: Main application
- requirements.txt: Required Python libraries
- .gitignore: Files excluded from Git

## 7. System Requirements
- Windows, Linux, or macOS
- Python 3.13 or a compatible Python version
- Internet connection for installing dependencies

## 8. Installation and Execution
1. Clone the repository.
2. Open the project directory in a terminal.
3. Create a virtual environment.
4. Install dependencies using:
   pip install -r requirements.txt
5. Run the application using:
   streamlit run app.py

## 9. Security Concepts
- Symmetric encryption
- AES-GCM authenticated encryption
- Password-based key derivation
- Random salts and nonces
- Data integrity verification

## 10. Limitations
- Forgotten passwords cannot be recovered.
- This prototype processes uploaded files in application memory.
- It is intended for educational demonstration, not as a fully audited production security tool.

## 11. GitHub Repository
https://github.com/himani17-04/SecureFileEncryption
