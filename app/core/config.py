import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    MONGODB_URI = os.getenv("MONGODB_URI", "mongodb://localhost:27017")
    DB_NAME = os.getenv("DB_NAME", "focus_forge")

settings = Settings()
