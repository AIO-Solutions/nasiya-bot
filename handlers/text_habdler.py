from loader import dp, types



@dp.message_handler()
async def message(message: types.Message):
    await message.answer(message.text)
