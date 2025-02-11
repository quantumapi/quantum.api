# security.py
from fastapi import Request, HTTPException
from starlette.middleware.base import BaseHTTPMiddleware
import os
from cryptography.fernet import Fernet
import bandit

class RateLimitMiddleware(BaseHTTPMiddleware):
    def __init__(self, app, max_requests: int, window_seconds: int):
        super().__init__(app)
        self.max_requests = max_requests
        self.window_seconds = window_seconds
        self.clients = {}

    async def dispatch(self, request: Request, call_next):
        client_ip = request.client.host
        if client_ip not in self.clients:
            self.clients[client_ip] = []
        request_times = self.clients[client_ip]
        current_time = request.scope["time"]
        request_times = [t for t in request_times if current_time - t < self.window_seconds]
        if len(request_times) >= self.max_requests:
            raise HTTPException(status_code=429, detail="Too many requests")
        request_times.append(current_time)
        self.clients[client_ip] = request_times
        response = await call_next(request)
        return response

SECRET_KEY = os.getenv("SECRET_KEY", "default_secret_key")

# Generate a key for encryption
encryption_key = Fernet.generate_key()
cipher_suite = Fernet(encryption_key)

# Example encryption function
def encrypt_data(data: str) -> str:
    return cipher_suite.encrypt(data.encode()).decode()

# Example decryption function
def decrypt_data(encrypted_data: str) -> str:
    return cipher_suite.decrypt(encrypted_data.encode()).decode()

# Perform security audit using Bandit
def perform_security_audit():
    bandit.main(["-r", "."])
