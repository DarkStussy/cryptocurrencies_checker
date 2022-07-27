from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

inline_btn_btc_track = InlineKeyboardButton('Track BITCOIN', callback_data='btc_track')
inline_btn_eth_track = InlineKeyboardButton('Track ETHEREUM', callback_data='eth_track')
inline_btn_bnb_track = InlineKeyboardButton('Track BINANCE COIN', callback_data='bnb_track')
inline_btn_dot_track = InlineKeyboardButton('Track POLKADOT', callback_data='dot_track')
inline_kb_main = InlineKeyboardMarkup().add(inline_btn_btc_track).add(inline_btn_eth_track).add(
    inline_btn_bnb_track).add(inline_btn_dot_track)
