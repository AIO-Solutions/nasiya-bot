from loader import dp, db, types, ram, admin_panel_states, setting, menu
from aiogram.dispatcher import FSMContext

@dp.message_handler(state=admin_panel_states.change_pass)
async def change_pass(message: types.Message, state: FSMContext):
    await message.answer("Parol o'zgartirildi", reply_markup=menu.settings())
    setting.data['pasword'] = message.text
    setting.update()

    await state.finish()