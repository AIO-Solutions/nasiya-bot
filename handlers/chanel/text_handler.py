from aiogram.dispatcher.filters import ChatTypeFilter
from aiogram import types
from loader import dp, ram, bot, setting
import re

sot = re.compile(r"/sot|.*/sot.*")

@dp.channel_post_handler(content_types = types.ContentTypes.TEXT)
async def catch_chanel_message(message : types.Message):
    if sot.match(message.text):
        text = message.text.replace("/sot", '')
        if len(text) > 1:
            await bot.edit_message_text(text = text, chat_id = message.sender_chat.id, message_id = message.message_id, 
                                reply_markup = types.InlineKeyboardMarkup(inline_keyboard = [[types.InlineKeyboardButton(text = '🛒 Buyurtma berish', url = f"{setting.data['myself']}?start={message.message_id}")]]))



@dp.edited_channel_post_handler(content_types = types.ContentTypes.TEXT)
async def catch_chanel_message_when_edit(message : types.Message):
    if sot.match(message.text):
        text = message.text.replace("/sot", '')
        if len(text) > 1:
            await bot.edit_message_text(text = text, chat_id = message.sender_chat.id, message_id = message.message_id, 
                                reply_markup = types.InlineKeyboardMarkup(inline_keyboard = [[types.InlineKeyboardButton(text = '🛒 Buyurtma berish', url = f"{setting.data['myself']}?start={message.message_id}")]]))