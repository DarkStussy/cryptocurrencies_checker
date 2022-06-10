import os

import aiohttp
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')

admin_id = 1026151741


async def get_crypto_now(name: str, currency: str):
    async with aiohttp.ClientSession() as session:
        currency_url = f"https://api.coingecko.com/api/v3/coins/{name}"
        async with session.get(currency_url) as resp:
            pokemon = await resp.json()
            return pokemon['market_data']['current_price'][currency]
