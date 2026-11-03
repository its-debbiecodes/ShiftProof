
import os
from dotenv import load_dotenv
load_dotenv()

class Config:
    APP_NAME = os.getenv("APP_NAME", "ShiftProof")
    APP_ENVIRONMENT = os.getenv("APP_ENV", "development")
    DEBUG= os.getenv("DEBUG", "False").lower() == "true"
    SECRET_KEY = os.getenv("SECRET_KEY")
    DATABASE_URL = os.getenv("DATABASE_URl", "sqlite:///shiftproof.db")