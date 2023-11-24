from loader import dp, ram, update_user_data, types, menu
from aiogram.dispatcher import FSMContext
import re

@dp.message_handler(state = update_user_data.want_to_update)
async def want_to_update(message : types.Message, state : FSMContext):
    if message.text == "✅ Xa":
        await state.set_state(update_user_data.get_name)
        await message.answer("Ilimos ismingzni kiriting", reply_markup = types.ReplyKeyboardRemove())

    elif message.text == "❌ Yo'q":
        await state.finish()
        await message.answer("Bosh menu", reply_markup = menu.user_menu())

    else:
        await message.answer("Iltimos tugmalardan birni bosing", reply_markup = menu.yes_or_no())

@dp.message_handler(state = update_user_data.get_name)
async def update_user_name(message: types.Message, state : FSMContext):
    await state.set_state(update_user_data.get_number)
    ram.update_name(id = message.from_user.id, name = message.text)
    await message.answer(f"{message.text} endi telfo'n raqamingzni kiritng yoki telfo'n raqamni ulashish tugmasni bosing", reply_markup = menu.phone_number())




pattern = re.compile(r'^(|\+?998)\s?\d{2}\s?\d{3}\s?\d{2}\s?\d{2}$')
@dp.message_handler(state = update_user_data.get_number)
async def getupdatenumber(message : types.Message, state : FSMContext):
    if message.text == "⬅️ Orqaga":
        await state.set_state(update_user_data.get_name)
        await message.answer("Ilimos ismingini qaytadan kiriting", reply_markup = types.ReplyKeyboardRemove())
    
    elif pattern.match(message.text):
        ram.update_number(id = message.from_user.id, number = message.text)
        data = ram.users[message.from_user.id]

        await message.answer(f"✅ Telefo'n raqam to'g'ri, \n🤔 Iltimos malumotlaringiz to'gri kiritganigizga ishonch xosil qiling\n👤 ism: {data['name']}  \n📱 Telefo'n raqam: {data['number']}",
                             reply_markup = menu.sure_registr_info(update=True))
        
        await state.set_state(update_user_data.have_finished)

    else:
        await message.answer("Telfo'n raqami xato, iltimos kiritgan raqamingzni tekshrib ko'ring (Faqat o'zbekiston raqamni kiritng)")
        
    
@dp.message_handler(content_types = types.ContentType.CONTACT, state = update_user_data.get_number)
async def contact_handler_when_update(message : types.Message, state : FSMContext):
    number = message.contact.phone_number

    ram.update_number(id = message.from_user.id, number = number)
    data = ram.users[message.from_user.id]

    await message.answer(f"✅ Telefo'n raqam to'g'ri, \n🤔 Iltimos malumotlaringiz to'gri kiritganigizga ishonch xosil qiling\n👤 isim: {data['name']}\n📱 Telefo'n raqam:{data['number']}",
                             reply_markup = menu.sure_registr_info(update=True))
    
    await state.set_state(update_user_data.have_finished)



@dp.message_handler(state = update_user_data.have_finished)
async def sure_about_info(message : types.Message, state : FSMContext):
    if message.text == "✅ To'g'ri":
        await message.answer("Malumotlaringiz muvaffaqiyatli yangliandi", reply_markup = menu.user_menu())
        await state.finish()
    
    elif message.text == "⬅️ Orqaga":
        await message.answer(f"Iltimos telefo'n raqamingizni qaytadan kiriting yoki kontakni ulashish tugmasni bosing", reply_markup = menu.phone_number())
        await state.set_state(update_user_data.get_number)

    else:
        await message.answer("Iltimos quydagi tugmalrdan birni bosing", reply_markup = menu.sure_registr_info(update = True))
