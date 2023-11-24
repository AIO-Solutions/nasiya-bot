from loader import dp, types, setting, bot
import re
sot = re.compile(r"/sot|.*/sot.*|.*/sot")


@dp.channel_post_handler(content_types = types.ContentType.VIDEO)
async def chanel_video_handler(message : types.Message):
    if not message.is_forward() and sot.match(message.caption):
        caption = message.caption.replace("/sot", '')
        if len(caption) > 1:
            await message.edit_caption(caption = caption,
                                       reply_markup = types.InlineKeyboardMarkup(inline_keyboard = [[types.InlineKeyboardButton(text = '🛒 Buyurtma berish', url = f"{setting.data['myself']}?start={message.message_id}")]]))
    
    if message.is_forward() and sot.match(message.caption):
        caption = message.caption.replace("/sot", '')
        if len(caption) > 1:
            await bot.send_video(chat_id = message.chat.id, video = message.video.file_id, caption = caption,
                                 reply_markup = types.InlineKeyboardMarkup(inline_keyboard = [[types.InlineKeyboardButton(text = '🛒 Buyurtma berish', url = f"{setting.data['myself']}?start={message.message_id}")]]))
            await bot.delete_message(chat_id = message.chat.id, message_id = message.message_id)



@dp.edited_channel_post_handler(content_types = types.ContentType.VIDEO)
async def chanel_video_handler_when_updated(message : types.Message):
    # print(sot.match(message.caption))
    if not message.is_forward() and sot.match(message.caption):
        caption = message.caption.replace("/sot", '')
        if len(caption) > 1:
            await message.edit_caption(caption = caption,
                                       reply_markup = types.InlineKeyboardMarkup(inline_keyboard = [[types.InlineKeyboardButton(text = '🛒 Buyurtma berish', url = f"{setting.data['myself']}?start={message.message_id}")]]))
    
    elif message.is_forward() and sot.match(message.caption):
        caption = message.caption.replace("/sot", '')
        if len(caption) > 1:
            await bot.send_video(chat_id = message.chat.id, video = message.video.file_id, caption = caption,
                                 reply_markup = types.InlineKeyboardMarkup(inline_keyboard = [[types.InlineKeyboardButton(text = '🛒 Buyurtma berish', url = f"{setting.data['myself']}?start={message.message_id}")]]))
            await bot.delete_message(chat_id = message.chat.id, message_id = message.message_id)
    
    
