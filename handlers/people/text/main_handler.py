from loader import dp, ram, types, menu, registir_state, order_state, setting, inline_buttons, bot
from aiogram.dispatcher import FSMContext


@dp.message_handler()
async def message(message: types.Message, state : FSMContext):
    if ram.is_user(message.from_user.id):
        id = message.from_user.id
        if not ram.users[id]['where']:
            await message.answer("Bosh menu", reply_markup = menu.user_menu())
            ram.users[id]['where'] = 'head_menu'
        
        elif message.text == "🛒 Buyurtma berish":
            await state.set_state(order_state.get_prodact_name)

            await message.answer("🛒", reply_markup = menu.back())
            await message.answer("Buyurtma berish uchun mahsulot nomini kiriting yoki kanlimzdagi postlarni sotib olish tugmasni bosing", 
                                 reply_markup = inline_buttons.go_main_chanel(setting.data['main_chanel']))
            

        elif message.text == "ℹ️ Biz haqimzda":
            await message.answer(setting.data['about_us'], reply_markup = inline_buttons.go_main_chanel(setting.data['main_chanel']))
        
        elif message.text == "⚙️ Malumotlarni o'zgartirish":
            await message.answer("Malumotlaringzni o'zgartirishni xoxlaysimi?")

    
    elif ram.is_admin(message.from_user.id):
        pass
    
    else:
        await message.answer("Assalomu alykum Grand Nasiya kanlinig rasmiy bo'tiga xush kelibsiz.\nIltimos ismingizni kiriting")
        await state.set_state(registir_state.get_name)


@dp.message_handler(content_types = types.ContentType.STICKER)
async def sticer_handler(message : types.Message):
    print(message)
