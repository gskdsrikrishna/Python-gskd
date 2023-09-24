#96.Encrypt and Decrypt a string
def encrypt_string(string, key):
    encrypted_string = ""
    for char in string:
        encrypted_char = chr(ord(char) + key)
        encrypted_string += encrypted_char
    return encrypted_string

def decrypt_string(string, key):
    decrypted_string = ""
    for char in string:
        decrypted_char = chr(ord(char) - key)
        decrypted_string += decrypted_char
    return decrypted_string

string = input("Enter a string: ")
key = int(input("Enter the encryption/decryption key: "))

encrypted_string = encrypt_string(string, key)
print("Encrypted string:", encrypted_string)

decrypted_string = decrypt_string(encrypted_string, key)
print("Decrypted string:", decrypted_string)