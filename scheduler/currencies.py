from aiogram.types import ParseMode
from aiogram.utils.markdown import italic
from sqlalchemy import select

from db.models import User
from loader import dp
from data.config import get_crypto_now


async def diff_currency():
    db_session = dp.bot.get("db")
    sql = select(User)
    async with db_session() as session:
        users_request = await session.execute(sql)
        users = users_request.scalars()

    for i in users:
        btc_now = get_crypto_now("BTC", "USD")
        eth_now = get_crypto_now("ETH", "USD")
        print(eth_now)
        message = italic("Notification:") + "\n\n"
        if i.btc_value:
            message += f"BTC:\nLast request: {i.btc_value}$\nCurrent BTC: {btc_now}$\nDifference since last request:" \
                       f" {round(btc_now - i.btc_value, 2)}$, {round(100.0 - (i.btc_value * 100 / btc_now), 2)}%\n\n"
        if i.eth_value:
            message += f"ETH:\nLast request: {i.eth_value}$\nCurrent BTC: {eth_now}$\nDifference since last request:\n" \
                       f" {round(eth_now - i.eth_value, 2)}$, {round(100.0 - (i.eth_value * 100 / eth_now), 2)}%\n\n"

        await dp.bot.send_message(chat_id=i.user_id, text=message,
                                  parse_mode=ParseMode.MARKDOWN)
