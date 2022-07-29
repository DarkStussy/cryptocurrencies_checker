from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

inline_tracking_button = InlineKeyboardButton("Tracking prices", callback_data='track_prices')
inline_btn_check_price = InlineKeyboardButton("Check price", callback_data='check_price')
inline_btn_exit = InlineKeyboardButton("Exit", callback_data='exit_menu')
inline_kb_main = InlineKeyboardMarkup().add(inline_tracking_button).add(inline_btn_check_price).add(inline_btn_exit)
