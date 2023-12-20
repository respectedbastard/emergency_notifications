import os
from dotenv import load_dotenv

load_dotenv()


JWT_SECRET = os.environ.get('JWT_SECRET')
JWT_ALGORITM = os.environ.get('JWT_ALGORITM')

DB_USER = os.environ.get('DB_USER')
DB_PASSWORD = os.environ.get('DB_PASSWORD')
DB_HOST = os.environ.get('DB_HOST')
DB_PORT = os.environ.get('DB_PORT')
DB_NAME = os.environ.get('DB_NAME')

SALT = os.environ.get('SALT')

