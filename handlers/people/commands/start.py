from loader import dp, ram, types, registir_state
from aiogram.dispatcher import FSMContext
from utilits.states import RegistirState

@dp.message_handler(commands = 'start')
async def start_command(message : types.Message, state : FSMContext):
    # if len(message.text) < 5
    prodact_id = message.text.split(' ')[-1]

    if prodact_id.isnumeric():
        if ram.is_user(message.from_user.id):
            await message.answer("the prodact id is" + prodact_id)
    
        elif ram.is_admin(message.from_user.id):
            pass

        else:
            await state.set_state(registir_state.get_name)
            await message.answer("Assalomu alykum, Xush kelibsiz. Buyurtma berishdan oldin iltimos ismingizni kiriting")
            ram.registr_data(id = message.from_user.id, order_id = prodact_id)
    
    else:
        if ram.is_user(message.from_user.id):
            await message.answer("You are user")
    
        elif ram.is_admin(message.from_user.id):
            pass

        else:
            await state.set_state(registir_state.get_name)
            await message.answer("Assalomu alykum Xush kelibsiz. iltimos ismingizni kiriting")