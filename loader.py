from aiogram import Bot, Dispatcher, types
from config import API_TOKEN
from data.base import Database
from data.acsess import RAM

bot = Bot(token = API_TOKEN)
dp = Dispatcher(bot)

db = Database('data/database.db')
ram = RAM('data/database.db')