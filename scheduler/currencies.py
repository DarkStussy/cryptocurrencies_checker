from aiogram.types import ParseMode
from sqlalchemy import select

from db.models import User
from loader import dp
from data.config import get_crypto_now


async def check_diff(value: float, now: float, difference: float, user_id: int, name: str):
    db_session = dp.bot.get("db")
    async with db_session() as session:
        if abs(value - now) > difference:
            if name == "BTC":
                await session.merge(User(user_id=user_id,
                                         is_checked_btc=True))
            elif name == "ETH":
                await session.merge(User(user_id=user_id,
                                         is_checked_eth=True))
            elif name == "BNB":
                await session.merge(User(user_id=user_id,
                                         is_checked_bnb=True))
            elif name == "DOT":
                await session.merge(User(user_id=user_id,
                                         is_checked_dot=True))
            await session.commit()
            await dp.bot.send_message(chat_id=user_id, text=f"WARNING:\n"
                                                            f"{name} REQUEST: {value}€\n"
                                                            f"{name} NOW: {now}€\n"
                                                            f"Difference since last request:\n"
                                                            f"{round(now - value, 2)}€,"
                                                            f" {round(100.0 - (value * 100 / now), 2)}%",
                                      parse_mode=ParseMode.MARKDOWN)


async def diff_currency():
    db_session = dp.bot.get("db")
    sql = select(User)
    async with db_session() as session:
        users_request = await session.execute(sql)
        users = users_request.scalars()
    for i in users:
        if i.btc_value and not i.is_checked_btc:
            btc_now = await get_crypto_now("BTC", "EUR")
            btc_now = round(float(btc_now), 2)
            await check_diff(value=i.btc_value, now=btc_now, difference=i.difference_btc, user_id=i.user_id,
                             name="BTC")
        if i.eth_value and not i.is_checked_eth:
            eth_now = await get_crypto_now("ETH", "EUR")
            eth_now = round(float(eth_now), 2)
            await check_diff(value=i.eth_value, now=eth_now, difference=i.difference_eth, user_id=i.user_id,
                             name="ETH")
        if i.bnb_value and not i.is_checked_bnb:
            bnb_now = await get_crypto_now("BNB", "EUR")
            bnb_now = round(float(bnb_now), 2)
            await check_diff(value=i.bnb_value, now=bnb_now, difference=i.difference_bnb, user_id=i.user_id,
                             name="BNB")
        if i.dot_value and not i.is_checked_dot:
            dot_now = await get_crypto_now("DOT", "EUR")
            dot_now = round(float(dot_now), 2)
            await check_diff(value=i.dot_value, now=dot_now, difference=i.difference_dot, user_id=i.user_id,
                             name="DOT")
