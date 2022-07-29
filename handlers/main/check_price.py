from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import ContentTypes

from data.config import get_crypto_now
from loader import dp
from states.check_price import CheckPrice


@dp.callback_query_handler(lambda c: c.data == 'check_price')
async def callback_tracking_prices(callback_query: types.CallbackQuery):
    await dp.bot.delete_message(chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id)
    await dp.bot.send_message(chat_id=callback_query.message.chat.id, text="Enter cryptocurrency:")
    await CheckPrice.cryptocurrency.set()


@dp.message_handler(state=CheckPrice.cryptocurrency, content_types=ContentTypes.TEXT)
async def enter_cryptocurrency_name(message: types.Message, state: FSMContext):
    try:
        price = await get_crypto_now(message.text, "EUR")
    except KeyError:
        await message.answer(text='Invalid cryptocurrency!')
    else:
        await message.answer(text=f'Cryptocurrency: {message.text}\nPrice: {round(float(price), 2)}€')
        await state.finish()
