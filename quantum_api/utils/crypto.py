# quantum_api/utils/crypto.py
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import base64
import os

class AESCipher:
    def __init__(self, key: bytes):
        if len(key) not in (16, 24, 32):
            raise ValueError("Key must be 16, 24, or 32 bytes long.")
        self.key = key

    def encrypt(self, raw: str) -> str:
        iv = os.urandom(16)
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        ct_bytes = cipher.encrypt(pad(raw.encode('utf-8'), AES.block_size))
        iv_encoded = base64.b64encode(iv).decode('utf-8')
        ct_encoded = base64.b64encode(ct_bytes).decode('utf-8')
        return f"{iv_encoded}:{ct_encoded}"

    def decrypt(self, enc: str) -> str:
        try:
            iv_encoded, ct_encoded = enc.split(":")
            iv = base64.b64decode(iv_encoded)
            ct = base64.b64decode(ct_encoded)
            cipher = AES.new(self.key, AES.MODE_CBC, iv)
            pt = unpad(cipher.decrypt(ct), AES.block_size)
            return pt.decode('utf-8')
        except (ValueError, KeyError) as e:
            raise ValueError("Decryption failed.") from e
