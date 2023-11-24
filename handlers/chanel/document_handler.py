from loader import types, dp, bot, setting
import re
sot = re.compile(r"/sot|.*/sot.*")

@dp.channel_post_handler(content_types = types.ContentType.DOCUMENT)
async def chanel_document_handler(message : types.Message):
    if not message.is_forward() and sot.match(message.caption):
        caption = message.caption.replace("/sot", '')
        if len(caption) > 1:
            await message.edit_caption(caption = caption,
                                       reply_markup = types.InlineKeyboardMarkup(inline_keyboard = [[types.InlineKeyboardButton(text = '🛒 Buyurtma berish', url = f"{setting.data['myself']}?start={message.message_id}")]]))
    
    if message.is_forward() and sot.match(message.caption):
        caption = message.caption.replace("/sot", '')
        if len(caption) > 1:
            await bot.send_document(chat_id = message.chat.id, document = message.document.file_id, caption = caption,
                                 reply_markup = types.InlineKeyboardMarkup(inline_keyboard = [[types.InlineKeyboardButton(text = '🛒 Buyurtma berish', url = f"{setting.data['myself']}?start={message.message_id}")]]))
            await bot.delete_message(chat_id = message.chat.id, message_id = message.message_id)