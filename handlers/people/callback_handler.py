# from loader import dp, bot, ram, types, Bot, setting
# from aiogram.dispatcher import FSMContext


# async def check_sub(user_id : int, chanel : str):
#     try:
#         bot = Bot.get_current()
#         member  = await bot.get_chat_member(chat_id = chanel, user_id = user_id)
#         # print('-'*10)
#         # print(chanel)
#         # print(member)
#         # print(member.is_chat_member())
#         if member.status != 'left':
#             return True
#         return False
#     except:
#         return False

# @dp.callback_query_handler(state = "*")
# async def main_callback_handler(query : types.InlineQuery, state : FSMContext):
#     current_state = await state.get_state()
#     id = query.from_user.id

#     if not await check_sub(user_id = id, chanel = setting.data['main_chanel_id']):
#         await query.answer(text = "Siz bizning kanlga obuna bo'lmadingiz")
    
    
        