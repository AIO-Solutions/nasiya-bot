from loader import dp, ram, order_state, types, menu, inline_buttons, setting
from aiogram.dispatcher import FSMContext


@dp.message_handler(state = [order_state.get_prodact_name])
async def orrder_id(message : types.Message, state : FSMContext):
    if message.text == "⬅️ Orqaga":
        await message.answer("Bosh menu", reply_markup = menu.user_menu())
        await state.finish()
        
    else:
        await state.set_state(order_state.buy_type_byname)

        ram.order_prodact_name(id = message.from_user.id, name = message.text)
        await message.answer(f"📝 Buyurtma nomi: {message.text},\nQanaqa usulda to'lo'v qilmoqchisz?", 
                             reply_markup = menu.chose_pay_type())

@dp.message_handler(state = order_state.buy_type_byname)
async def buy_type_byname(message : types.Message, state : FSMContext):
    if message.text == "⬅️ Orqaga":
        await state.set_state(order_state.get_prodact_name)

        await message.answer("🛒", reply_markup = menu.back())
        await message.answer("Buyurtma berish uchun mahsulot nomini kiriting yoki kanlimzdagi postlarni sotib olish tugmasni bosing", 
                                 reply_markup = inline_buttons.go_main_chanel(setting.data['main_chanel']))