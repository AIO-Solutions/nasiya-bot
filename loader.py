from aiogram import Bot, Dispatcher, types
from config import API_TOKEN, TELEGRAP_API_TOKEN
from data.base import Database
from data.acsess import RAM
from data.settings import Setting
from utilits.states import RegistirState, OrderProdactState, UpdateUserData
from utilits.postman import Postman
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from buttons.defolt import Defolt
from buttons.inline import InlineButtons


storage = MemoryStorage()
bot = Bot(token = API_TOKEN)
dp = Dispatcher(bot, storage = storage)

db = Database('data/database.db')
ram = RAM('data/database.db')
setting = Setting('data/setting.json')
postman = Postman(token = TELEGRAP_API_TOKEN)

registir_state = RegistirState()
order_state = OrderProdactState()
update_user_data = UpdateUserData()

menu = Defolt()
inline_buttons = InlineButtons()