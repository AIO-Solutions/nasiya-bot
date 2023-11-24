from aiogram.dispatcher.filters.state import StatesGroup, State


class RegistirState(StatesGroup):
    get_name = State()
    get_number = State()
    sure_abaut_info = State()


class OrderProdactState(StatesGroup):
    get_prodact_name = State()
    buy_type_byname = State()
    sure_about_info_byname = State()

    buy_type_byid = State()
    sure_about_info_byid = State()


class UpdateUserData(StatesGroup):
    want_to_update = State()
    get_name = State()
    get_number = State()
    have_finished = State()

    
