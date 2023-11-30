from loader import types, dp, ram, admin_login, setting, menu, bot, db
from aiogram.dispatcher import FSMContext
import asyncio

@dp.message_handler(state = admin_login.adim_login)
async def admin_login_handler(message : types.Message, state : FSMContext):
    if message.text == "⬅️ Orqaga":
        await state.finish()
        await message.answer('Bosh menu', reply_markup = menu.user_menu())
    
    elif ram.admin_login(message.from_user.id) < 3:
        if message.text == setting.data['pasword']:
            # ram.registr(id =  message.from_user.id, name = message.from_user.first_name, admin = True)
            ram.registir_admin(id = message.from_user.id)
            await state.finish()
            # await bot.set_my_commands(commands = [types.BotCommand(command = '/start', description = "Botni ishga tushirish"), 
            #                               types.BotCommand(command = '/restart', description = "Botni qayta ishga tushirish"),
            #                               types.BotCommand(command = '/help', description = "Yordam"),
            #                               types.BotCommand(command = '/admin', description = "Admin panelga krish"),
            #                               types.BotCommand(command = '/logout', description = "Admin paneldan chqish")])

            db.delet_user_order(message.from_user.id)
            await bot.delete_message(chat_id = message.from_user.id, message_id = message.message_id)
            message_data = await bot.send_sticker(chat_id = message.from_user.id, sticker = 'CAACAgIAAxkBAAI6tWU1NXTI6ZhBHGkyBqEPXPtdO-M-AAJJAgACVp29CiqXDJ0IUyEOMAQ')
            
            await message.answer("Admin panel", reply_markup = menu.admin_menu())

            await asyncio.sleep(3)
            await bot.delete_message(chat_id = message.from_user.id, message_id = message_data.message_id) 

        else:
            if ram.admin_login(message.from_user.id, block = True) == 3:
                await state.finish()
                await message.answer("Ko'd xato siz bloklandingiz", reply_markup = menu.user_menu())

            else:
                await message.reply(f"Ko'd xato sizda {3 - ram.block[message.from_user.id]} ta urinish qoldi", reply_markup = menu.back())
    
    else:
        await state.finish()
        await message.answer("Siz blo'klandingiz! Iltimos keyinroq urinib ko'ring", menu.user_menu())


@dp.message_handler(state = admin_login.admin_logout)
async def admin_logout_handler_text(update : types.Message, state : FSMContext):
    if update.text == '🚶 Chqish':
        ram.logout_admin(update.from_user.id)
        
        await state.finish()
        await update.answer("Siz admin paneldan chiqdingiz", reply_markup = types.ReplyKeyboardRemove())
        # await bot.set_my_commands(commands = [types.BotCommand(command = '/start', description = "Botni ishga tushirish"), 
        #                                   types.BotCommand(command = '/restart', description = "Botni qayta ishga tushirish"),
        #                                   types.BotCommand(command = '/help', description = "Yordam"),
        #                                   types.BotCommand(command = '/admin', description = "Admin panelga kirish")])
    
    elif update.text == "⬅️ Orqaga":
        await state.finish()
        await update.answer("Bosh menu", reply_markup = menu.admin_menu())
    
    else:
        await update.answer("Quydagi tugmalardan birni bosing", reply_markup = menu.live_admin_panel())