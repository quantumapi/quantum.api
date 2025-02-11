from cryptography.fernet import Fernet
import hashlib

def generate_quantum_key():
    return Fernet.generate_key()

def get_aes_cipher(key):
    return Fernet(key)

def post_quantum_encrypt(data, key):
    cipher = get_aes_cipher(key)
    encrypted_data = cipher.encrypt(data.encode())
    return encrypted_data

def secure_transmit_message(message, destination):
    key = generate_quantum_key()
    encrypted_message = post_quantum_encrypt(message, key)
    message_hash = hashlib.sha256(encrypted_message).hexdigest()
    blockchain_log = {
        'message_hash': message_hash,
        'destination': destination,
        'timestamp': datetime.now().isoformat()
    }
    # Simulate blockchain logging
    print(f"Blockchain log: {blockchain_log}")
    return encrypted_message
