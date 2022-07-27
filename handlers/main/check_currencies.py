from aiogram import types

from db.models import User
from loader import dp
from data.config import get_crypto_now


@dp.message_handler(commands=['check'])
async def check_currencies(message: types.Message):
    msg = ""
    db_session = dp.bot.get("db")
    async with db_session() as session:
        user = await session.get(User, message.chat.id)

    if user.btc_value:
        btc_now = await get_crypto_now("BTC", "EUR")
        btc_now = round(float(btc_now), 2)
        msg += f"BTC:\nLast request: {user.btc_value}€\nCurrent BTC: {btc_now}€\nDifference since last request:" \
               f" {round(btc_now - user.btc_value, 2)}€, {round(100.0 - (user.btc_value * 100 / btc_now), 2)}%\n\n"
    if user.eth_value:
        eth_now = await get_crypto_now("ETH", "EUR")
        eth_now = round(float(eth_now), 2)
        msg += f"ETH:\nLast request: {user.eth_value}€\nCurrent ETH: {eth_now}€\nDifference since last request:\n" \
               f" {round(eth_now - user.eth_value, 2)}€, {round(100.0 - (user.eth_value * 100 / eth_now), 2)}%\n\n"

    if user.bnb_value:
        bnb_now = await get_crypto_now("BNB", "EUR")
        bnb_now = round(float(bnb_now), 2)
        msg += f"BNB:\nLast request: {user.bnb_value}€\nCurrent BNB: {bnb_now}€\nDifference since last request:\n" \
               f" {round(bnb_now - user.bnb_value, 2)}€, {round(100.0 - (user.bnb_value * 100 / bnb_now), 2)}%\n\n"

    if user.dot_value:
        dot_now = await get_crypto_now("DOT", "EUR")
        dot_now = round(float(dot_now), 2)
        msg += f"DOT:\nLast request: {user.dot_value}€\nCurrent DOT: {dot_now}€\nDifference since last request:\n" \
               f" {round(dot_now - user.dot_value, 2)}€, {round(100.0 - (user.dot_value * 100 / dot_now), 2)}%\n\n"

    await message.answer(text=msg)
