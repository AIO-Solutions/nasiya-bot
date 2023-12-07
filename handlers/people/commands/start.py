from loader import dp, ram, types, registir_state, menu, bot, setting, order_state
from aiogram.dispatcher import FSMContext
from utilits.states import RegistirState

@dp.message_handler(commands = ['start', 'restart'], state = '*')
async def start_command(message : types.Message, state : FSMContext):
    await bot.set_my_commands(commands = [types.BotCommand(command = '/start', description = "Botni ishga tushirish"), 
                                          types.BotCommand(command = '/restart', description = "Botni qayta ishga tushirish"),
                                          types.BotCommand(command = '/help', description = "Yordam"),
                                          types.BotCommand(command = '/admin', description = "Admin panelga krish"),
                                          types.BotCommand(command = '/logout', description = "Admin paneldan chqish")])
    
    current_state = await state.get_state()
    prodact_id = message.text.split(' ')[-1]

    if not current_state:  # If user not in state
        if prodact_id.isnumeric():  # If have prodact order
            if ram.is_user(message.from_user.id):
                try:
                    await bot.copy_message(chat_id = message.from_user.id, from_chat_id = setting.data['main_chanel_id'], message_id = prodact_id)
                    
                    await message.answer("Qanaqa usulda 💰 to'lo'v qilmoqchisiz?", reply_markup = menu.chose_pay_type(by_id=True))
                    await state.set_state(order_state.buy_type_byid)
                    ram.save_order(id = message.from_user.id, order_id = prodact_id)
                
                except:
                    await message.answer("😞 Afsuski mahsulot topilmadi", reply_markup = menu.user_menu())
    
            elif ram.is_admin(message.from_user.id):
                await message.answer("❗️ Siz adminsiz, 😁 adminlar buyurtma bera olmaydi", reply_markup = menu.admin_menu())

            else:
                await state.set_state(registir_state.get_name)
                await message.answer("Assalomu alaykum, Xush kelibsiz.📦 Buyurtma berishdan oldin iltimos 👤 ismingizni kriting",
                                     reply_markup = types.ReplyKeyboardRemove())
                ram.registr_data(id = message.from_user.id, order_id = prodact_id)
    
        else: # don't have prodact id
            if ram.is_user(message.from_user.id):
                await message.answer("🎛 Bosh menu", reply_markup = menu.user_menu())
    
            elif ram.is_admin(message.from_user.id):
                await message.answer("🎛 Bosh menu", reply_markup = menu.admin_menu())

            else:
                await state.set_state(registir_state.get_name)
                await message.answer("Assalomu alaykum, Xush kelibsiz. Iltimos ismingizni kiriting", 
                                     reply_markup = types.ReplyKeyboardRemove())
    
    else: # Else user in state
        if prodact_id.isnumeric():
            if ram.is_user(message.from_user.id):
                try:
                    await bot.copy_message(chat_id = message.from_user.id, from_chat_id = setting.data['main_chanel_id'], message_id = prodact_id)
                    
                    await message.answer("Qanaqa usulda 💰 to'lo'v qilmoqchisiz?", reply_markup = menu.chose_pay_type(by_id=True))
                    await state.set_state(order_state.buy_type_byid)
                    ram.save_order(id = message.from_user.id, order_id = prodact_id)
                    

                except:
                    await state.finish()
                    await message.answer("😞 Afsuski mahsulot topilmadi", reply_markup = menu.user_menu())
    
            elif ram.is_admin(message.from_user.id):
                await message.answer("❗️ Siz adminsiz, 😁 adminlar buyurtma bera olmaydi", reply_markup = menu.admin_menu())

            else:
                await state.set_state(registir_state.get_name)
                await message.answer("Assalomu alaykum, Xush kelibsiz.📦 Buyurtma berishdan oldin iltimos 👤 ismingizni kriting",
                                     reply_markup = types.ReplyKeyboardRemove())
                ram.registr_data(id = message.from_user.id, order_id = prodact_id)
    
        else:
            if ram.is_user(message.from_user.id):
                await state.finish()
                ram.users[message.from_user.id]['where'] = 'head_menu'
                await message.answer("🎛 Bosh menu", reply_markup = menu.user_menu())
    
            elif ram.is_admin(message.from_user.id):
                await state.finish()
                await message.answer("🎛 Bosh menu", reply_markup = menu.admin_menu())


            else:
                await state.set_state(registir_state.get_name)
                await message.answer("Assalomu alaykum Xush kelibsiz. Iltimos ismingizni kiriting", 
                                     reply_markup = types.ReplyKeyboardRemove())