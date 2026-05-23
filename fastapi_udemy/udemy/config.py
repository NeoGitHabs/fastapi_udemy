from dotenv import load_dotenv
import os


load_dotenv()
SECRET_KEY = os.getenv('SECRET_KEY')
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30
REFRESH_TOKEN_EXPIRE_DAYS = 3

class Settings:
    GITHUB_CLIENT_ID = os.getenv('GITHUB_CLIENT_ID')
    GITHUB_KEY = os.getenv('GITHUB_KEY')
    GITHUB_URL = os.getenv('GITHUB_URL')

    GOOGLE_CLIENT_ID = os.getenv('GOOGLE_CLIENT_ID')
    GOOGLE_KEY = os.getenv('GOOGLE_KEY')
    GOOGLE_URL = os.getenv('GOOGLE_URL')

settings = Settings()
