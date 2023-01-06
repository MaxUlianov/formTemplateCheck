import os
from dotenv import load_dotenv

load_dotenv()
secret = os.environ.get('SECRET')

if secret is None:
    secret = '8cefa206a3c043499fd82515a95e83a6'
