from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import ContentTypes

from data.config import get_crypto_now
from db.models import User
from loader import dp

from states import GetDiff

from keyboard.inline import inline_kb_main


async def db_merge_currency(user_id: int, difference: float, btc_value: float = None, eth_value: float = None,
                            bnb_value: float = None, dot_value: float = None):
    db_session = dp.bot.get("db")
    async with db_session() as session:
        if btc_value:
            await session.merge(User(user_id=user_id,
                                     btc_value=btc_value, difference_btc=difference, is_checked_btc=False))
        if eth_value:
            await session.merge(User(user_id=user_id,
                                     eth_value=eth_value, difference_eth=difference, is_checked_eth=False))
        if bnb_value:
            await session.merge(User(user_id=user_id,
                                     bnb_value=bnb_value, difference_bnb=difference, is_checked_bnb=False))
        if dot_value:
            await session.merge(User(user_id=user_id,
                                     dot_value=dot_value, difference_dot=difference, is_checked_dot=False))
        await session.commit()


@dp.callback_query_handler(lambda c: c.data == 'btc_track')
async def callback_track_btc(callback_query: types.CallbackQuery):
    await dp.bot.edit_message_reply_markup(callback_query.message.chat.id, callback_query.message.message_id,
                                           reply_markup=None)
    await dp.bot.send_message(chat_id=callback_query.message.chat.id, text='Enter difference for change notification:')
    await GetDiff.difference_btc.set()


@dp.callback_query_handler(lambda c: c.data == 'eth_track')
async def callback_track_eth(callback_query: types.CallbackQuery):
    await dp.bot.edit_message_reply_markup(callback_query.message.chat.id, callback_query.message.message_id,
                                           reply_markup=None)
    await dp.bot.send_message(chat_id=callback_query.message.chat.id, text='Enter difference for change notification:')
    await GetDiff.difference_eth.set()


@dp.callback_query_handler(lambda c: c.data == 'bnb_track')
async def callback_track_bnb(callback_query: types.CallbackQuery):
    await dp.bot.edit_message_reply_markup(callback_query.message.chat.id, callback_query.message.message_id,
                                           reply_markup=None)
    await dp.bot.send_message(chat_id=callback_query.message.chat.id, text='Enter difference for change notification:')
    await GetDiff.difference_bnb.set()


@dp.callback_query_handler(lambda c: c.data == 'dot_track')
async def callback_track_dot(callback_query: types.CallbackQuery):
    await dp.bot.edit_message_reply_markup(callback_query.message.chat.id, callback_query.message.message_id,
                                           reply_markup=None)
    await dp.bot.send_message(chat_id=callback_query.message.chat.id, text='Enter difference for change notification:')
    await GetDiff.difference_dot.set()


@dp.callback_query_handler(lambda c: c.data == 'exit_tracking')
async def callback_exit_tracking(callback_query: types.CallbackQuery):
    await dp.bot.edit_message_reply_markup(callback_query.message.chat.id, callback_query.message.message_id,
                                           reply_markup=inline_kb_main)


@dp.message_handler(state=GetDiff.difference_btc, content_types=ContentTypes.TEXT)
async def track_btc_state(message: types.Message, state: FSMContext):
    try:
        diff = round(float(message.text), 2)
    except ValueError:
        await message.answer("Enter number!")
    else:
        current = await get_crypto_now("BTC", "EUR")
        current = round(float(current), 2)
        await db_merge_currency(user_id=message.chat.id, difference=diff, btc_value=current)
        await message.answer(text=f'BTC: {current} EUR\n'
                                  f'Difference: {diff}€\n\n'
                                  f'To check the changes, enter the command: /check')
        await state.finish()


@dp.message_handler(state=GetDiff.difference_eth, content_types=ContentTypes.TEXT)
async def track_eth_state(message: types.Message, state: FSMContext):
    try:
        diff = round(float(message.text), 2)
    except ValueError:
        await message.answer("Enter number!")
    else:
        current = await get_crypto_now("ETH", "EUR")
        current = round(float(current), 2)
        await db_merge_currency(user_id=message.chat.id, difference=diff, eth_value=round(float(current), 2))
        await message.answer(text=f'ETH: {current} €\n'
                                  f'Difference: {diff}€\n\n'
                                  f'To check the changes, enter the command: /check')
        await state.finish()


@dp.message_handler(state=GetDiff.difference_bnb, content_types=ContentTypes.TEXT)
async def track_bnb_state(message: types.Message, state: FSMContext):
    try:
        diff = round(float(message.text), 2)
    except ValueError:
        await message.answer("Enter number!")
    else:
        current = await get_crypto_now("BNB", "EUR")
        current = round(float(current), 2)
        await db_merge_currency(user_id=message.chat.id, difference=diff, bnb_value=round(float(current), 2))
        await message.answer(text=f'BNB: {current} €\n'
                                  f'Difference: {diff}€\n\n'
                                  f'To check the changes, enter the command: /check')
        await state.finish()


@dp.message_handler(state=GetDiff.difference_dot, content_types=ContentTypes.TEXT)
async def track_dot_state(message: types.Message, state: FSMContext):
    try:
        diff = round(float(message.text), 2)
    except ValueError:
        await message.answer("Enter number!")
    else:
        current = await get_crypto_now("DOT", "EUR")
        current = round(float(current), 2)
        await db_merge_currency(user_id=message.chat.id, difference=diff, dot_value=round(float(current), 2))
        await message.answer(text=f'DOT: {current} €\n'
                                  f'Difference: {diff}€\n\n'
                                  f'To check the changes, enter the command: /check')
        await state.finish()
