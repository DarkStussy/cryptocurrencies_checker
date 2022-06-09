from aiogram import types
from aiogram.types import ContentType, ParseMode
from aiogram.utils.markdown import code, text

from loader import dp


@dp.message_handler(content_types=ContentType.ANY)
async def unknown_message(message: types.Message):
    message_text = 'Мои функции слегка ограничены, поэтому я не могу отвечать на всё \n' + code('Команда: ') + text(
        "/help")

    await message.reply(message_text, parse_mode=ParseMode.MARKDOWN)
