from aiogram import Bot, Dispatcher, types
from config import API_TOKEN
from data.base import Database
from data.acsess import RAM
from data.settings import Setting
from utilits.states import RegistirState, OrderProdactState
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from buttons.defolt import Defolt
from buttons.inline import InlineButtons


storage = MemoryStorage()
bot = Bot(token = API_TOKEN)
dp = Dispatcher(bot, storage = storage)

db = Database('data/database.db')
ram = RAM('data/database.db')
setting = Setting('data/setting.json')


registir_state = RegistirState()
order_state = OrderProdactState()

menu = Defolt()
inline_buttons = InlineButtons()