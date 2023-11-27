from loader import types, dp, ram, menu, admin_login
from aiogram.dispatcher import FSMContext


@dp.message_handler(commands = 'admin', state = "*")
async def admin(message : types.Message, state : FSMContext):
    id = message.from_user.id
   
    if ram.is_user(id):
        if ram.admin_login(id) < 3:
            await state.set_state(admin_login.adim_login)
            await message.answer("Admin panelga kirish uchun paro'lni kiriting", reply_markup = menu.back())
        else:
            await message.answer("Siz bloklangansiz! Iltimos keyinroq urinib ko'ring.")
    
    elif ram.is_admin(id):
        await message.reply("Siz adminsiz", reply_markup = menu.admin_menu())
    else:
        # name = message.from_user.first_name
        # ram.registr(id = id, name = name)
        await message.answer(f"Siz ro'yxatdan o'tmagansiz")


@dp.message_handler(commands = 'logout', state = '*')
async def admin_logout_handler(update : types.Message, state : FSMContext):
    if ram.is_admin(update.from_user.id):
        await state.set_state(admin_login.admin_logout)
        await update.answer("Admin paneldan chiqishni xoxlaysizmi?", reply_markup = menu.live_admin_panel())