import zipfile
import os
from cryptography.fernet import Fernet

def encrypt_zip_file(zip_file_path, encryption_key):
    # Generate encryption key
    key = Fernet.generate_key()
    f = Fernet(key)

    # Create a temporary directory to store the encrypted files
    temp_directory = 'D:/Py/RAR/'
    os.makedirs(temp_directory, exist_ok=True)

    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        # Extract files from the original ZIP file to the temporary directory
        zip_ref.extractall(temp_directory)

    # Encrypt the files in the temporary directory
    for root, dirs, files in os.walk(temp_directory):
        for file in files:
            file_path = os.path.join(root, file)
            with open(file_path, 'rb') as f_in:
                data = f_in.read()
                encrypted_data = f.encrypt(data)
            with open(file_path, 'wb') as f_out:
                f_out.write(encrypted_data)

    # Create a new encrypted ZIP file
    encrypted_zip_file_path = 'D:/Py/RAR/gskdzip1.zip'
    with zipfile.ZipFile(encrypted_zip_file_path, 'w') as zip_ref:
        for root, dirs, files in os.walk(temp_directory):
            for file in files:
                file_path = os.path.join(root, file)
                zip_ref.write(file_path, os.path.relpath(file_path, temp_directory))

    # Remove the temporary directory
    for root, dirs, files in os.walk(temp_directory, topdown=False):
        for file in files:
            file_path = os.path.join(root, file)
            os.remove(file_path)
        os.rmdir(root)
    os.removedirs(temp_directory)

    # Save the encryption key to a file
    key_file_path = 'D:/Py/RAR/gskd.key'
    with open(key_file_path, 'wb') as key_file:
        key_file.write(key)

    return encrypted_zip_file_path, key_file_path

# Usage example:
zip_file_path = 'D:/Py/RAR/gskd.zip'
encryption_key = b'your_encryption_key'
encrypted_zip_file_path, key_file_path = encrypt_zip_file(zip_file_path, encryption_key)
print(f"Encrypted ZIP file: {encrypted_zip_file_path}")
print(f"Encryption key file: {key_file_path}")
