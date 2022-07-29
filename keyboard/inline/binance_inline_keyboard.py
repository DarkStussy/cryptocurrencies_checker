from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

inline_btn_check_balance = InlineKeyboardButton('Check balance', callback_data='check_balance')
inline_btn_exit_binance = InlineKeyboardButton('Exit', callback_data='exit_binance')
binance_inline_kb = InlineKeyboardMarkup().add(inline_btn_check_balance).add(inline_btn_exit_binance)
