import os
from dotenv import load_dotenv

load_dotenv()

BASE_URL = "https://www.lamoda.by"

MAIL_LOGIN_USER = os.getenv("MAIL_LOGIN_USER")
PASSWORD_USER = os.getenv("PASSWORD_USER")

WRONG_MAIL_LOGIN_USER = 'my@mail.ru'
WRONG_PASSWORD = 12345