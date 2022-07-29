from aiogram import types
from loader import dp

from keyboard.inline import inline_kb_main, inline_kb_tracking_prices


@dp.message_handler(commands=['menu'])
async def send_menu(message: types.Message):
    await message.answer('Menu: ', reply_markup=inline_kb_main)


@dp.callback_query_handler(lambda c: c.data == 'exit_menu')
async def callback_exit_tracking_prices(callback_query: types.CallbackQuery):
    await dp.bot.delete_message(chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id)


@dp.callback_query_handler(lambda c: c.data == 'track_prices')
async def callback_tracking_prices(callback_query: types.CallbackQuery):
    await dp.bot.edit_message_reply_markup(callback_query.message.chat.id, callback_query.message.message_id,
                                           reply_markup=inline_kb_tracking_prices)
