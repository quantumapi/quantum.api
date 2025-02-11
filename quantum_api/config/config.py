import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Config:
    API_KEY = os.getenv('API_KEY')
    LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')
    DATABASE_URL = os.getenv('DATABASE_URL')

config = Config()
