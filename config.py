import os
from dotenv import load_dotenv

load_dotenv()

MAIL_LOGIN_USER = os.getenv("MAIL_LOGIN_USER")
PASSWORD_LOGIN_USER = os.getenv("PASSWORD_LOGIN_USER")
