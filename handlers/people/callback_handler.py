from loader import dp, bot, ram, types, Bot, setting
from aiogram.dispatcher import FSMContext


async def check_sub(user_id : int, chanel : str):
    try:
        bot = Bot.get_current()
        member  = await bot.get_chat_member(chat_id = chanel, user_id = user_id)
        # print('-'*10)
        # print(chanel)
        # print(member)
        # print(member.is_chat_member())
        if member.status != 'left':
            return True
        return False
    except:
        return False

@dp.callback_query_handler(state = "*")
async def main_callback_handler(update : types.CallbackQuery, state : FSMContext):
    current_state = await state.get_state()
    id = update.from_user.id

        
    if update.data == 'delet':
        await bot.delete_message(chat_id = update.from_user.id, message_id = update.message.message_id)
        return None
    

    params = update.data.split('=')
    if len(params) > 1:
        command = params[0]
        param = params[1]

        if command == 'next_cash':
            pass

        elif command == 'last_cash':
            pass
        
        elif command == 'cash':
            pass
            # await bot.edit_message_text(text = "Blah")

        
    
        