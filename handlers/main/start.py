from aiogram import types
from loader import dp


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply('Hello! I\'m help to tracking cryptocurrencies.\n'
                        'Enter: /menu')
