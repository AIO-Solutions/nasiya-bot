from loader import dp, db, bot, ram, types, Bot, setting, inline_buttons, menu
from aiogram.dispatcher import FSMContext

months = {
    '1' : 'yanvar',
    '2' : 'fevral',
    '3' : 'mart',
    '4' : 'aprel',
    '5' : 'may',
    '6' : 'iyun',
    '7' : 'iyul',
    '8' : 'avgust',
    '9' : 'sentyabr',
    '10': 'oktyabr',
    '11': 'noyabr',
    '12': 'dekabr' 
}

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

        elif command == 'back_cash':
            prodact_data, orders_id = db.get_orders(cash = True, ofset = int(param))
            if len(prodact_data) >= 1:
                answer = ""
                n = 1
                for prodact in prodact_data:
                    answer += f"{n}.👤 {prodact['user_name']}"
                    month_index = prodact['ordered_time'].split('.')[1]
                    answer += f"  ⌛️ {prodact['ordered_time'].split('.')[0]}-{months[month_index]} {prodact['ordered_time'].split(' ')[-1]}"
                    
                    if prodact.get('order_name'):
                        answer += f"\n📦 Buyurtma nomi:{prodact['order_name']}"

                    
                    answer += '\n\n' + '_'*40
                    answer += "\n\n"
                    n+=1

                # print(orders_id)
                await bot.edit_message_text(text = answer, 
                                        chat_id = update.from_user.id,
                                        message_id = update.message.message_id,
                                        reply_markup = inline_buttons.cash_menu_buttons(ids = orders_id))
                # await message.answer(answer, reply_markup = inline_buttons.cash_menu_buttons(ids = orders_id))
            else:
                await bot.send_message(text = "Xozircha buyurtma yo'q", chat_id = update.from_user.id, reply_markup = menu.admin_menu())
        
        elif command == 'cash':
            param = param.split('&')
            last = param[-1]
            param = param[0]

            order_data = db.get_order(order_id = param)
            month_index = order_data['time'].split('.')[1]

            # print(order_data)
            if order_data['order_name']:
                await bot.edit_message_text(text = f"👤 Buyurtmachi: {ram.users[order_data['user_id']]['name']} \n\n📱 Telefo'n raqam: {ram.users[order_data['user_id']]['number']}  \n\n📦 Buyurtma nomi: {order_data['order_name']}  \n\n⌛️ Buyurtma vaxti: {order_data['time'].split('.')[0]}-{months[month_index]} {order_data['time'].split(' ')[-1]}", 
                                        chat_id = update.from_user.id,
                                        message_id = update.message.message_id,
                                        reply_markup = inline_buttons.cash_order_button(offset = last))
            else:
                await bot.edit_message_text(text = f"👤 Buyurtmachi: {ram.users[order_data['user_id']]['name']} \n\n📱 Telefo'n raqam: {ram.users[order_data['user_id']]['number']}   \n\n⌛️ Buyurtma vaxti:  {order_data['time'].split('.')[0]}-{months[month_index]} {order_data['time'].split(' ')[-1]}", 
                                        chat_id = update.from_user.id,
                                        message_id = update.message.message_id,
                                        reply_markup = inline_buttons.cash_order_button(message_id = order_data['message_id'], offset = last))
            

        
    
        