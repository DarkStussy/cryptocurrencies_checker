from aiogram import types
from aiogram.utils.markdown import italic
from sqlalchemy import select

from db.models import User
from loader import dp
from data.config import get_crypto_now


@dp.message_handler(commands=['check'])
async def check_currencies(message: types.Message):
    btc_now = get_crypto_now("BTC", "USD")
    eth_now = get_crypto_now("ETH", "USD")
    msg = ""
    db_session = dp.bot.get("db")
    async with db_session() as session:
        user = await session.get(User, message.chat.id)

    if user.btc_value:
        msg += f"BTC:\nLast request: {user.btc_value}$\nCurrent BTC: {btc_now}$\nDifference since last request:" \
               f" {round(btc_now - user.btc_value, 2)}$, {round(100.0 - (user.btc_value * 100 / btc_now), 2)}%\n\n"
    if user.eth_value:
        msg += f"ETH:\nLast request: {user.eth_value} $\nCurrent ETH: {eth_now}$\nDifference since last request:\n" \
                   f" {round(eth_now - user.eth_value, 2)}$, {round(100.0 - (user.eth_value * 100 / eth_now), 2)}%\n\n"

    await message.answer(text=msg)
