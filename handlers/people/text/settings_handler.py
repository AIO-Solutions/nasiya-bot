from loader import dp, db, ram, setting, admin_panel_states, types, menu, bot, postman
from aiogram.dispatcher import FSMContext
import asyncio
import re



@dp.message_handler(state = admin_panel_states.settings)
async def main_settings_handler(update : types.Message, state : FSMContext):
    if update.text == '⬅️ Orqaga':
        await state.finish()
        await update.answer("Bosh menu", reply_markup = menu.admin_menu())
    
    elif update.text == "🔐 Parolni o'zgartish":
        await state.set_state(admin_panel_states.change_paswor_verfy)
        await update.answer("Iltimos hozirgi paro'lni kriting", reply_markup = menu.back())

    
    elif update.text == "📡 Asosiy kanal ➕":
        await state.set_state(admin_panel_states.change_main_chanel)
        await update.answer("Iltimos meni yangi kanalingizga admi qilib qo'shing va kanal havolasni kiriting \nmasalan : https://t.me/grandnasiya", reply_markup = menu.back())

    elif update.text == "🤖 Bot profil info":
        await state.set_state(admin_panel_states.change_bot_info)
        await update.answer("120 belgdan oshmagan bot profil malumotni kriting", reply_markup = menu.back())

    elif update.text == "ℹ️ Biz haqimzda":
        await state.set_state(admin_panel_states.change_about_us)
        await update.answer("Biz haqimzda tugmasi uchun malumot kriting", reply_markup=menu.back())

    else:
        await update.answer("Quydagi tugmalrdan brni bosing", reply_markup = menu.settings())



@dp.message_handler(state = admin_panel_states.change_paswor_verfy)
async def change_paswor_verfy(update : types.Message, state : FSMContext):
    if update.text == '⬅️ Orqaga':
        await state.set_state(admin_panel_states.settings)
        await update.answer("Sozlamalar menyus", reply_markup = menu.settings())
    
    elif update.text == setting.data['pasword']:
        await bot.delete_message(chat_id = update.from_user.id, message_id = update.message_id)
        message_data = await bot.send_sticker(chat_id = update.from_user.id, sticker = 'CAACAgIAAxkBAAI6tWU1NXTI6ZhBHGkyBqEPXPtdO-M-AAJJAgACVp29CiqXDJ0IUyEOMAQ')

        await state.set_state(admin_panel_states.change_pasword)
        await bot.send_message(text = "Yangi paro'lni kriting", reply_markup = menu.back(), chat_id = update.from_user.id)

        await asyncio.sleep(3)
        await bot.delete_message(chat_id = update.from_user.id, message_id = message_data.message_id) 
    else:
        await update.reply("Paro'l xato")


@dp.message_handler(state = admin_panel_states.change_pasword)
async def change_paswor(update : types.Message, state : FSMContext):
    if update.text == '⬅️ Orqaga':
        await state.set_state(admin_panel_states.settings)
        await update.answer("Sozlamalar menyus", reply_markup = menu.settings())
    
    else:
        setting.data['pasword'] = update.text
        setting.update()

        await state.set_state(admin_panel_states.settings)
        await update.answer(text = "Paro'l muvaffaqiyatli o'zgartirldi", reply_markup = menu.settings())

        await asyncio.sleep(15)
        await bot.delete_message(chat_id = update.from_user.id, message_id = update.message_id) 
    


@dp.message_handler(state = admin_panel_states.change_main_chanel)
async def change_chanel_handler(update : types.Message, state : FSMContext):
    if update.text == '⬅️ Orqaga':
        await state.set_state(admin_panel_states.settings)
        await update.answer("Sozlamalar menyus", reply_markup = menu.settings())

    elif re.search(r"^https://t.me/", update.text):
        try: 
            url = update.text
            data = await bot.get_chat(chat_id = '@' + url.replace('https://t.me/', ''))
            chanel_id = data.id
            admins = await bot.get_chat_administrators(chat_id = chanel_id)

            for admin in admins:
                if admin.user.username == 'grand_nasiya_bot':
                    setting.data['main_chanel'] = url
                    setting.data['main_chanel_id'] = chanel_id
                    setting.update()
                    break
            
            await state.set_state(admin_panel_states.settings)
            await update.answer("Kanal muvaffaqiyatli o'zgartirldi", reply_markup = menu.settings())

        except:
            await update.answer("Iltimos birnchi meni admin qiling")
    else:
        await update.answer("Ilitmos kanal linkni to'g'ri kriting")



@dp.message_handler(state = admin_panel_states.change_bot_info)
async def change_bot_info_handler(update : types.Message, state : FSMContext):
    if update.text == '⬅️ Orqaga':
        await state.set_state(admin_panel_states.settings)
        await update.answer("Sozlamalar menyus", reply_markup = menu.settings())

    elif len(update.text) < 120:
        postman.edit_bot_describtion(update.text)
        await state.set_state(admin_panel_states.settings)
        await update.answer("Bot profil malumot muvaffaqiyatli yangilandi", reply_markup = menu.settings())

    else:
        await update.answer("Belglra soni 120 tadan oshib ketdi", reply_markup = menu.back())



@dp.message_handler(state = admin_panel_states.change_about_us)
async def change_about_us(update : types.Message, state : FSMContext):
    if update.text == '⬅️ Orqaga':
        await state.set_state(admin_panel_states.settings)
        await update.answer("Sozlamalar menyus", reply_markup = menu.settings())
    
    else:
        setting.data['about_us'] = update.text
        setting.update()

        await state.set_state(admin_panel_states.settings)
        await update.reply("Malumot muvaffaqiyatli yuklandi", reply_markup = menu.settings())
    
