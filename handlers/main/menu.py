from aiogram import types
from loader import dp

from keyboard.inline import inline_kb_main


@dp.message_handler(commands=['menu'])
async def send_menu(message: types.Message):
    await message.answer('Menu: ', reply_markup=inline_kb_main)
