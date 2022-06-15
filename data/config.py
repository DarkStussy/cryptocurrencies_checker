import os

import aiohttp
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')

admin_id = 1026151741


async def get_crypto_now(name: str, currency: str):
    async with aiohttp.ClientSession() as session:
        currency_url = f"https://api.binance.com/api/v3/ticker/price?symbol={name}{currency}"
        async with session.get(currency_url) as resp:
            currency_price = await resp.json()
            return currency_price['price']
