# encryption.py
import os
import base64
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

# Secure key derivation: ensure these environment variables are set securely in production.
PASSPHRASE = os.environ.get("ENCRYPTION_PASSPHRASE", "default_supersecret_passphrase").encode()
SALT = os.environ.get("ENCRYPTION_SALT", "default_salt").encode()

# Derive a 256-bit key using PBKDF2HMAC
kdf = PBKDF2HMAC(
    algorithm=hashes.SHA256(),
    length=32,
    salt=SALT,
    iterations=100000,
)
_KEY = kdf.derive(PASSPHRASE)

def encrypt_data(plaintext: str) -> str:
    """
    Encrypts plaintext using AES-GCM and returns a Base64 encoded string.
    """
    iv = os.urandom(12)  # 96-bit nonce for GCM
    cipher = Cipher(algorithms.AES(_KEY), modes.GCM(iv))
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(plaintext.encode()) + encryptor.finalize()
    encrypted_blob = iv + encryptor.tag + ciphertext
    return base64.b64encode(encrypted_blob).decode()

def decrypt_data(encoded_ciphertext: str) -> str:
    """
    Decrypts the Base64 encoded ciphertext using AES-GCM.
    """
    data = base64.b64decode(encoded_ciphertext)
    iv = data[:12]
    tag = data[12:28]
    ciphertext = data[28:]
    cipher = Cipher(algorithms.AES(_KEY), modes.GCM(iv, tag))
    decryptor = cipher.decryptor()
    plaintext = decryptor.update(ciphertext) + decryptor.finalize()
    return plaintext.decode()
