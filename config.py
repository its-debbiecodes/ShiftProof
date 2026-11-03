
import os
from dotenv import load_dotenv
load_dotenv()

class Config:
    APP_NAME = os.getenv("APP_NAME", "ShiftProof")
    APP_ENVIRONMENT = os.getenv("APP_ENV", "development")
    DEBUG= os.getenv("DEBUG", "False").lower() == "true"
    SECRET_KEY = os.getenv("SECRET_KEY")
    DATABASE_URI = os.getenv("DATABASE_URI", "sqlite:///shiftproof.db")