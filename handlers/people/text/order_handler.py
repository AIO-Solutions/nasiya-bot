from loader import dp, db, ram, order_state, types, menu, inline_buttons, setting, bot
from aiogram.dispatcher import FSMContext
from datetime import datetime
import pytz

def now():
    tashkent_tz = pytz.timezone('Asia/Tashkent')
    tashkent_time = datetime.now(tashkent_tz)

    return str(tashkent_time.strftime("%d.%m.%Y %H:%M"))

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
        await message.answer(f"Malumotlar to'gri kirtlganiga ishonch xosil qilng  \n👤 Ism : {user_data['name']} \n📱 Telefo'n raqam:  {user_data['number']}  \n📦 Buyurtma nomi: {order_data['name']} \n💰 To'lo'v usuli: {order_data['order_type']}",
                             reply_markup = menu.sure_registr_info())

    elif message.text == "💸 Nasiya":
        id = message.from_user.id
        ram.save_order(id = id, buy_type = "nasiya")
        await state.set_state(order_state.sure_about_info_byname)

        user_data = ram.users[id]
        order_data = ram.orders[id]
        await message.answer(f"Malumotlar to'gri kirtlganiga ishonch xosil qilng  \n👤 Ism : {user_data['name']} \n 📱 Telefo'n raqam:  {user_data['number']}  \n📦 Buyurtma nomi: {order_data['name']} \n💰 To'lo'v usuli: {order_data['order_type']}",
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
        

        for admin_id in ram.admins.keys():
            await bot.send_message(chat_id = admin_id, text = f"🆕 Yangi buyurtma \n👤Buyurtmachi: {ram.users[message.from_user.id]['name']} \n📱 Telefo'n raqam: {ram.users[message.from_user.id]['number']}\n📦 Buyurtma nomi: {data['name']} \n💰 To'lo'v turi: {data['order_type']}")

        # print(f"🆕 Yangi buyurtma \n👤Buyurtmachi: {ram.users[message.from_user.id]['name']} \n📱 Telefo'n raqam: {ram.users[message.from_user.id]['number']}\n📦 Buyurtma nomi: {data['name']} \n💰 To'lo'v turi: {data['order_type']}")
        
        
        db.save_order(by_name = True, order_name = data['name'], user_id = message.from_user.id,
                      ordered_time = now(), pay_type = data['order_type'])
        
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




#order by id

@dp.message_handler(state = order_state.buy_type_byid)
async def get_buy_type_byid(message : types.Message, state : FSMContext):
    if message.text == "💰 Naxt":
        id = message.from_user.id
        ram.save_order(id = id, buy_type = "naxt")
        await state.set_state(order_state.sure_about_info_byid)

        user_data = ram.users[id]
        order_data = ram.orders[id]
        await message.answer(f"Malumotlar to'gri kirtlganiga ishonch xosil qilng \n👤 Ism: {user_data['name']}  \n📱 Telefo'n raqam: {user_data['number']}  \n💰 To'lo'v: {order_data['order_type']}",
                             reply_markup = menu.sure_registr_info(byid=True))

    elif message.text == "💸 Nasiya":
        id = message.from_user.id
        ram.save_order(id = id, buy_type = "nasiya")
        await state.set_state(order_state.sure_about_info_byid)

        user_data = ram.users[id]
        order_data = ram.orders[id]
        await message.answer(f"Malumotlar to'gri kirtlganiga ishonch xosil qilng \n👤 Ism: {user_data['name']}  \n📱 Telefo'n raqam: {user_data['number']}  \n💰 To'lo'v: {order_data['order_type']}",
                             reply_markup = menu.sure_registr_info(byid=True))
        
    elif message.text == "🎛 Bosh menu":
        await state.finish()
        await message.answer(text = "Bosh menu", reply_markup = menu.user_menu())
    
    else:
        await message.answer("Quydagi tugmalrdan birni bosing", reply_markup = menu.chose_pay_type())



@dp.message_handler(state = order_state.sure_about_info_byid)
async def sure_about_info_byid_handler(message : types.Message, state : FSMContext):
    if message.text == "⬅️ Orqaga":
        await state.set_state(order_state.buy_type_byid)
        await message.answer("Qanqa usulda to'lo'v qilmoqchisiz?", reply_markup = menu.chose_pay_type(by_id=True))
    
    elif message.text == "✅ To'g'ri":
        # print(ram.orders)
        data = ram.orders[message.from_user.id]
        
        for admin_id in ram.admins.keys():
            await bot.send_message(chat_id = admin_id, text = f"🆕 Yangi buyurtma \n👤Buyurtmachi: {ram.users[message.from_user.id]['name']} \n📱 Telefo'n raqam: {ram.users[message.from_user.id]['number']} \n💰 To'lo'v turi: {data['order_type']}",
                                   reply_markup = inline_buttons.see_order(data['order_id']))

        
        db.save_order(by_id = True, message_id = data['order_id'], user_id = message.from_user.id,
                      ordered_time = now(), pay_type = data['order_type'])
        
        await state.finish()
        await message.answer("Sizng buyurtmangiz qabul qilindi. Tez orada Sotuvchimiz siz bilan bog'lanadi", 
                             reply_markup = menu.user_menu())
