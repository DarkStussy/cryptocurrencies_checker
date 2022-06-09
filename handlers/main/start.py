from aiogram import types
from loader import dp

from keyboard.inline import inline_kb_main


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply('Привет! Я помогу тебе отслеживать движение биткоина и эфириума)\n'
                        'Введи: /menu, чтобы начать')
