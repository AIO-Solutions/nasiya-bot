from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton



class InlineButtons:
    def __init__(self):
        pass

    def go_main_chanel(self, url : str):
        return InlineKeyboardMarkup(inline_keyboard = [[InlineKeyboardButton(text = "🛍 Kanalga o'tish", url = url)]])
        