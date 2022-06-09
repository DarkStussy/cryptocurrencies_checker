from aiogram import types, Dispatcher


async def set_default_commands(dp: Dispatcher):
    await dp.bot.set_my_commands([
        types.BotCommand('start', 'Запустить бота'),
        types.BotCommand('check', 'Проверить изменение криптовалют'),
        types.BotCommand('menu', 'Меню'),
    ])
