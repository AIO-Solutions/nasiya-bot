from aiogram.dispatcher.filters import ChatTypeFilter
from aiogram import types
from loader import dp, ram, bot
import re

sot = re.compile(r"/sot")

@dp.channel_post_handler()
async def catch_chanel_message(message : types.Message):
    if sot.match(message.text):
        await bot.edit_message_text(text = "axa ko'rdim\n" + message.text, chat_id = message.sender_chat.id, message_id = message.message_id, 
                                reply_markup = types.InlineKeyboardMarkup(inline_keyboard = [[types.InlineKeyboardButton(text = 'test', url = "https://t.me/grand_nasiya_bot?start=1234")]]))
        