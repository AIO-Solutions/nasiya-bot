from loader import dp, ram, types, menu, registir_state
from aiogram.dispatcher import FSMContext


@dp.message_handler()
async def message(message: types.Message, state : FSMContext):
    if ram.is_user(message.from_user.id):
        await message.answer("siz users")
    
    elif ram.is_admin(message.from_user.id):
        pass
    
    else:
        await message.answer("Assalomu alykum Grand Nasiya kanlinig rasmiy bo'tiga xush kelibsiz.\nIltimos ismingizni kiriting")
        # await message.answer("Iltimos ismingizni kiriting")
        await state.set_state(registir_state.get_name)
    print(message.text)