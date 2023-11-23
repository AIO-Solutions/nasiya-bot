from loader import dp, db, ram, order_state, types, menu, inline_buttons, setting
from aiogram.dispatcher import FSMContext


@dp.message_handler(state = [order_state.get_prodact_name])
async def orrder_id(message : types.Message, state : FSMContext):
    if message.text == "⬅️ Orqaga":
        await message.answer("Bosh menu", reply_markup = menu.user_menu())
        await state.finish()
        
    else:
        await state.set_state(order_state.buy_type_byname)
        
        ram.save_order(id = message.from_user.id, name = message.text)
        # ram.order_prodact_name(id = message.from_user.id, name = message.text)
        await message.answer(f"📝 Buyurtma nomi: {message.text},\nQanaqa usulda to'lo'v qilmoqchisz?", 
                             reply_markup = menu.chose_pay_type())


@dp.message_handler(state = order_state.buy_type_byname)
async def buy_type_byname(message : types.Message, state : FSMContext):
    if message.text == "⬅️ Orqaga":
        await state.set_state(order_state.get_prodact_name)

        await message.answer("🛒", reply_markup = menu.back())
        await message.answer("Buyurtma berish uchun mahsulot nomini kiriting yoki kanlimzdagi postlarni sotib olish tugmasni bosing", 
                                 reply_markup = inline_buttons.go_main_chanel(setting.data['main_chanel']))
        
    elif message.text == "💰 Naxt":
        id = message.from_user.id
        ram.save_order(id = id, buy_type = "naxt")
        await state.set_state(order_state.sure_about_info_byname)

        user_data = ram.users[id]
        order_data = ram.orders[id]
        await message.answer(f"Malumotlar to'gri kirtlganiga ishonch xosil qilng\nismi : {user_data['name']}\ntelefo'n raqam:  {user_data['number']}\nBuyurtma nomi: {order_data['name']}\nTo'lo'v: {order_data['order_type']}",
                             reply_markup = menu.sure_registr_info())

    elif message.text == "💸 Nasiya":
        id = message.from_user.id
        ram.save_order(id = id, buy_type = "nasiya")
        await state.set_state(order_state.sure_about_info_byname)

        user_data = ram.users[id]
        order_data = ram.orders[id]
        await message.answer(f"Malumotlar to'gri kirtlganiga ishonch xosil qilng\nismi : {user_data['name']}\ntelefo'n raqam:  {user_data['number']}\nBuyurtma nomi: {order_data['name']}\nTo'lo'v: {order_data['order_type']}",
                             reply_markup = menu.sure_registr_info())

    elif message.text == "🎛 Bosh menu":
        await state.finish()
        await message.answer(text = "Bosh menu", reply_markup = menu.user_menu())
    
    else:
        await message.answer("Quydagi tugmalrdan birni bosing", reply_markup = menu.chose_pay_type())


@dp.message_handler(state = order_state.sure_about_info_byname)
async def sure_about_info_byname(message : types.Message, state : FSMContext):
    if message.text == "✅ To'g'ri":
        data = ram.orders[message.from_user.id]
        db.save_order(by_name = True, order_name = data['name'], user_id = message.from_user.id,
                      ordered_time = 'xozir', pay_type = data['order_type'])
        
        await state.finish()
        await message.answer("Sizng buyurtmangiz qabul qilind. Tez orada Sotuvchimiz siz bilan bog'lanadi", 
                             reply_markup = menu.user_menu())
    
    elif message.text == "🔄 Qaytadan kiritish":
        await state.set_state(order_state.get_prodact_name)

        await message.answer("🛒", reply_markup = menu.back())
        await message.answer("Buyurtma berish uchun mahsulot nomini kiriting yoki kanlimzdagi postlarni sotib olish tugmasni bosing", 
                                 reply_markup = inline_buttons.go_main_chanel(setting.data['main_chanel']))

    elif message.text == "⬅️ Orqaga":
        await state.set_state(order_state.buy_type_byname)
        order_data = ram.orders[message.from_user.id]

        await message.answer(f"📝 Buyurtma nomi: {order_data['name']},\nQanaqa usulda to'lo'v qilmoqchisz?", 
                             reply_markup = menu.chose_pay_type())
        
    
