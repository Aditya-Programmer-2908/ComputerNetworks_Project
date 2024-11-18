from cryptography.fernet import Fernet

def generate_key():
    return Fernet.generate_key()

def encrypt_data(data, key):
    cipher = Fernet(key)
    return cipher.encrypt(data)

from cryptography.fernet import Fernet
import base64

def decrypt_data(encrypted_content, key):
    try:
        key = base64.urlsafe_b64decode(key)
        cipher = Fernet(key)
        decrypted_content = cipher.decrypt(encrypted_content.encode())  # Ensure the encrypted content is in bytes
        return decrypted_content.decode()
    except Exception as e:
        print(f"Error during decryption: {e}")
        raise

