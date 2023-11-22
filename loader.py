from aiogram import Bot, Dispatcher, types
from config import API_TOKEN
from data.base import Database
from data.acsess import RAM
from utilits.states import RegistirState
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from buttons.defolt import Defolt



storage = MemoryStorage()
bot = Bot(token = API_TOKEN)
dp = Dispatcher(bot, storage = storage)

db = Database('data/database.db')
ram = RAM('data/database.db')

registir_state = RegistirState()

menu = Defolt()