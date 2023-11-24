from aiogram.dispatcher.filters import ChatTypeFilter
from aiogram import types
from loader import dp, ram, bot, setting
import re

sot = re.compile(r"/sot|.*/sot.*")

@dp.channel_post_handler(content_types = types.ContentType.PHOTO)
async def catch_chanel_message(message : types.Message):
    if not message.is_forward() and message.caption and sot.match(message.caption):
        await message.edit_caption(caption = message.caption.replace('/sot', ''), 
                                   reply_markup = types.InlineKeyboardMarkup(inline_keyboard = [[types.InlineKeyboardButton(text = '🛒 Buyurtma berish', url = f"{setting.data['myself']}?start={message.message_id}")]]))
    
    elif message.is_forward() and message.caption and sot.match(message.caption):
        photo = message.photo[-1]

        # Download photo file
        file_path = await bot.get_file(photo.file_id)
        await bot.download_file(file_path.file_path, destination='data/pictures/image.jpg')

        await bot.send_photo(photo = open('data/pictures/image.jpg', 'rb'), caption = message.caption.replace('/sot', ''), chat_id = message.chat.id,
                                reply_markup = types.InlineKeyboardMarkup(inline_keyboard = [[types.InlineKeyboardButton(text = '🛒 Buyurtma berish', url = f"{setting.data['myself']}?start={message.message_id}")]]))
        await bot.delete_message(chat_id = message.chat.id, message_id = message.message_id)


@dp.edited_channel_post_handler(content_types=types.ContentType.PHOTO)
async def when_photo_edited(message : types.Message):
    # print(message.caption)
    if not message.is_forward() and message.caption and sot.match(message.caption):
        await message.edit_caption(caption = message.caption.replace('/sot', ''), 
                                   reply_markup = types.InlineKeyboardMarkup(inline_keyboard = [[types.InlineKeyboardButton(text = '🛒 Buyurtma berish', url = f"{setting.data['myself']}?start={message.message_id}")]]))
    
    elif message.is_forward() and message.caption and sot.match(message.caption):
        photo = message.photo[-1]

        # Download photo file
        file_path = await bot.get_file(photo.file_id)
        await bot.download_file(file_path.file_path, destination='data/pictures/image.jpg')

        await bot.send_photo(photo = open('data/pictures/image.jpg', 'rb'), caption = message.caption.replace('/sot', ''), chat_id = message.chat.id,
                                reply_markup = types.InlineKeyboardMarkup(inline_keyboard = [[types.InlineKeyboardButton(text = '🛒 Buyurtma berish', url = f"{setting.data['myself']}?start={message.message_id}")]]))
        await bot.delete_message(chat_id = message.chat.id, message_id = message.message_id)

