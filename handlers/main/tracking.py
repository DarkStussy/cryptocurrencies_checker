from aiogram import types

from db.models import User
from loader import dp
import cryptocompare


async def db_merge_currency(user_id, btc_value=None, eth_value=None):
    db_session = dp.bot.get("db")
    async with db_session() as session:
        if btc_value:
            await session.merge(User(user_id=user_id,
                                     btc_value=btc_value))
        if eth_value:
            await session.merge(User(user_id=user_id,
                                     eth_value=eth_value))
        await session.commit()


@dp.callback_query_handler(lambda c: c.data == 'btc_track')
async def callback_track_btc(callback_query: types.CallbackQuery):
    await dp.bot.answer_callback_query(callback_query.id)
    await dp.bot.edit_message_reply_markup(callback_query.message.chat.id, callback_query.message.message_id,
                                           reply_markup=None)
    current = cryptocompare.get_price("BTC", currency='USD')['BTC']['USD']
    await db_merge_currency(user_id=callback_query.message.chat.id, btc_value=current)
    await dp.bot.send_message(chat_id=callback_query.message.chat.id,
                              text=f'BTC: {current} USD\n\n'
                                   f'Чтобы проверить изменения введите команду: /check')


@dp.callback_query_handler(lambda c: c.data == 'eth_track')
async def callback_track_eth(callback_query: types.CallbackQuery):
    await dp.bot.answer_callback_query(callback_query.id)
    await dp.bot.edit_message_reply_markup(callback_query.message.chat.id, callback_query.message.message_id,
                                           reply_markup=None)
    current = cryptocompare.get_price("ETH", currency='USD')['ETH']['USD']
    await db_merge_currency(user_id=callback_query.message.chat.id, eth_value=current)
    await dp.bot.send_message(chat_id=callback_query.message.chat.id,
                              text=f'ETH: {current} USD\n\n'
                                   f'Чтобы проверить изменения введите команду: /check')
