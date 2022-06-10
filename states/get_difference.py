from aiogram.dispatcher.filters.state import StatesGroup, State


class GetDiff(StatesGroup):
    difference_btc = State()
    difference_eth = State()
