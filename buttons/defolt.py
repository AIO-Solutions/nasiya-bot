from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, WebAppInfo

class Defolt:
    def __init__(self):
        pass

    def phone_number(self):
        return ReplyKeyboardMarkup(keyboard = [[KeyboardButton("📱 Kontaktni ulashish", request_contact = True)],
                                               [KeyboardButton("⬅️ Orqaga")]], resize_keyboard = True)

    def sure_registr_info(self, byid = False, update = False):
        if update:
            return ReplyKeyboardMarkup(keyboard = [[KeyboardButton(text = "✅ To'g'ri"), KeyboardButton(text = "⬅️ Orqaga")]], resize_keyboard = True)
        
        elif byid:
            return ReplyKeyboardMarkup(keyboard = [[KeyboardButton(text = "✅ To'g'ri")],
                                               [KeyboardButton(text = "⬅️ Orqaga")]], resize_keyboard = True)
        
        return ReplyKeyboardMarkup(keyboard = [[KeyboardButton(text = "✅ To'g'ri"), KeyboardButton(text = "🔄 Qaytadan kiritish")],
                                               [KeyboardButton(text = "⬅️ Orqaga")]], resize_keyboard = True)
    
    def user_menu(slef):
        return ReplyKeyboardMarkup(keyboard = [[KeyboardButton(text = "🛒 Buyurtma berish")],
                                               [KeyboardButton(text = "❓ Savollar", web_app = WebAppInfo(url = "https://telegra.ph/Kop-Soraladigan-Savollar-11-24")), KeyboardButton(text = "ℹ️ Biz haqimzda")],
                                               [KeyboardButton(text = "⚙️ Malumotlarni o'zgartirish")]], 
                                               resize_keyboard = True)

    def back(self):
        return ReplyKeyboardMarkup(resize_keyboard = True,
                                   keyboard = [[KeyboardButton(text = "⬅️ Orqaga")]])
    
    def chose_pay_type(self, by_id = False):
        if by_id:
            return ReplyKeyboardMarkup(resize_keyboard = True,
                                   keyboard = [[KeyboardButton(text = "💰 Naxt"), KeyboardButton(text = "💸 Nasiya")],
                                               [KeyboardButton(text = "🎛 Bosh menu")]])
        
        return ReplyKeyboardMarkup(resize_keyboard = True,
                                   keyboard = [[KeyboardButton(text = "💰 Naxt"), KeyboardButton(text = "💸 Nasiya")],
                                               [KeyboardButton(text = "⬅️ Orqaga"), KeyboardButton(text = "🎛 Bosh menu")]])
    
    
    def yes_or_no(self):
        return ReplyKeyboardMarkup(resize_keyboard = True, keyboard = [[KeyboardButton(text = "✅ Xa"), KeyboardButton(text = "❌ Yo'q")]])
    
    def admin_menu(self):
        return ReplyKeyboardMarkup(resize_keyboard = True,
                                   keyboard = [
                                       [KeyboardButton(text = "📦 Buyurmalar Tarixi")],
                                       [KeyboardButton(text = "💰 Naxtga"), KeyboardButton(text = "💸 Nasiyaga")],
                                       [KeyboardButton(text = "❓ Savollar"), KeyboardButton(text = "⚙️ Sozlamalar")]
                                   ])

    def live_admin_panel(self):
        return ReplyKeyboardMarkup(resize_keyboard=True, 
                                   keyboard = 
                                   [
                                       [KeyboardButton(text = "🚶 Chqish"), KeyboardButton(text = "⬅️ Orqaga")]
                                    ])

    def settings(self): 
        return ReplyKeyboardMarkup(resize_keyboard=True, 
                                  keyboard=[ 
                                      [KeyboardButton(text="🔐 Parolni o'zgartish"), KeyboardButton(text="📡 Asosiy kanal ➕")], 
                                      [KeyboardButton(text="🤖 Bot profil info"), KeyboardButton(text="ℹ️ Biz haqimzda")], 
                                      [KeyboardButton(text='⬅️ Orqaga')] 
                                  ] )
    def question_edit(self):
        return ReplyKeyboardMarkup(resize_keyboard = True,
                                   keyboard = [
                                       [KeyboardButton(text = "❓ Savollarni ko'rish",  web_app = WebAppInfo(url = "https://telegra.ph/Kop-Soraladigan-Savollar-11-24"))],
                                       [KeyboardButton(text = "➕ Qo'shish"), KeyboardButton(text = "➖ Olib tashlash")],
                                       [KeyboardButton(text='⬅️ Orqaga')] 
                                       ])
    
    def back_or_cansle(self, sure = False):
        if sure:
            return ReplyKeyboardMarkup(resize_keyboard=True,
                                   keyboard = 
                                   [
                                       [KeyboardButton(text="✅ To'g'ri")],
                                       [KeyboardButton(text='⬅️ Orqaga'), KeyboardButton(text = "❌ Bekor qlish")]
                                   ])

        return ReplyKeyboardMarkup(resize_keyboard=True,
                                   keyboard = 
                                   [
                                       [KeyboardButton(text='⬅️ Orqaga'), KeyboardButton(text = "❌ Bekor qlish")]
                                   ])