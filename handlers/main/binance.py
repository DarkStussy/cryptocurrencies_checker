import os

from aiogram import types
from binance import AsyncClient

from data.config import admin_id
from loader import dp

from keyboard.inline import binance_inline_kb


@dp.message_handler(lambda message: message.chat.id == admin_id, commands=['binance'])
async def send_menu(message: types.Message):
    await message.answer('Binance menu: ', reply_markup=binance_inline_kb)


@dp.callback_query_handler(lambda c: c.data == 'check_balance')
async def callback_check_balance(callback_query: types.CallbackQuery):
    await dp.bot.edit_message_reply_markup(callback_query.message.chat.id, callback_query.message.message_id,
                                           reply_markup=None)
    client = await AsyncClient.create(api_key=os.getenv("BINANCE_API_KEY"), api_secret=os.getenv("BINANCE_API_SECRET"))

    balance_btc = await client.get_asset_balance(asset='BTC')
    balance_eth = await client.get_asset_balance(asset='ETH')
    balance_eur = await client.get_asset_balance(asset='EUR')
    balance_usdt = await client.get_asset_balance(asset='USDT')
    price_btc = await client.get_avg_price(symbol='BTCEUR')
    price_eth = await client.get_avg_price(symbol='ETHEUR')
    msg = f"Your balance:\n\nBTC: {balance_btc['free']}," \
          f" {round(float(balance_btc['free']) * float(price_btc['price']), 2)}€" \
          f"\nETH: {balance_eth['free']}, {round(float(balance_eth['free']) * float(price_eth['price']), 2)}€" \
          f"\nEUR: {balance_eur['free']}" \
          f"\nUSDT: {balance_usdt['free']}"
    await dp.bot.send_message(chat_id=callback_query.message.chat.id, text=msg)

    await client.close_connection()
