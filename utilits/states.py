from aiogram.dispatcher.filters.state import StatesGroup, State


class RegistirState(StatesGroup):
    get_name = State()
    get_number = State()
    sure_abaut_info = State()
