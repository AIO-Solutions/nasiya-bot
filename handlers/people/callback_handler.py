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
        try:
            await bot.delete_message(chat_id = update.from_user.id, message_id = update.message.message_id)
        except:
            pass
        return None
    
    # print(update.data)
    params = update.data.split('=')
    if len(params) > 1:
        command = params[0]
        param = params[1]
    
    

        if command == 'next_cash':
            prodact_data, orders_id = db.get_orders(cash = True, ofset = param)
            if len(prodact_data) >= 1:
                n = db.orders_len()
                nex = int(param)+10
                star = int(param)
                if star == 0:
                    star = 1
                elif nex > n:
                    nex = n
                answer = f"Natijalar {star}-{nex} {n} dan\n\n"
                n = 1
                for prodact in prodact_data:
                    answer += f"{n}.👤 {prodact['user_name']}"
                    month_index = prodact['ordered_time'].split('.')[1]
                    answer += f"  ⏱ {prodact['ordered_time'].split('.')[0]}-{months[month_index]} {prodact['ordered_time'].split(' ')[-1]}"
                    
                    if prodact.get('order_name'):
                        answer += f"\n📦 Buyurtma nomi:{prodact['order_name']}"
                    answer += "\n\n"
                    n+=1
                try:
                    await bot.edit_message_text(text = answer, 
                                        chat_id = update.from_user.id,
                                        message_id = update.message.message_id,
                                        reply_markup = inline_buttons.cash_menu_buttons(ids = orders_id, last = int(param), next =  int(param)+10))
                except:
                    pass

            else:
                await update.answer("Boshqa buyurtmalar yo'q")

        elif command == 'last_cash':
            if int(param) >= 10:
                prodact_data, orders_id = db.get_orders(cash = True, ofset = int(param)-10)
                if len(prodact_data) >= 1:
                    n = db.orders_len()
                    nex = int(param)
                    star = int(param)-10
                    if star == 0:
                        start = 1
                    elif nex > n:
                        nex = n
                    answer = f"Natijalar {star}-{nex} {n} dan\n\n"
                    n = 1

                    for prodact in prodact_data:
                        answer += f"{n}.👤 {prodact['user_name']}"
                        month_index = prodact['ordered_time'].split('.')[1]
                        answer += f"  ⏱ {prodact['ordered_time'].split('.')[0]}-{months[month_index]} {prodact['ordered_time'].split(' ')[-1]}"
                    
                        if prodact.get('order_name'):
                            answer += f"\n📦 Buyurtma nomi:{prodact['order_name']}"

                        answer += "\n\n"
                        n+=1

                    try:
                        await bot.edit_message_text(text = answer, 
                                        chat_id = update.from_user.id,
                                        message_id = update.message.message_id,
                                        reply_markup = inline_buttons.cash_menu_buttons(ids = orders_id, last = int(param)-10, next =  int(param)))
                    except:
                        pass

                else:
                    await update.answer(text = "Siz birnchi sahifadasiz")

            else:
                await update.answer(text = "Siz birnchi sahifadasiz")

        elif command == 'back_cash':
            prodact_data, orders_id = db.get_orders(cash = True, ofset = int(param))
            if len(prodact_data) >= 1:
                n = db.orders_len()
                nex = int(param)+10
                star = int(param)
                # print(nex)
                if star == 0:
                    star = 1
                elif nex > n:
                    nex = n
                answer = f"Natijalar {star}-{nex} {n} dan\n\n"
                n = 1

                for prodact in prodact_data:
                    answer += f"{n}.👤 {prodact['user_name']}"
                    month_index = prodact['ordered_time'].split('.')[1]
                    answer += f"  ⏱ {prodact['ordered_time'].split('.')[0]}-{months[month_index]} {prodact['ordered_time'].split(' ')[-1]}"
                    
                    if prodact.get('order_name'):
                        answer += f"\n📦 Buyurtma nomi:{prodact['order_name']}"

                    answer += "\n\n"
                    n+=1

                try:
                    await bot.edit_message_text(text = answer, 
                                        chat_id = update.from_user.id,
                                        message_id = update.message.message_id,
                                        reply_markup = inline_buttons.cash_menu_buttons(ids = orders_id, last = param, next = nex))
                except:
                    pass
            else:
                await bot.edit_message_text(text = "Boshqa buyurtmalr yo'q", 
                                            chat_id = update.from_user.id, 
                                            message_id = update.message.message_id)
                # await bot.send_message(text = "Boshqa buyurtma yo'q", chat_id = update.from_user.id, reply_markup = menu.admin_menu())
        
        elif command == 'cash':
            param = param.split('&')
            last = param[-1]
            param = param[0]

            order_data = db.get_order(order_id = param)
            if not order_data:
                return None
            month_index = order_data['time'].split('.')[1]

            # print(order_data)
            if order_data['order_name']:
                await bot.edit_message_text(text = f"👤 Buyurtmachi: {ram.users[order_data['user_id']]['name']} \n\n📱 Telefo'n raqam: {ram.users[order_data['user_id']]['number']}  \n\n📦 Buyurtma nomi: {order_data['order_name']}  \n\n⏱ Buyurtma vaxti: {order_data['time'].split('.')[0]}-{months[month_index]} {order_data['time'].split(' ')[-1]}", 
                                        chat_id = update.from_user.id,
                                        message_id = update.message.message_id,
                                        reply_markup = inline_buttons.cash_order_button(offset = last, order_id=order_data['id']))
            else:
                await bot.edit_message_text(text = f"👤 Buyurtmachi: {ram.users[order_data['user_id']]['name']} \n\n📱 Telefo'n raqam: {ram.users[order_data['user_id']]['number']}   \n\n⏱ Buyurtma vaxti:  {order_data['time'].split('.')[0]}-{months[month_index]} {order_data['time'].split(' ')[-1]}", 
                                        chat_id = update.from_user.id,
                                        message_id = update.message.message_id,
                                        reply_markup = inline_buttons.cash_order_button(message_id = order_data['message_id'], offset = last, order_id=order_data['id']))
            

        elif command == 'cdone':
            ofset = param.split('&')[-1]
            order_id = param.split('&')[0]

            order_data = db.get_order(order_id)
            if order_data:
                db.save_arxiv(order_data['id'])

                # return cash menu
                prodact_data, orders_id = db.get_orders(cash = True, ofset = ofset)
                if len(prodact_data) >= 1:
                    n = db.orders_len()
                    nex = int(ofset)+10
                    star = int(ofset)
                    # print(nex)
                    if star == 0:
                        star = 1
                    elif nex > n:
                        nex = n
                    answer = f"Natijalar {star}-{nex} {n} dan\n\n"
                    n = 1

                    for prodact in prodact_data:
                        answer += f"{n}.👤 {prodact['user_name']}"
                        month_index = prodact['ordered_time'].split('.')[1]
                        answer += f"  ⏱ {prodact['ordered_time'].split('.')[0]}-{months[month_index]} {prodact['ordered_time'].split(' ')[-1]}"
                    
                        if prodact.get('order_name'):
                            answer += f"\n📦 Buyurtma nomi:{prodact['order_name']}"

                        answer += "\n\n"
                        n+=1

                    try:
                        await update.answer("✅ Buyurtma bajarildi")
                        await bot.edit_message_text(text = answer, 
                                        chat_id = update.from_user.id,
                                        message_id = update.message.message_id,
                                        reply_markup = inline_buttons.cash_menu_buttons(ids = orders_id, last = ofset))
                    except:
                        pass
                else:
                    await bot.edit_message_text(text = "Boshqa buyurtmalr yo'q", 
                                            chat_id = update.from_user.id, 
                                            message_id = update.message.message_id)
                    # await bot.send_message(text = "Boshqa buyurtma yo'q", chat_id = update.from_user.id, reply_markup = menu.admin_menu())


        elif command == 'loan':
            param = param.split('&')
            last = param[-1]
            param = param[0]

            order_data = db.get_order(order_id = param)
            if not order_data:
                return None
            month_index = order_data['time'].split('.')[1]

            # print(order_data)
            if order_data['order_name']:
                await bot.edit_message_text(text = f"👤 Buyurtmachi: {ram.users[order_data['user_id']]['name']} \n\n📱 Telefo'n raqam: {ram.users[order_data['user_id']]['number']}  \n\n📦 Buyurtma nomi: {order_data['order_name']}  \n\n⏱ Buyurtma vaxti: {order_data['time'].split('.')[0]}-{months[month_index]} {order_data['time'].split(' ')[-1]}", 
                                        chat_id = update.from_user.id,
                                        message_id = update.message.message_id,
                                        reply_markup = inline_buttons.loan_order_button(message_id = order_data['message_id'], offset = last, order_id=order_data['id']))
            else:
                await bot.edit_message_text(text = f"👤 Buyurtmachi: {ram.users[order_data['user_id']]['name']} \n\n📱 Telefo'n raqam: {ram.users[order_data['user_id']]['number']}   \n\n⏱ Buyurtma vaxti:  {order_data['time'].split('.')[0]}-{months[month_index]} {order_data['time'].split(' ')[-1]}", 
                                        chat_id = update.from_user.id,
                                        message_id = update.message.message_id,
                                        reply_markup = inline_buttons.loan_order_button(message_id = order_data['message_id'], offset = last, order_id=order_data['id']))

        elif command == "back_loan":
            prodact_data, orders_id = db.get_orders(loan = True, ofset = int(param))
            if len(prodact_data) >= 1:
                n = db.orders_len(loan = True)
                nex = int(param)+10
                star = int(param)

                # if star == 0:
                #     star = 1
                if nex > n:
                    nex = len(prodact_data)
                answer = f"Natijalar {star}-{len(prodact_data)} {n} dan\n\n"
                n = 1

                for prodact in prodact_data:
                    answer += f"{n}.👤 {prodact['user_name']}"
                    month_index = prodact['ordered_time'].split('.')[1]
                    answer += f"  ⏱ {prodact['ordered_time'].split('.')[0]}-{months[month_index]} {prodact['ordered_time'].split(' ')[-1]}"
                    
                    if prodact.get('order_name'):
                        answer += f"\n📦 Buyurtma nomi:{prodact['order_name']}"

                    answer += "\n\n"
                    n+=1

                try:
                    await bot.edit_message_text(text = answer, 
                                        chat_id = update.from_user.id,
                                        message_id = update.message.message_id,
                                        reply_markup = inline_buttons.loan_menu_buttons(ids = orders_id, last = star, next = nex))
                except:
                    pass
            else:
                await bot.send_message(text = "Boshqa buyurtma yo'q", chat_id = update.from_user.id, reply_markup = menu.admin_menu())
    
        elif command == 'next_loan':
            prodact_data, orders_id = db.get_orders(loan = True, ofset = param)
            if len(prodact_data) >= 1:
                n = db.orders_len()
                nex = int(param)+10
                star = int(param)
                if star == 0:
                    star = 1
                elif nex > n:
                    nex = n
                answer = f"Natijalar {star}-{nex} {n} dan\n\n"
                n = 1
                for prodact in prodact_data:
                    answer += f"{n}.👤 {prodact['user_name']}"
                    month_index = prodact['ordered_time'].split('.')[1]
                    answer += f"  ⏱ {prodact['ordered_time'].split('.')[0]}-{months[month_index]} {prodact['ordered_time'].split(' ')[-1]}"
                    
                    if prodact.get('order_name'):
                        answer += f"\n📦 Buyurtma nomi:{prodact['order_name']}"
                    answer += "\n\n"
                    n+=1
                try:
                    await bot.edit_message_text(text = answer, 
                                        chat_id = update.from_user.id,
                                        message_id = update.message.message_id,
                                        reply_markup = inline_buttons.loan_menu_buttons(ids = orders_id, last = star, next =  nex))
                except:
                    pass

            else:
                await update.answer(text = "Boshqa buyurtmalar yo'q")

        elif command == 'last_loan':
            if int(param) >= 10:
                prodact_data, orders_id = db.get_orders(loan = True, ofset = int(param)-10)
                if len(prodact_data) >= 1:
                    n = db.orders_len()
                    nex = int(param)
                    star = int(param) - 10
                    if star == 0:
                        star = 1
                    elif nex > n:
                        nex = n
                    answer = f"Natijalar {star}-{nex} {n} dan\n\n"
                    n = 1

                    for prodact in prodact_data:
                        answer += f"{n}.👤 {prodact['user_name']}"
                        month_index = prodact['ordered_time'].split('.')[1]
                        answer += f"  ⏱ {prodact['ordered_time'].split('.')[0]}-{months[month_index]} {prodact['ordered_time'].split(' ')[-1]}"
                    
                        if prodact.get('order_name'):
                            answer += f"\n📦 Buyurtma nomi:{prodact['order_name']}"

                        answer += "\n\n"
                        n+=1

                    try:
                        await bot.edit_message_text(text = answer, 
                                        chat_id = update.from_user.id,
                                        message_id = update.message.message_id,
                                        reply_markup = inline_buttons.loan_menu_buttons(ids = orders_id, last = int(param)-10, next =  int(param)))
                    except:
                        pass

                else:
                    await update.answer(text = "Siz birnchi sahifadasiz")

            else:
                await update.answer(text = "Siz birnchi sahifadasiz")

        elif command == 'ldone':
            ofset = param.split('&')[-1]
            order_id = param.split('&')[0]

            order_data = db.get_order(order_id)
            if order_data:
                db.save_arxiv(order_data['id'])

                # return loan menu
                prodact_data, orders_id = db.get_orders(loan = True, ofset = ofset)
                if len(prodact_data) >= 1:
                    n = db.orders_len()
                    nex = int(ofset)+10
                    star = int(ofset)
                    # print(nex)
                    if star == 0:
                        star = 1
                    elif nex > n:
                        nex = n
                    answer = f"Natijalar {star}-{nex} {n} dan\n\n"
                    n = 1

                    for prodact in prodact_data:
                        answer += f"{n}.👤 {prodact['user_name']}"
                        month_index = prodact['ordered_time'].split('.')[1]
                        answer += f"  ⏱ {prodact['ordered_time'].split('.')[0]}-{months[month_index]} {prodact['ordered_time'].split(' ')[-1]}"
                    
                        if prodact.get('order_name'):
                            answer += f"\n📦 Buyurtma nomi:{prodact['order_name']}"

                        answer += "\n\n"
                        n+=1

                    try:
                        await update.answer("✅ Buyurtma bajarildi")
                        await bot.edit_message_text(text = answer, 
                                        chat_id = update.from_user.id,
                                        message_id = update.message.message_id,
                                        reply_markup = inline_buttons.loan_menu_buttons(ids = orders_id, last = ofset))
                    except:
                        pass
                else:
                    await bot.edit_message_text(text = "Boshqa buyurtmalar yo'q", 
                                            chat_id = update.from_user.id, 
                                            message_id = update.message.message_id)
                    # await bot.send_message(text = "Boshqa buyurtma yo'q", chat_id = update.from_user.id, reply_markup = menu.admin_menu())

        elif command == 'next_arxiv':
            prodact_data, orders_id = db.get_arxiv(ofset = param)
            if len(prodact_data) >= 1:
                n = db.arxiv_len()
                nex = int(param)+10
                star = int(param)
                if star == 0:
                    star = 1
                elif nex > n:
                    nex = n
                answer = f"Natijalar {star}-{nex} {n} dan\n\n"
                n = 1
                for prodact in prodact_data:
                    answer += f"{n}.👤 {prodact['user_name']}"
                    month_index = prodact['ordered_time'].split('.')[1]
                    answer += f"  ⏱ {prodact['ordered_time'].split('.')[0]}-{months[month_index]} {prodact['ordered_time'].split(' ')[-1]}"
                    # answer += f"\n💰 To'lo'v turi: {prodact['pay']}"
                    answer += '\n'
                    if prodact.get('order_name'):
                        answer += f"📦 Nomi: {prodact['order_name']}    "
                    

                    answer += f"💰 To'lo'v: {prodact['pay']}\n\n"
                    n+=1
                try:
                    await bot.edit_message_text(text = answer, 
                                        chat_id = update.from_user.id,
                                        message_id = update.message.message_id,
                                        reply_markup = inline_buttons.arxiv_menu_buttons(ids = orders_id, last = star, next =  nex))
                except:
                    pass

            else:
                await update.answer(text = "Boshqa buyurtmalr yo'q")


        elif command == 'last_arxiv':
            if int(param) >= 10:
                prodact_data, orders_id = db.get_arxiv(ofset = int(param)-10)
                if len(prodact_data) >= 1:
                    n = db.arxiv_len()
                    nex = int(param)
                    star = int(param)-10
                    if star == 0:
                        star = 1
                    elif nex > n:
                        nex = n
                    answer = f"Natijalar {star}-{nex} {n} dan\n\n"
                    n = 1
                    for prodact in prodact_data:
                        answer += f"{n}.👤 {prodact['user_name']}"
                        month_index = prodact['ordered_time'].split('.')[1]
                        answer += f"  ⏱ {prodact['ordered_time'].split('.')[0]}-{months[month_index]} {prodact['ordered_time'].split(' ')[-1]}"
                        # answer += f"\n💰 To'lo'v turi: {prodact['pay']}"
                        answer += '\n'
                        if prodact.get('order_name'):
                            answer += f"📦 Nomi: {prodact['order_name']}    "
                    

                        answer += f"💰 To'lo'v: {prodact['pay']}\n\n"
                        n+=1

                    try:
                        await bot.edit_message_text(text = answer, 
                                        chat_id = update.from_user.id,
                                        message_id = update.message.message_id,
                                        reply_markup = inline_buttons.arxiv_menu_buttons(ids = orders_id, last = int(param)-10, next =  int(param)))
                    except:
                        pass

                else:
                    await update.answer(text = "Siz birnchi sahifadasiz")

            else:
                await update.answer(text = "Siz birnchi sahifadasiz")
        
        elif command == 'arxiv':
            param = param.split('&')
            last = param[-1]
            param = param[0]

            order_data = db.get_arxiv_data(order_id = param)
            if not order_data:
                return None
            month_index = order_data['time'].split('.')[1]

            # print(order_data)
            if order_data['order_name']:
                await bot.edit_message_text(text = f"👤 Buyurtmachi: {ram.users[order_data['user_id']]['name']} \n\n📱 Telefo'n raqam: {ram.users[order_data['user_id']]['number']} \n\n💰 Buyurtma turi: {order_data['pay_type']}  \n\n📦 Buyurtma nomi: {order_data['order_name']}  \n\n⏱ Buyurtma vaxti: {order_data['time'].split('.')[0]}-{months[month_index]} {order_data['time'].split(' ')[-1]}", 
                                        chat_id = update.from_user.id,
                                        message_id = update.message.message_id,
                                        reply_markup = inline_buttons.arxiv_order_button(offset = last, order_id=order_data['id']))
            else:
                await bot.edit_message_text(text = f"👤 Buyurtmachi: {ram.users[order_data['user_id']]['name']} \n\n📱 Telefo'n raqam: {ram.users[order_data['user_id']]['number']}  \n\n💰 Buyurtma turi: {order_data['pay_type']}  \n\n⏱ Buyurtma vaxti:  {order_data['time'].split('.')[0]}-{months[month_index]} {order_data['time'].split(' ')[-1]}", 
                                        chat_id = update.from_user.id,
                                        message_id = update.message.message_id,
                                        reply_markup = inline_buttons.arxiv_order_button(message_id = order_data['message_id'], offset = last, order_id=order_data['id']))
                
        elif command == 'back_arxiv':
            prodact_data, orders_id = db.get_arxiv(ofset = int(param))
            if len(prodact_data) >= 1:
                n = db.arxiv_len()
                nex = int(param)+10
                star = int(param)

                if nex > n:
                    nex = n
                answer = f"Natijalar {star}-{nex} {n} dan\n\n"
                n = 1
                for prodact in prodact_data:
                    answer += f"{n}.👤 {prodact['user_name']}"
                    month_index = prodact['ordered_time'].split('.')[1]
                    answer += f"  ⏱ {prodact['ordered_time'].split('.')[0]}-{months[month_index]} {prodact['ordered_time'].split(' ')[-1]}"
                    # answer += f"\n💰 To'lo'v turi: {prodact['pay']}"
                    answer += '\n'
                    if prodact.get('order_name'):
                        answer += f"📦 Nomi: {prodact['order_name']}    "
                    

                    answer += f"💰 To'lo'v: {prodact['pay']}\n\n"
                    n+=1

                try:
                    await bot.edit_message_text(text = answer,
                                        chat_id = update.from_user.id,
                                        message_id = update.message.message_id,
                                        reply_markup = inline_buttons.arxiv_menu_buttons(ids = orders_id, last = star, next = nex))
                except:
                    pass
            else:
                await bot.edit_message_text(text = "Boshqa buyurtmalr yo'q", 
                                            chat_id = update.from_user.id, 
                                            message_id = update.message.message_id)
                # await bot.send_message(text = "Boshqa buyurtma yo'q", chat_id = update.from_user.id, reply_markup = menu.admin_menu())

        elif command == "rearxiv":
            order_id = param.split('&')[0]
            param = param.split('&')[-1]

            # mov arxiv to orders:
            arxiv_data = db.get_arxiv_data(order_id = order_id)
            if arxiv_data:
                db.save_arxiv_to_orders(arxiv_data['id'])
                # print(arxiv_data)
                if arxiv_data["pay_type"] == 'naxt':
                    await update.answer("💰 Naxt buyurtmalr menyusiga ko'chirldi")
                else:
                    await update.answer("💸 Nasiya buyurtmalr menyusiga ko'chirldi")

                prodact_data, orders_id = db.get_arxiv(ofset = int(param))
                if len(prodact_data) >= 1:
                    n = db.arxiv_len()
                    nex = int(param)+10
                    star = int(param)

                    if star == 0:
                        star = 1
                    elif nex > n:
                        nex = n
                    answer = f"Natijalar {star}-{nex} {n} dan\n\n"
                    n = 1
                    for prodact in prodact_data:
                        answer += f"{n}.👤 {prodact['user_name']}"
                        month_index = prodact['ordered_time'].split('.')[1]
                        answer += f"  ⏱ {prodact['ordered_time'].split('.')[0]}-{months[month_index]} {prodact['ordered_time'].split(' ')[-1]}"
                        # answer += f"\n💰 To'lo'v turi: {prodact['pay']}"
                        answer += '\n'
                        if prodact.get('order_name'):
                            answer += f"📦 Nomi: {prodact['order_name']}    "
                    

                        answer += f"💰 To'lo'v: {prodact['pay']}\n\n"
                        n+=1

                    try:
                        await bot.edit_message_text(text = answer,
                                        chat_id = update.from_user.id,
                                        message_id = update.message.message_id,
                                        reply_markup = inline_buttons.arxiv_menu_buttons(ids = orders_id, last = star, next = nex))
                    except:
                        pass
                else:
                    await bot.edit_message_text(text = "Boshqa buyurtmalr yo'q", 
                                            chat_id = update.from_user.id, 
                                            message_id = update.message.message_id)
                    # await bot.send_message(text = "Boshqa buyurtma yo'q", chat_id = update.from_user.id, reply_markup = menu.admin_menu())

        elif command == 'delet_arxiv':
            order_id = param.split('&')[0]
            ofset = param.split('&')[-1]
            
            try:
                text = update.message.text.replace('\n\n', '\n')
                await bot.edit_message_text(chat_id = update.from_user.id,
                                        message_id = update.message.message_id,
                                        text = f"❗️ Buyurtmani o'chrmoqchimisiz?  \n\n{text}",
                                        reply_markup = inline_buttons.sure_delet_arxiv(offset = ofset, arxiv_id = order_id))
            except:
                pass
        
        
        elif command == 'delet_sarxiv':
            order_id = param.split('&')[0]
            param = param.split('&')[-1]

            # print(order_id)
            db.delet_arxiv_order(order_id)
            await update.answer("🗑 Buyurtma o'chrib tashlandi")

            prodact_data, orders_id = db.get_arxiv(ofset = int(param))
            if len(prodact_data) >= 1:
                n = db.arxiv_len()
                nex = int(param)+10
                star = int(param)

                if nex > n:
                    nex = n
                answer = f"Natijalar {star}-{nex} {n} dan\n\n"
                n = 1
                for prodact in prodact_data:
                    answer += f"{n}.👤 {prodact['user_name']}"
                    month_index = prodact['ordered_time'].split('.')[1]
                    answer += f"  ⏱ {prodact['ordered_time'].split('.')[0]}-{months[month_index]} {prodact['ordered_time'].split(' ')[-1]}"
                    # answer += f"\n💰 To'lo'v turi: {prodact['pay']}"
                    answer += '\n'
                    if prodact.get('order_name'):
                        answer += f"📦 Nomi: {prodact['order_name']}    "
                    

                    answer += f"💰 To'lo'v: {prodact['pay']}\n\n"
                    n+=1

                try:
                    await bot.edit_message_text(text = answer,
                                        chat_id = update.from_user.id,
                                        message_id = update.message.message_id,
                                        reply_markup = inline_buttons.arxiv_menu_buttons(ids = orders_id, last = star, next = nex))
                except:
                    pass
            else:
                await bot.edit_message_text(text = "Boshqa buyurtmalr yo'q", 
                                            chat_id = update.from_user.id, 
                                            message_id = update.message.message_id)
                # await bot.send_message(text = "Boshqa buyurtma yo'q", chat_id = update.from_user.id, reply_markup = menu.admin_menu())




            

