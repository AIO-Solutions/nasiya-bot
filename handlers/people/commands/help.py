from loader import dp, types, inline_buttons, setting, postman, menu
from aiogram.dispatcher import FSMContext
import sqlite3
from aiogram.dispatcher.filters.state import StatesGroup, State

@dp.message_handler(commands='help', state = "*")
async def info(message : types.Message):
    # postman.edit_bot_what_cando("✅  Ushbu bot orqali Grand Nasiya kanaldagi maxsulotlarga buyurtma berishingiz mumkun. \n\n❗️ Sizning malumotlaringiz telefo'n raqam va ismingiz siz bilan aloqaga chiqish uchun ishlatiladi")
    await message.answer("✅  Ushbu bot orqali Grand Nasiya kanaldagi maxsulotlarga buyurtma berishingiz mumkun. \n\n❗️ Sizning malumotlaringiz telefo'n raqam va ismingiz siz bilan aloqaga chiqish uchun ishlatiladi", 
                         reply_markup = inline_buttons.go_main_chanel(url=setting.data['main_chanel']))