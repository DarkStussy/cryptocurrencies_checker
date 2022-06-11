from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import ContentTypes

from db.models import User
from loader import dp
import cryptocompare

from states import GetDiff


async def db_merge_currency(user_id: int, difference: float, btc_value: float = None, eth_value: float = None):
    db_session = dp.bot.get("db")
    async with db_session() as session:
        if btc_value:
            await session.merge(User(user_id=user_id,
                                     btc_value=btc_value, difference_btc=difference, is_checked_btc=False))
        if eth_value:
            await session.merge(User(user_id=user_id,
                                     eth_value=eth_value, difference_eth=difference, is_checked_eth=False))
        await session.commit()


@dp.callback_query_handler(lambda c: c.data == 'btc_track')
async def callback_track_btc(callback_query: types.CallbackQuery):
    await dp.bot.answer_callback_query(callback_query.id)
    await dp.bot.edit_message_reply_markup(callback_query.message.chat.id, callback_query.message.message_id,
                                           reply_markup=None)
    await dp.bot.send_message(chat_id=callback_query.message.chat.id, text='Enter difference for change notification:')
    await GetDiff.difference_btc.set()


@dp.callback_query_handler(lambda c: c.data == 'eth_track')
async def callback_track_eth(callback_query: types.CallbackQuery):
    await dp.bot.answer_callback_query(callback_query.id)
    await dp.bot.edit_message_reply_markup(callback_query.message.chat.id, callback_query.message.message_id,
                                           reply_markup=None)
    await dp.bot.send_message(chat_id=callback_query.message.chat.id, text='Enter difference for change notification:')
    await GetDiff.difference_eth.set()


@dp.message_handler(state=GetDiff.difference_btc, content_types=ContentTypes.TEXT)
async def track_btc_state(message: types.Message, state: FSMContext):
    try:
        diff = float(message.text)
    except ValueError:
        await message.answer("Enter number!")
    else:
        current = cryptocompare.get_price("BTC", currency='USD')['BTC']['USD']
        await db_merge_currency(user_id=message.chat.id, difference=diff, btc_value=current)
        await message.answer(text=f'BTC: {current} USD\n'
                                  f'Difference: {diff}$\n\n'
                                  f'To check the changes, enter the command: /check')
        await state.finish()


@dp.message_handler(state=GetDiff.difference_eth, content_types=ContentTypes.TEXT)
async def track_eth_state(message: types.Message, state: FSMContext):
    try:
        diff = float(message.text)
    except ValueError:
        await message.answer("Enter number!")
    else:
        current = cryptocompare.get_price("ETH", currency='USD')['ETH']['USD']
        await db_merge_currency(user_id=message.chat.id, difference=diff, eth_value=current)
        await message.answer(text=f'ETH: {current} USD\n'
                                  f'Difference: {diff}$\n\n'
                                  f'To check the changes, enter the command: /check')
        await state.finish()
