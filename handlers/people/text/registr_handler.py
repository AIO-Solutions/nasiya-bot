from loader import dp, ram, types, menu, registir_state, bot, setting, order_state
from aiogram.dispatcher import FSMContext
import re


@dp.message_handler(state = registir_state.get_name)
async def getname(message : types.Message, state : FSMContext):
    ram.registr_data(message.from_user.id, name = message.text)
    await message.answer(f"{message.text} iltimos telefo'n raqamingizni kiriting yoki kontakni ulashish tugmasni bosing", reply_markup = menu.phone_number())
    await state.set_state(registir_state.get_number)


pattern = re.compile(r'^(|\+?998)\s?\d{2}\s?\d{3}\s?\d{2}\s?\d{2}$')
@dp.message_handler(state = registir_state.get_number)
async def getnumber(message : types.Message, state : FSMContext):
    if message.text == "⬅️ Orqaga":
        await state.set_state(registir_state.get_name)
        await message.answer("Ilimos ismingini qaytadan kiriting", reply_markup = types.ReplyKeyboardRemove())
    
    elif pattern.match(message.text):
        ram.registr_data(id = message.from_user.id, number = message.text)
        data = ram.registr_data(id = message.from_user.id, get_data = True)

        await message.answer(f"✅ Telefo'n raqam to'g'ri, \n🤔 Iltimos malumotlaringiz to'gri kiritganigizga ishonch xosil qiling\n👤 isim: {data['name']}\n📱 Telefo'n raqam:{data['number']}",
                             reply_markup = menu.sure_registr_info())
        
        await state.set_state(registir_state.sure_abaut_info)

    else:
        await message.answer("Telfo'n raqami xato, iltimos kiritgan raqamingzni tekshrib ko'ring (Faqat o'zbekiston raqamni kiritng)")
        
    
@dp.message_handler(content_types = types.ContentType.CONTACT, state = registir_state.get_number)
async def contact_handler(message : types.Message, state : FSMContext):
    number = message.contact.phone_number

    ram.registr_data(id = message.from_user.id, number = number)
    data = ram.registr_data(id = message.from_user.id, get_data = True)

    await message.answer(f"✅ Telefo'n raqam to'g'ri, \n🤔 Iltimos malumotlaringiz to'gri kiritganigizga ishonch xosil qiling\n👤 ism: {data['name']}\n📱 Telefo'n raqam:{data['number']}",
                             reply_markup = menu.sure_registr_info())
    
    await state.set_state(registir_state.sure_abaut_info)


@dp.message_handler(state = registir_state.sure_abaut_info)
async def sure_about_info(message : types.Message, state : FSMContext):
    if message.text == "✅ To'g'ri":
        await message.answer("Siz muvaffaqiyatli ro'yxatdan o'tdingiz", reply_markup = menu.user_menu())
        # data = ram.registr_data(id = message.from_user.id, get_data = True)
        ram.registir_user(id = message.from_user.id)
        ram.users[message.from_user.id]['where'] = 'head_menu'

        order = ram.registdata[message.from_user.id].get('order')
        if order:
            # ram.save_order(id  = message.from_user.id, order_id = order)
            await message.answer(f"Order id : {order}")
            try:
                    await bot.copy_message(chat_id = message.from_user.id, from_chat_id = setting.data['main_chanel_id'], message_id = order)
                    
                    await message.answer("Qanaqa usulda to'lo'v qilmoqchisiz?", reply_markup = menu.chose_pay_type(by_id=True))
                    await state.set_state(order_state.buy_type_byid)
                    ram.save_order(id = message.from_user.id, order_id = order)
                    

            except:
                await state.finish()
                await message.answer("Mahsulot topilmadi", reply_markup = menu.user_menu())

        else:
            await state.finish()

    elif message.text == "🔄 Qaytadan kiritish":
        await state.set_state(registir_state.get_name)
        await message.answer("Ilimos ismingini qaytadan kiriting", reply_markup = types.ReplyKeyboardRemove())
    
    elif message.text == "⬅️ Orqaga":
        await message.answer(f"Iltimos telefo'n raqamingizni qaytadan kiriting yoki kontakni ulashish tugmasni bosing", reply_markup = menu.phone_number())
        await state.set_state(registir_state.get_number)

    else:
        await message.answer("Iltimos quydagi tugmalrdan birni bosing", reply_markup = menu.sure_registr_info())