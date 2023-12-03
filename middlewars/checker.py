import logging
from aiogram import types, Bot
from aiogram.dispatcher.handler import CancelHandler
from aiogram.dispatcher.middlewares import BaseMiddleware
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from loader import setting, bot, ram


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


class Bro(BaseMiddleware):
    async def on_pre_process_update(self, update : types.Update,  data: dict):
        if update.message:
            id = update.message.from_user.id
        
            # print(status)
            if not await check_sub(user_id=id, chanel=setting.data['main_chanel_id']):
                keyboard = InlineKeyboardMarkup(inline_keyboard=[
                    [InlineKeyboardButton(text="🛍 Azo bo'lish", callback_data='chanel', url=setting.data['main_chanel'])],
                    [InlineKeyboardButton(text = "♻️ Tekshirish", callback_data = 'check')]
                ])
                await update.message.answer("Iltimos bizning Grand Nasiya kanlimizga obuna bo'ling", reply_markup=keyboard)
                raise CancelHandler()

        elif update.callback_query:
            # print(update.callback_query.data)
            id = update.callback_query.from_user.id
            keyboard = InlineKeyboardMarkup(inline_keyboard=[
                    [InlineKeyboardButton(text="🛍 Azo bo'lish", callback_data='chanel', url=setting.data['main_chanel'])],
                    [InlineKeyboardButton(text = "♻️ Tekshirish", callback_data = 'check')]])
            
            if update.callback_query.data == 'check':
                if await check_sub(user_id = id, chanel = setting.data['main_chanel_id']):
                    buttons = types.ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[[types.KeyboardButton(text = "/restart")]])
                    # if ram.is_user(update.callback_query.from_user.id):
                    #     pass
                    # elif ram.is_admin(update.callback_query.from_user.id):
                    #     pass
                    # else:
                    await update.callback_query.answer("✅ Obuna bo'lgansiz")
                    await bot.delete_message(chat_id = update.callback_query.from_user.id, message_id = update.callback_query.message.message_id)
                    # await bot
                    await bot.send_message(chat_id = update.callback_query.from_user.id, text = "Botni qayta ishga tushrish", reply_markup=buttons)
                    raise CancelHandler()
                else:
                    await update.callback_query.answer("❌ Siz bizning kanlga obuna bo'lmadingiz", show_alert = True)
                    raise CancelHandler()
            
            
                

                
                
            elif not await check_sub(user_id=id, chanel=setting.data['main_chanel_id']):
                await bot.send_message(chat_id = id, text = "Iltimos bizning Grand Nasiya kanlimizga obuna bo'ling", reply_markup=keyboard)
                raise CancelHandler()
        

        elif update.channel_post:
            # print(update.channel_post.chat.id)
            if update.channel_post.chat.id != setting.data['main_chanel_id']:
                raise CancelHandler()
