from cryptography.fernet import Fernet


def generate_key():
    key = Fernet.generate_key()
    with open('key.key', 'wb') as key_file:
        key_file.write(key)


def load_key():
    with open('key.key', 'rb') as key_file:
        key = key_file.read()
    return key


def encrypt_message(message, key):
    f = Fernet(key)
    encrypted_message = f.encrypt(message.encode())
    return encrypted_message


def decrypt_message(encrypted_message, key):
    f = Fernet(key)
    decrypted_message = f.decrypt(encrypted_message).decode()
    return decrypted_message


if __name__ == '__main__':
    # Generate and load encryption key
    generate_key()
    key = load_key()

    # Encrypt and decrypt a message
    message = "Bhuvana"
    encrypted_message = encrypt_message(message, key)
    decrypted_message = decrypt_message(encrypted_message, key)

    print("Original Message:", message)
    print("Encrypted Message:", encrypted_message)
    print("Decrypted Message:", decrypted_message)