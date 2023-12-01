from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton



class InlineButtons:
    def __init__(self, main_chanel : str = None):
        self.main_chanel = main_chanel

    def go_main_chanel(self, url : str):
        return InlineKeyboardMarkup(inline_keyboard = [[InlineKeyboardButton(text = "🛍 Kanalga o'tish", url = url)]])
    
    def cash_menu_buttons(self, ids : list = None, last = 0, next = 10):
        n = len(ids)
        if n <= 5:
            keyboards = [[InlineKeyboardButton(text = f"{index+1}", callback_data = f"cash={ids[index]}&{last}") for index in range(n)]]
        
        elif n <= 7:
            keyboards = [[InlineKeyboardButton(text = f"{index+1}", callback_data = f"cash={ids[index]}&{last}") for index in range(4)],
                         [InlineKeyboardButton(text = f"{index+1}", callback_data = f"cash={ids[index]}&{last}") for index in range(4, n)]]

        else:
            keyboards = [[InlineKeyboardButton(text = f"{index+1}", callback_data = f"cash={ids[index]}&{last}") for index in range(5)],
                         [InlineKeyboardButton(text = f"{index+1}", callback_data = f"cash={ids[index]}&{last}") for index in range(5, n)]]
            
        

        keyboards.append([InlineKeyboardButton(text = "⬅️", callback_data = f'last_cash={last}'), InlineKeyboardButton(text = "❌", callback_data = 'delet'),
                          InlineKeyboardButton(text = "➡️", callback_data = f'next_cash={next}')])
        return InlineKeyboardMarkup(inline_keyboard = keyboards)
    
    def loan_menu_buttons(self, ids : list = None, last = 0, next = 10):
        n = len(ids)
        if n <= 5:
            keyboards = [[InlineKeyboardButton(text = f"{index+1}", callback_data = f"loan={ids[index]}&{last}") for index in range(n)]]
        
        elif n <= 7:
            keyboards = [[InlineKeyboardButton(text = f"{index+1}", callback_data = f"loan={ids[index]}&{last}") for index in range(4)],
                         [InlineKeyboardButton(text = f"{index+1}", callback_data = f"loan={ids[index]}&{last}") for index in range(4, n)]]

        else:
            keyboards = [[InlineKeyboardButton(text = f"{index+1}", callback_data = f"loan={ids[index]}&{last}") for index in range(5)],
                         [InlineKeyboardButton(text = f"{index+1}", callback_data = f"loan={ids[index]}&{last}") for index in range(5, n)]]
            
        

        keyboards.append([InlineKeyboardButton(text = "⬅️", callback_data = f'last_loan={last}'), InlineKeyboardButton(text = "❌", callback_data = 'delet'),
                          InlineKeyboardButton(text = "➡️", callback_data = f'next_loan={next}')])
        return InlineKeyboardMarkup(inline_keyboard = keyboards)

    def cash_order_button(self, message_id : int = None, offset : int = 0, order_id = None):
        if message_id:
            keyboards = [[InlineKeyboardButton(text = "⬅️ Orqaga", callback_data = f"back_cash={offset}"), InlineKeyboardButton(text = "✅ Bajarldi", callback_data = f"cdone={order_id}&{offset}")],
                         [InlineKeyboardButton(text = "📦 Buyurtmani ko'rish", callback_data = f"see", url = f"{self.main_chanel}/{message_id}")]]
        
        else:
            keyboards = [[InlineKeyboardButton(text = "⬅️ Orqaga", callback_data = f"back_cash={offset}"), InlineKeyboardButton(text = "✅ Bajarldi", callback_data = f"cdone={order_id}&{offset}")]]
        
        return InlineKeyboardMarkup(inline_keyboard = keyboards)
    
    def loan_order_button(self, message_id : int = None, offset : int = 0, order_id = None):
        if message_id:
            keyboards = [[InlineKeyboardButton(text = "⬅️ Orqaga", callback_data = f"back_loan={offset}"), InlineKeyboardButton(text = "✅ Bajarldi", callback_data = f"ldone={order_id}&{offset}")],
                         [InlineKeyboardButton(text = "📦 Buyurtmani ko'rish", callback_data = f"see", url = f"{self.main_chanel}/{message_id}")]]
        
        else:
            keyboards = [[InlineKeyboardButton(text = "⬅️ Orqaga", callback_data = f"back_loan={offset}"), InlineKeyboardButton(text = "✅ Bajarldi", callback_data = f"ldone={order_id}&{offset}")]]
        
        return InlineKeyboardMarkup(inline_keyboard = keyboards)
    
    def arxiv_menu_buttons(self, ids : list = None, last = 0, next = 10):
        n = len(ids)
        if n <= 5:
            keyboards = [[InlineKeyboardButton(text = f"{index+1}", callback_data = f"arxiv={ids[index]}&{last}") for index in range(n)]]
        
        elif n <= 7:
            keyboards = [[InlineKeyboardButton(text = f"{index+1}", callback_data = f"arxiv={ids[index]}&{last}") for index in range(4)],
                         [InlineKeyboardButton(text = f"{index+1}", callback_data = f"arxiv={ids[index]}&{last}") for index in range(4, n)]]

        else:
            keyboards = [[InlineKeyboardButton(text = f"{index+1}", callback_data = f"arxiv={ids[index]}&{last}") for index in range(5)],
                         [InlineKeyboardButton(text = f"{index+1}", callback_data = f"arxiv={ids[index]}&{last}") for index in range(5, n)]]
            
        

        keyboards.append([InlineKeyboardButton(text = "⬅️", callback_data = f'last_arxiv={last}'), InlineKeyboardButton(text = "❌", callback_data = 'delet'),
                          InlineKeyboardButton(text = "➡️", callback_data = f'next_arxiv={next}')])
        return InlineKeyboardMarkup(inline_keyboard = keyboards)
    
    def arxiv_order_button(self, message_id : int = None, offset : int = 0, order_id = None):
        if message_id:
            keyboards = [[InlineKeyboardButton(text = "⬅️ Orqaga", callback_data = f"back_arxiv={offset}"), InlineKeyboardButton(text = "🔄 Bajarilmadi", callback_data = f"rearxiv={order_id}&{offset}")],
                         [InlineKeyboardButton(text = "🗑 O'chrish", callback_data = f'delet_arxiv={order_id}&{offset}')],
                         [InlineKeyboardButton(text = "📦 Buyurtmani ko'rish", callback_data = f"see", url = f"{self.main_chanel}/{message_id}")]]
        
        else:
             keyboards = [[InlineKeyboardButton(text = "⬅️ Orqaga", callback_data = f"back_arxiv={offset}"), InlineKeyboardButton(text = "🔄 Bajarilmadi", callback_data = f"rearxiv={order_id}&{offset}")],
                         [InlineKeyboardButton(text = "🗑 O'chrish", callback_data = f'delet_arxiv={order_id}&{offset}')]]
        
        return InlineKeyboardMarkup(inline_keyboard = keyboards)
    
    def sure_delet_arxiv(self, offset = 0, arxiv_id = None):
        return InlineKeyboardMarkup(inline_keyboard = 
                                    [
                                        [InlineKeyboardButton(text = "✅ Xa", callback_data = f"delet_sarxiv={arxiv_id}&{offset}"), InlineKeyboardButton(text = "❌ Yo'q", callback_data = f"arxiv={arxiv_id}&{offset}")]
                                    ])
    
    def see_order(self, message_id):
        return InlineKeyboardMarkup(inline_keyboard = [[InlineKeyboardButton(text = "📦 Buyurtmani ko'rish", callback_data = f"see", url = f"{self.main_chanel}/{message_id}")]])
    