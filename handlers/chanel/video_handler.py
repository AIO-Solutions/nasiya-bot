from loader import dp, types, setting, bot
import re
sot = re.compile(r"/sot|.*/sot.*|.*/sot")


@dp.channel_post_handler(content_types = types.ContentType.VIDEO)
async def chanel_video_handler(message : types.Message):
    if not message.is_forward() and sot.match(message.caption):
        caption = message.caption.replace('/sot', '').replace('\n\n🕸 Telegram | Instagram | Music', '').replace('🕸Telegram | Instagram | Music', '') + "\n\n🕸 <a href='https://t.me/grandnasiya'>Telegram</a> | <a href='https://instagram.com/grand_nasiya'>Instagram</a> | <a href='https://t.me/GRANDMUSIC24'>Music</a>"
        if len(caption) > 1:
            try:
                await message.edit_caption(caption = caption,
                                       parse_mode="html",
                                       reply_markup = types.InlineKeyboardMarkup(inline_keyboard = [[types.InlineKeyboardButton(text = '🛒 Buyurtma berish', url = f"{setting.data['myself']}?start={message.message_id}")]]))
            except:
                print("Can't edit video")
    if message.is_forward() and sot.match(message.caption):
        caption = message.caption.replace('/sot', '').replace('\n\n🕸 Telegram | Instagram | Music', '').replace('🕸Telegram | Instagram | Music', '') + "\n\n🕸 <a href='https://t.me/grandnasiya'>Telegram</a> | <a href='https://instagram.com/grand_nasiya'>Instagram</a> | <a href='https://t.me/GRANDMUSIC24'>Music</a>"
        
        try:
            if len(caption) > 1:
                await bot.send_video(chat_id = message.chat.id, video = message.video.file_id, caption = caption,
                                 parse_mode="html",
                                 reply_markup = types.InlineKeyboardMarkup(inline_keyboard = [[types.InlineKeyboardButton(text = '🛒 Buyurtma berish', url = f"{setting.data['myself']}?start={message.message_id}")]]))
                await bot.delete_message(chat_id = message.chat.id, message_id = message.message_id)
        except:
            print("Can't edit video forward")


@dp.edited_channel_post_handler(content_types = types.ContentType.VIDEO)
async def chanel_video_handler_when_updated(message : types.Message):
    # print(sot.match(message.caption))
    
    if not message.is_forward() and sot.match(message.caption):
        caption = message.caption.replace('/sot', '').replace('\n\n🕸 Telegram | Instagram | Music', '').replace('🕸Telegram | Instagram | Music', '') + "\n\n🕸 <a href='https://t.me/grandnasiya'>Telegram</a> | <a href='https://instagram.com/grand_nasiya'>Instagram</a> | <a href='https://t.me/GRANDMUSIC24'>Music</a>"
        if len(caption) > 1:
            try:
                await message.edit_caption(caption = caption,
                                       parse_mode="html",
                                       reply_markup = types.InlineKeyboardMarkup(inline_keyboard = [[types.InlineKeyboardButton(text = '🛒 Buyurtma berish', url = f"{setting.data['myself']}?start={message.message_id}")]]))
            except:
                print("can't edit video whenedit")
    
    elif message.is_forward() and sot.match(message.caption):
        caption = message.caption.replace('/sot', '').replace('\n\n🕸 Telegram | Instagram | Music', '').replace('🕸Telegram | Instagram | Music', '') + "\n\n🕸 <a href='https://t.me/grandnasiya'>Telegram</a> | <a href='https://instagram.com/grand_nasiya'>Instagram</a> | <a href='https://t.me/GRANDMUSIC24'>Music</a>"
        if len(caption) > 1:
            try:
                await bot.send_video(chat_id = message.chat.id, video = message.video.file_id, caption = caption,
                                 parse_mode="html",
                                 reply_markup = types.InlineKeyboardMarkup(inline_keyboard = [[types.InlineKeyboardButton(text = '🛒 Buyurtma berish', url = f"{setting.data['myself']}?start={message.message_id}")]]))
                await bot.delete_message(chat_id = message.chat.id, message_id = message.message_id)

            except:
                print("can't edit video whenedit forfarded")



    
