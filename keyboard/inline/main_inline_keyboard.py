from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

inline_btn_btc_track = InlineKeyboardButton('Отслеживать биткоин', callback_data='btc_track')
inline_btn_eth_track = InlineKeyboardButton('Отслеживать эфириум', callback_data='eth_track')
inline_kb_main = InlineKeyboardMarkup().add(inline_btn_btc_track).add(inline_btn_eth_track)
