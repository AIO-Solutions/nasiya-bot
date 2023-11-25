from loader import dp, types, inline_buttons, setting
from aiogram.dispatcher import FSMContext


@dp.message_handler(commands='help', state = "*")
async def info(message : types.Message):
    await message.answer("✅  Ushbu bot orqali Grand Nasiya kanaldagi maxsulotlarga buyurtma berishingiz mumkun. \n\n❗️ Sizning malumotlaringiz telefo'n raqam va ismingiz siz bilan aloqaga chiqish uchun ishlatiladi", 
                         reply_markup = inline_buttons.go_main_chanel(url=setting.data['main_chanel']))