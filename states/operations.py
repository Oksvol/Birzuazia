from aiogram.dispatcher.filters.state import StatesGroup, State


class Operation(StatesGroup):
    quantity = State()