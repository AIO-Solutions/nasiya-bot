from aiogram.dispatcher.filters import ChatTypeFilter
from aiogram import types
from loader import dp, ram, bot


@dp.channel_post_handler()
async def catch_chanel_message(message : types.Message):
    # print(message)
    await bot.edit_message_text(text = "axa ko'rdim\n" + message.text, chat_id = message.sender_chat.id, message_id = message.message_id, 
                                reply_markup = types.InlineKeyboardMarkup(inline_keyboard = [[types.InlineKeyboardButton(text = 'test', callback_data = 'test')]]))