# config.py
from pydantic_settings import BaseSettings, Field
import logging
import os

class Settings(BaseSettings):
    quantum_api_key: str = Field(..., env="QUANTUM_API_KEY")
    quantum_backend: str = Field("qiskit", env="QUANTUM_BACKEND")
    log_level: str = Field("INFO", env="LOG_LEVEL")
    uvicorn_workers: int = Field(2, env="UVICORN_WORKERS")
    secret_key: str = Field(..., env="SECRET_KEY")

    class Config:
        env_file = ".env"

try:
    settings = Settings()
except Exception as e:
    logging.error(f"Configuration error: {e}")
    raise RuntimeError("Configuration error: " + str(e))

# Configure logging
logging.basicConfig(level=settings.log_level)
logging.info("Configuration loaded successfully")

# Additional configuration for production
if os.getenv("PRODUCTION") == "true":
    logging.info("Running in production mode")
    # Additional production-specific configurations can be added here
