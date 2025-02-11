# quantum_api/security/security.py
import os
from cryptography.fernet import Fernet
from quantum_api.utils.utils import setup_logging

logger = setup_logging()

# Load key from environment variable; fallback only for development
KEY = os.getenv("FERNET_KEY")
if not KEY:
    logger.warning("FERNET_KEY not set; generating a temporary key.")
    KEY = Fernet.generate_key()
cipher_suite = Fernet(KEY)

def encrypt_data(data: str) -> str:
    """
    Encrypt data using Fernet symmetric encryption.
    """
    try:
        encrypted_data = cipher_suite.encrypt(data.encode())
        return encrypted_data.decode()
    except Exception as e:
        logger.error(f"Error encrypting data: {e}")
        raise RuntimeError("Error encrypting data: " + str(e))

def decrypt_data(encrypted_data: str) -> str:
    """
    Decrypt data using Fernet symmetric encryption.
    """
    try:
        decrypted_data = cipher_suite.decrypt(encrypted_data.encode())
        return decrypted_data.decode()
    except Exception as e:
        logger.error(f"Error decrypting data: {e}")
        raise RuntimeError("Error decrypting data: " + str(e))
