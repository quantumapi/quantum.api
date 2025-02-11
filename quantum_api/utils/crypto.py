# crypto.py
import os
from cryptography.fernet import Fernet
import logging

logger = logging.getLogger(__name__)

class QuantumEncryption:
    def __init__(self):
        # Retrieve encryption key from environment or generate a new one.
        # NOTE: In production, manage keys via a secure vault (e.g., HashiCorp Vault, AWS KMS)
        key = os.getenv("ENCRYPTION_KEY")
        if not key:
            key = Fernet.generate_key()
            logger.warning("No ENCRYPTION_KEY found in environment; generated temporary key.")
        self.fernet = Fernet(key)

    def encrypt(self, data):
        """
        Encrypts the provided data (converted to a string) using symmetric encryption.
        For production, consider implementing quantum–resistant algorithms.
        """
        try:
            # Convert data (which could be a list or complex structure) to string
            data_str = str(data)
            encrypted = self.fernet.encrypt(data_str.encode())
            logger.debug("Data encrypted successfully.")
            return encrypted.decode()
        except Exception as e:
            logger.error("Encryption failed: %s", e)
            raise

    def decrypt(self, token):
        """
        Decrypts the provided token back into the original data string.
        """
        try:
            decrypted = self.fernet.decrypt(token.encode())
            logger.debug("Data decrypted successfully.")
            return decrypted.decode()
        except Exception as e:
            logger.error("Decryption failed: %s", e)
            raise
