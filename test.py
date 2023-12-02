from aiogram import Dispatcher, types, Bot, executor
import logging


bot = Bot(token = "6082856375:AAEsIVNrfe7TDUmIvJNsztqjuZjCiLMp4ns")
dp = Dispatcher(bot)



@dp.channel_post_handler(content_types = types.ContentType.PHOTO)
async def handler(message : types.Message):
    print(message)
    # await message.edit_reply_markup(reply_markup = types.InlineKeyboardMarkup(inline_keyboard = [[types.InlineKeyboardButton(text = "clik", callback_data="clic")]]))

@dp.channel_post_handler(content_types = types.ContentType.TEXT)
async def handler_text(message : types.Message):
    print(message.text)
    # await bot.copy_message(from_chat_id= message.sender_chat.id,
    #                        chat_id = message.chat.id,
    #                        message_id = message.forward_from_message_id)



if __name__ == '__main__':
    logging.basicConfig(level = logging.INFO)
    executor.start_polling(dp, skip_updates = False)
