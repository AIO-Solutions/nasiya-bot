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

class AdminLogin(StatesGroup):
    adim_login = State()
    admin_logout = State()


class AdminPanelState(StatesGroup):
    loan_orders = State()
    cash_orders = State()
    order_history = State()

    change_paswor_verfy = State()
    change_pasword = State()

    change_main_chanel = State()
    change_bot_info = State()

    change_about_us = State()
    change_questions = State()

    add_question = State()
    get_question = State()
    get_answer = State()
    question_add_sure = State()

    remove_question = State()

    settings = State()
    change_pass = State()
    question_edit = State()

    
    
