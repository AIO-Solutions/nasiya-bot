from loader import dp, ram, types, menu, registir_state
from aiogram.dispatcher import FSMContext


@dp.message_handler()
async def message(message: types.Message, state : FSMContext):
    if ram.is_user(message.from_user.id):
        pass
    
    elif ram.is_admin(message.from_user.id):
        pass
    
    else:
        await message.answer(message.text)