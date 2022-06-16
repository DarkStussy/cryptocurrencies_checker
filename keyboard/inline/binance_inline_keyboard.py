from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

inline_btn_check_balance = InlineKeyboardButton('Check balance', callback_data='check_balance')
binance_inline_kb = InlineKeyboardMarkup().add(inline_btn_check_balance)
