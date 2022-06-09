import os

import cryptocompare
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')

admin_id = 1026151741


def get_crypto_now(name: str, currency: str):
    return cryptocompare.get_price(name, currency=currency)[name][currency]
