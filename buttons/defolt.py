from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, WebAppInfo

class Defolt:
    def __init__(self):
        pass

    def phone_number(self):
        return ReplyKeyboardMarkup(keyboard = [[KeyboardButton("📱 Kontaktni ulashish", request_contact = True)],
                                               [KeyboardButton("⬅️ Orqaga")]], resize_keyboard = True)

    def sure_registr_info(self):
        return ReplyKeyboardMarkup(keyboard = [[KeyboardButton(text = "✅ To'g'ri"), KeyboardButton(text = "🔄 Qaytadan kiritish")]], resize_keyboard = True)
    
    def user_menu(slef):
        return ReplyKeyboardMarkup(keyboard = [[KeyboardButton(text = "🛒 Buyurtma berish")],
                                               [KeyboardButton(text = "❓ Savollar", web_app = WebAppInfo(url = "https://telegra.ph/Savollar-11-23")), KeyboardButton(text = "ℹ️ Biz haqimzda")],
                                               [KeyboardButton(text = "⚙️ Malumotlarni o'zgartirish")]], 
                                               resize_keyboard = True)

    def back(self):
        return ReplyKeyboardMarkup(resize_keyboard = True,
                                   keyboard = [[KeyboardButton(text = "⬅️ Orqaga")]])
    
    def chose_pay_type(self):
        return ReplyKeyboardMarkup(resize_keyboard = True,
                                   keyboard = [[KeyboardButton(text = "💰 Naxt"), KeyboardButton(text = "💸 Nasiya")],
                                               [KeyboardButton(text = "⬅️ Orqaga"), KeyboardButton(text = "🎛 Bosh menu")]])