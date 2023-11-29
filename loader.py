from aiogram import Bot, Dispatcher, types
from config import API_TOKEN, TELEGRAP_API_TOKEN
from data.base import Database
from data.acsess import RAM
from data.settings import Setting
from utilits.states import RegistirState, OrderProdactState, UpdateUserData, AdminLogin, AdminPanelState
from utilits.postman import Postman
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from buttons.defolt import Defolt
from buttons.inline import InlineButtons

setting = Setting('data/setting.json')
storage = MemoryStorage()

if setting.data['server'] == '1':
    bot = Bot(token = API_TOKEN, proxy = "http://proxy.server:3128")
else:
    bot = Bot(token = API_TOKEN)
dp = Dispatcher(bot, storage = storage)

db = Database('data/database.db')
ram = RAM('data/database.db')

postman = Postman(token = TELEGRAP_API_TOKEN, telgram_bot_token = API_TOKEN)
registir_state = RegistirState()
order_state = OrderProdactState()
update_user_data = UpdateUserData()
admin_login = AdminLogin()
admin_panel_states = AdminPanelState()

menu = Defolt()
inline_buttons = InlineButtons(setting.data['main_chanel'])