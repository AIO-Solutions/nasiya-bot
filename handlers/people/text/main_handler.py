from loader import dp, db, ram, types, menu, registir_state, order_state, setting, inline_buttons, bot, update_user_data, admin_login, admin_panel_states
from aiogram.dispatcher import FSMContext

months = {
    '1' : 'yanvar',
    '2' : 'fevral',
    '3' : 'mart',
    '4' : 'aprel',
    '5' : 'may',
    '6' : 'iyun',
    '7' : 'iyul',
    '8' : 'avgust',
    '9' : 'sentyabr',
    '10': 'oktyabr',
    '11': 'noyabr',
    '12': 'dekabr' 
}

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
            data = ram.users[message.from_user.id]
            await state.set_state(state = update_user_data.want_to_update)
            await message.answer(f"Malumotlaringzni o'zgartirishni hoxlaysizmi? \n👤 isim: {data['name']}\n📱 Telefo'n raqam: {data['number']}", reply_markup = menu.yes_or_no())

    
    elif ram.is_admin(message.from_user.id):
        data = ram.admins[message.from_user.id]
        
        
        if message.text == "💰 Naxtga":
            prodact_data, orders_id = db.get_orders(cash = True, ofset = 0)
            if len(prodact_data) >= 1:
                answer = ""
                n = 1
                for prodact in prodact_data:
                    answer += f"{n}.👤 {prodact['user_name']}"
                    month_index = prodact['ordered_time'].split('.')[1]
                    answer += f"  ⌛️ {prodact['ordered_time'].split('.')[0]}-{months[month_index]} {prodact['ordered_time'].split(' ')[-1]}"
                    
                    if prodact.get('order_name'):
                        answer += f"\n📦 Buyurtma nomi:{prodact['order_name']}"

                    
                    answer += '\n\n' + '_'*45
                    answer += "\n\n"
                    n+=1

                # print(orders_id)
                await message.answer(answer, reply_markup = inline_buttons.cash_menu_buttons(ids = orders_id))
            else:
                await message.answer("Xozircha buyurtma yo'q", reply_markup = menu.admin_menu())
            
        elif not data['where']:
            data['where'] = 'head_men'
            await message.answer("Bosh menu", reply_markup = menu.admin_menu())
            
            
        else:
            await message.answer("Quydagi tugmalrdan birni bosing", reply_markup = menu.admin_menu())
    
    else:
        await bot.set_my_commands(commands = [types.BotCommand(command = '/start', description = "Botni ishga tushirish"), 
                                          types.BotCommand(command = '/restart', description = "Botni qayta ishga tushirish"),
                                          types.BotCommand(command = '/help', description = "Yordam"),
                                          types.BotCommand(command = '/admin', description = "Admin panelga kirish")])

        await message.answer("Assalomu alykum Grand Nasiya kanlinig rasmiy bo'tiga xush kelibsiz.\nIltimos ismingizni kiriting")
        await state.set_state(registir_state.get_name)


@dp.message_handler(content_types = types.ContentType.STICKER)
async def sticer_handler(message : types.Message):
    print(message)
