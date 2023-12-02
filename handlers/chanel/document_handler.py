from loader import types, dp, bot, setting
import re
sot = re.compile(r"/sot|.*/sot.*")

@dp.channel_post_handler(content_types = types.ContentType.DOCUMENT)
async def chanel_document_handler(message : types.Message):
    if not message.is_forward() and sot.match(message.caption):
        # caption = message.caption.replace("/sot", '')
        caption = message.caption.replace('/sot', '').replace('\n\n🕸 Telegram | Instagram | Music', '').replace('🕸Telegram | Instagram | Music', '') + "\n\n🕸 <a href='https://t.me/grandnasiya'>Telegram</a> | <a href='https://instagram.com/grand_nasiya'>Instagram</a> | <a href='https://t.me/GRANDMUSIC24'>Music</a>"
        if len(caption) > 1:
            await message.edit_caption(caption = caption, parse_mode = "html",
                                       reply_markup = types.InlineKeyboardMarkup(inline_keyboard = [[types.InlineKeyboardButton(text = '🛒 Buyurtma berish', url = f"{setting.data['myself']}?start={message.message_id}")]]))
    
    if message.is_forward() and sot.match(message.caption):
        caption = message.caption.replace('/sot', '').replace('\n\n🕸 Telegram | Instagram | Music', '').replace('🕸Telegram | Instagram | Music', '') + "\n\n🕸 <a href='https://t.me/grandnasiya'>Telegram</a> | <a href='https://instagram.com/grand_nasiya'>Instagram</a> | <a href='https://t.me/GRANDMUSIC24'>Music</a>"
        if len(caption) > 1:
            await bot.send_document(chat_id = message.chat.id, parse_mode = "html", document = message.document.file_id, caption = caption,
                                 reply_markup = types.InlineKeyboardMarkup(inline_keyboard = [[types.InlineKeyboardButton(text = '🛒 Buyurtma berish', url = f"{setting.data['myself']}?start={message.message_id}")]]))
            await bot.delete_message(chat_id = message.chat.id, message_id = message.message_id)



@dp.edited_channel_post_handler(content_types = types.ContentType.DOCUMENT)
async def chanel_document_handler_when_edit(message : types.Message):
    if not message.is_forward() and sot.match(message.caption):
        # caption = message.caption.replace("/sot", '')
        caption = message.caption.replace('/sot', '').replace('\n\n🕸 Telegram | Instagram | Music', '').replace('🕸Telegram | Instagram | Music', '') + "\n\n🕸 <a href='https://t.me/grandnasiya'>Telegram</a> | <a href='https://instagram.com/grand_nasiya'>Instagram</a> | <a href='https://t.me/GRANDMUSIC24'>Music</a>"
        if len(caption) > 1:
            await message.edit_caption(caption = caption, parse_mode = "html",
                                       reply_markup = types.InlineKeyboardMarkup(inline_keyboard = [[types.InlineKeyboardButton(text = '🛒 Buyurtma berish', url = f"{setting.data['myself']}?start={message.message_id}")]]))
    
    if message.is_forward() and sot.match(message.caption):
        caption = message.caption.replace('/sot', '').replace('\n\n🕸 Telegram | Instagram | Music', '').replace('🕸Telegram | Instagram | Music', '') + "\n\n🕸 <a href='https://t.me/grandnasiya'>Telegram</a> | <a href='https://instagram.com/grand_nasiya'>Instagram</a> | <a href='https://t.me/GRANDMUSIC24'>Music</a>"
        if len(caption) > 1:
            await bot.send_document(chat_id = message.chat.id, parse_mode = "html", document = message.document.file_id, caption = caption,
                                 reply_markup = types.InlineKeyboardMarkup(inline_keyboard = [[types.InlineKeyboardButton(text = '🛒 Buyurtma berish', url = f"{setting.data['myself']}?start={message.message_id}")]]))
            await bot.delete_message(chat_id = message.chat.id, message_id = message.message_id)