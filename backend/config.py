import os

from dotenv import load_dotenv


load_dotenv()



APIFOOTBALL_KEY = os.getenv(
    "APIFOOTBALL_KEY"
)


TELEGRAM_TOKEN = os.getenv(
    "TELEGRAM_TOKEN"
)


TELEGRAM_CHAT_ID = os.getenv(
    "TELEGRAM_CHAT_ID"
)