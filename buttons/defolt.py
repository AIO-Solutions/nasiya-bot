from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


class Defolt:
    def __init__(self):
        pass

    def phone_number(self):
        return ReplyKeyboardMarkup(keyboard = [[KeyboardButton("📱 Kontaktni ulashish", request_contact = True)],
                                               [KeyboardButton("⬅️ Orqaga")]], resize_keyboard = True)

    def sure_registr_info(sekf):
        return ReplyKeyboardMarkup(keyboard = [[KeyboardButton(text = "✅ To'g'ri"), KeyboardButton(text = "🔄 Qaytadan kiritish")]], resize_keyboard = True)