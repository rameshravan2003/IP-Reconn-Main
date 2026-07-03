import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'a-hard-to-guess-string'
    ABUSEIPDB_API_KEY = os.environ.get('ABUSEIPDB_API_KEY')