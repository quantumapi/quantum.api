from cryptography.fernet import Fernet
from quantum_api.utils.utils import setup_logging
import logging

logger = setup_logging()

# Generate a key for encryption and decryption
key = Fernet.generate_key()
cipher_suite = Fernet(key)

def encrypt_data(data: str) -> str:
    """
    Encrypt the given data using Fernet symmetric encryption.
    """
    try:
        encrypted_data = cipher_suite.encrypt(data.encode())
        return encrypted_data.decode()
    except Exception as e:
        logger.error(f"Error encrypting data: {e}")
        raise RuntimeError("Error encrypting data: " + str(e))

def decrypt_data(encrypted_data: str) -> str:
    """
    Decrypt the given encrypted data using Fernet symmetric encryption.
    """
    try:
        decrypted_data = cipher_suite.decrypt(encrypted_data.encode())
        return decrypted_data.decode()
    except Exception as e:
        logger.error(f"Error decrypting data: {e}")
        raise RuntimeError("Error decrypting data: " + str(e))
