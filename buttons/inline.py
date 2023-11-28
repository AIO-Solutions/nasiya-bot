from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton



class InlineButtons:
    def __init__(self):
        pass

    def go_main_chanel(self, url : str):
        return InlineKeyboardMarkup(inline_keyboard = [[InlineKeyboardButton(text = "🛍 Kanalga o'tish", url = url)]])
    
    def cash_menu_buttons(self, ids : list = None, last = 0, next = 10):
        n = len(ids)
        if n <= 5:
            keyboards = [[InlineKeyboardButton(text = f"{index+1}", callback_data = f"{ids[index]}&{last}") for index in range(n)]]
        
        elif n <= 7:
            keyboards = [[InlineKeyboardButton(text = f"{index+1}", callback_data = f"cash={ids[index]}&{last}") for index in range(4)],
                         [InlineKeyboardButton(text = f"{index+1}", callback_data = f"cash={ids[index]}&{last}") for index in range(4, n)]]

        else:
            keyboards = [[InlineKeyboardButton(text = f"{index+1}", callback_data = f"cash={ids[index]}&{last}") for index in range(5)],
                         [InlineKeyboardButton(text = f"{index+1}", callback_data = f"cash={ids[index]}&{last}") for index in range(5, n)]]
            
        

        keyboards.append([InlineKeyboardButton(text = "⬅️", callback_data = f'last_cash={last}'), InlineKeyboardButton(text = "❌", callback_data = 'delet'),
                          InlineKeyboardButton(text = "➡️", callback_data = f'next_cash={next}')])
        return InlineKeyboardMarkup(inline_keyboard = keyboards)

    def cash_order_button(self, message_id : int = None, offset : int = 0, order_id = None):
        if message_id:
            keyboards = [[InlineKeyboardButton(text = "⬅️ Orqaga", callback_data = f"back_cash={offset}"), InlineKeyboardButton(text = "✅ Bajarldi", callback_data = f"done={order_id}")],
                         [InlineKeyboardButton(text = "📦 Buyurtmani ko'rish", callback_data = f"see", url = f"https://t.me/blahblat/{message_id}")]]
        
        else:
            keyboards = [[InlineKeyboardButton(text = "⬅️ Orqaga", callback_data = f"back_cash={offset}"), InlineKeyboardButton(text = "✅ Bajarldi", callback_data = f"done={order_id}")]]
        
        return InlineKeyboardMarkup(inline_keyboard = keyboards)