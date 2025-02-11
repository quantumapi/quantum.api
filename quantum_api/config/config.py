# config.py
from pydantic_settings import BaseSettings, Field

class Settings(BaseSettings):
    quantum_api_key: str = Field(..., env="QUANTUM_API_KEY")
    quantum_backend: str = Field("qiskit", env="QUANTUM_BACKEND")
    log_level: str = Field("INFO", env="LOG_LEVEL")
    uvicorn_workers: int = Field(2, env="UVICORN_WORKERS")

    class Config:
        env_file = ".env"

settings = Settings()
