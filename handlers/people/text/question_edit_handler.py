from loader import setting, dp, db, ram, admin_panel_states, types, menu, postman
from aiogram.dispatcher import FSMContext


@dp.message_handler(state = admin_panel_states.change_questions)
async def change_question_handler(update : types.Message, state : FSMContext):
    if update.text == '⬅️ Orqaga':
        await state.finish()
        await update.answer("Bosh menu", reply_markup = menu.admin_menu())
    
    elif update.text == "➕ Qo'shish":
        await state.set_state(admin_panel_states.get_question)
        await update.answer("Iltimos yangi savolni kriting", reply_markup = menu.back())
        

    elif update.text == "➖ Olib tashlash":
        await state.set_state(admin_panel_states.remove_question)
        await update.answer("Olib tashlamoqchi bo'lgan savolingzni raqamni kriting", reply_markup=menu.back())

    else:
        await update.answer("Quydagi tugmalrdan brni bosing")
    # setting.data['questions'] = {'Nasiyaga savdo qilasizmi?' : 'Xa qilamiz', 'Kreditga savdo qilasizmi?' : 'Afsuskiy yo\'q'}
    # setting.update()

    # postman.upload(setting.data['questions'])



@dp.message_handler(state = admin_panel_states.get_question)
async def add_question_handler(update : types.Message, state : FSMContext):
    if update.text == '⬅️ Orqaga':
        await state.set_state(admin_panel_states.change_questions)
        await update.answer("Savollar menusi", reply_markup = menu.question_edit())

    else:
        ram.admins[update.from_user.id]['question'] = update.text
        await state.set_state(admin_panel_states.get_answer)
        await update.reply("Endi savolga javob yozing", reply_markup = menu.back_or_cansle())






@dp.message_handler(state = admin_panel_states.get_answer)
async def get_answer_handler(update : types.Message, state : FSMContext):
    if update.text == '⬅️ Orqaga':
        await state.set_state(admin_panel_states.get_question)
        await update.answer("Savolni qaytadan kriting", reply_markup = menu.back())

    elif update.text == "❌ Bekor qlish":
        await state.set_state(admin_panel_states.change_questions)
        await update.answer("Savollar menusi", reply_markup = menu.question_edit())
    

    else:
        #"✅ To'g'ri"
        ram.admins[update.from_user.id]['answer'] = update.text
        await state.set_state(admin_panel_states.question_add_sure)
        await update.answer(f"Yangi savol javob to'g'rililga ishonch xosil qiling  \n❓Savol: {ram.admins[update.from_user.id]['question']}  \n❗️Javob: {ram.admins[update.from_user.id]['answer']}", 
                            reply_markup = menu.back_or_cansle(sure=True))


@dp.message_handler(state=admin_panel_states.question_add_sure)
async def question_add_sure(update : types.Message, state : FSMContext):
    if update.text == '⬅️ Orqaga':
        await state.set_state(admin_panel_states.get_answer)
        await update.answer("Javobni qaytadan kriting", reply_markup = menu.back())
    
    elif update.text == "❌ Bekor qlish":
        await state.set_state(admin_panel_states.change_questions)
        await update.answer("Savollar menusi", reply_markup = menu.question_edit())

    elif update.text == "✅ To'g'ri":
        question = ram.admins[update.from_user.id]['question']
        answer = ram.admins[update.from_user.id]['answer']
        setting.data["questions"][question] =answer
        setting.update()
        postman.upload(setting.data['questions'])

        await state.set_state(admin_panel_states.change_questions)
        await update.reply("Savol muvaffaqiyatli qo'shildi", reply_markup = menu.question_edit())
    
    else:
        await update.answer("Quydagi tugmalrdan brni bosing", reply_markup = menu.back_or_cansle(sure=True))




@dp.message_handler(state = admin_panel_states.remove_question)
async def remove_question(update : types.Message, state : FSMContext):
    if update.text == '⬅️ Orqaga':
        await state.set_state(admin_panel_states.change_questions)
        await update.answer("Savollar menusi", reply_markup = menu.question_edit())
    
    elif update.text.isnumeric():
        number = int(update.text)
        n = 0
        for question in setting.data['questions'].keys():
            n+=1
            if n == number:
                del setting.data['questions'][question]
                setting.update()
                postman.upload(setting.data['questions'])

                
                await state.set_state(admin_panel_states.change_questions)
                await update.reply("Savol muvaffaqiyatli o'chrib tashlandi", reply_markup = menu.question_edit())
                return
        
        await update.reply("Savol tartib raqami mavjud emas", reply_markup = menu.back())
            

    else:
        await update.reply("Iltimos faqat raqam kriting", reply = menu.back())