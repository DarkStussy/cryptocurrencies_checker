from aiogram import types
from aiogram.types import ContentType
from loader import dp


@dp.message_handler(content_types=ContentType.ANY)
async def unknown_message(message: types.Message):
    message_text = 'My features are slightly limited so I can\'t reply to everything.'

    await message.reply(message_text)
