from aiogram import types, Dispatcher


async def set_default_commands(dp: Dispatcher):
    await dp.bot.set_my_commands([
        types.BotCommand('start', 'Run the bot'),
        types.BotCommand('check', 'Check changes since last tracking'),
        types.BotCommand('menu', 'Menu'),
    ])
