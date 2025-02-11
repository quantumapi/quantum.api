# quantum_api/config.py
import os

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", "default_super_secret_key")
    # Additional configuration settings (e.g., API keys, quantum backend endpoints) go here.

config = Config()
