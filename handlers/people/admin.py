from loader import dp, ram, bot, types, menu
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
import sqlite3
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# Database file path
data = "data/database.db"

# Connect to the database
connection = sqlite3.connect(data)

# Create a cursor object to interact with the database
cursor = connection.cursor()

# Execute a simple query to fetch and print the contents of the "orders" table
cursor.execute("SELECT id, user_id, name, pay_type FROM orders")

# Fetch all the rows from the result set
rows = cursor.fetchall()

# Print the column names
columns = [description[0] for description in cursor.description]


class AdminStates(StatesGroup):
    password_attempts = State()


@dp.message_handler(commands='admin')
async def admin_process(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    open_base_query = 'SELECT id FROM admins'
    cursor.execute(open_base_query)
    admins_ids = [row[0] for row in cursor.fetchall()]

    if user_id not in admins_ids:
        await message.answer("Parolni kiriting")
    else:
        # Handle the case when user_id is already in the admins table
        await message.answer("Hush Kelibsiz.", reply_markup=menu.admin_buttons())
        await state.finish()


@dp.message_handler(state=AdminStates.password_attempts)
async def admin_password_entered(message: types.Message, state: FSMContext):
    user_id = message.from_user.id

    correct_password = "0000"  # Replace with your actual admin password

    if message.text == correct_password:
        # Correct password, proceed with admin actions
        await message.answer("Hush kelibsiz!", reply_markup=menu.admin_buttons())

        # Insert the user_id into the admins table
        cursor.execute('INSERT INTO admins (id) VALUES (?)', (user_id,))
        connection.commit()  # Don't forget to commit the changes
        await state.finish()
    else:
        # Incorrect password
        attempts_left = await state.get_data()  # Retrieve the current attempts count

        if "attempts" not in attempts_left:
            attempts_left["attempts"] = 2  # Initial attempts count is 2
        else:
            attempts_left["attempts"] -= 1  # Decrement attempts count

        await state.update_data(attempts=attempts_left["attempts"])

        if attempts_left["attempts"] > 0:
            await message.answer(f"Notog'ri parol. {attempts_left['attempts']} Urunish qoldi. Iltimos qaytadan urunib ko'ring.")
        else:
            # Block the user after 3 incorrect attempts
            await message.answer("Too many incorrect attempts. You are now blocked.")
            # Block the user using the ram module

            # Reset the state
            await state.finish()


# ... (previous code)

@dp.message_handler(lambda message: message.text.lower() in ['naxt', 'nasiya'])
async def naxt_handler(message: types.Message, state: FSMContext):
    global inline_keyboard, net
    response_messages = []
    inline_keyboard = InlineKeyboardMarkup(row_width=2)

    for count, row in enumerate(rows, start=1):
        if message.text.lower() == row[3].lower():
            user_id = row[1]
            cursor.execute("SELECT name, number FROM users WHERE id = ?", (user_id,))
            user_data = cursor.fetchone()
            response_messages.append(f"{count}. {user_data[0]}")
            inline_keyboard.add(InlineKeyboardButton(f"{count}", callback_data=f"count_button_{count}"))

    await state.update_data(url=f"https://t.me/blahblat/{message.message_id}")

    if response_messages:
        if len(response_messages) <= 10:
            net = "\n".join(response_messages)
            print(net)
            await message.answer(net, reply_markup=inline_keyboard)
        else:
            chunks = [response_messages[i:i + 10] for i in range(0, len(response_messages), 10)]
            net = "\n".join(chunks[0])
            next_page_button = InlineKeyboardButton("Next Page", callback_data="next_page_1")
            inline_keyboard.add(next_page_button)
            await message.answer(net, reply_markup=inline_keyboard)
            await state.update_data(chunks=chunks[1:])


# @dp.callback_query_handler(lambda query: query.data.startswith('next_page'))
# async def callback_next_page_handler(query: types.CallbackQuery, state: FSMContext):
#     page_number = int(query.data.split('_')[2])
#     chunks = await state.get_data("chunks")
    
#     if chunks and len(chunks) > 0:
#         current_chunk = chunks.pop(0)
#         net = "\n".join(current_chunk)

#         if chunks:
#             inline_keyboard = InlineKeyboardMarkup(row_width=2)
#             next_page_button = InlineKeyboardButton("Next Page", callback_data=f"next_page_{page_number + 1}")
#             inline_keyboard.add(next_page_button)
#             await bot.edit_message_text(
#                 chat_id=query.message.chat.id,
#                 message_id=query.message.message_id,
#                 text=net,
#                 reply_markup=inline_keyboard
#             )
#         else:
#             await bot.edit_message_text(
#                 chat_id=query.message.chat.id,
#                 message_id=query.message.message_id,
#                 text=net
#             )
#         await state.update_data(chunks=chunks)
#     await query.answer()



@dp.callback_query_handler(lambda query: query.data.startswith(f'count_button'))
async def callback_count_button_handler(query: types.CallbackQuery, state: FSMContext):
    # Extract the count from the callback data
    count = int(query.data.split('_')[2])

    # Assuming you have the rows variable available from the previous code
    row = rows[count - 1]

    user_id = row[1]
    name = row[2]

    cursor.execute("SELECT name, number, registred FROM users WHERE id = ?", (user_id,))
    user_data = cursor.fetchone()

    # Extract the message_id from the tuple
    message_id = user_data[0] if user_data else None

    # Save the message_id in the state
    await state.update_data(message_id=message_id)

    # Check if message_id is not None before redirecting to the URL
    if message_id is not None:
        data_ = "\n".join(str(info) for info in user_data) if user_data else "No data available."

        # Create an inline keyboard with a back button
        back_button = InlineKeyboardButton("Back", callback_data="back_button")
        order = InlineKeyboardButton('Order', callback_data='order')
        delete = InlineKeyboardButton('Bajarildi', callback_data=f'delete_{count}')
        inline_keyboard = InlineKeyboardMarkup().add(back_button, order, delete)

        # Edit the previous message (the one that triggered the callback) with the new content and inline keyboard
        await bot.edit_message_text(
            chat_id=query.message.chat.id,
            message_id=query.message.message_id,
            text=f"{data_}",
            reply_markup=inline_keyboard
        )

        # Answer the callback query to remove the inline keyboard
        await query.answer()
    else:
        # Handle the case when message_id is None
        await query.message.answer("No message_id available.")
        await query.answer()


@dp.callback_query_handler(lambda query: query.data == "back_button")
async def callback_back_button_handler(query: types.CallbackQuery, state: FSMContext):
    global net  # Declare net as a global variable
    await query.message.edit_text(net, reply_markup=inline_keyboard)
    await query.answer()


@dp.callback_query_handler(lambda query: query.data == "order")
async def callback_back_button_handler(query: types.CallbackQuery, state: FSMContext):
    cursor.execute('SELECT user_id, message_id FROM orders')

    # Fetch all rows from the result set
    rows = cursor.fetchall()

    for i in rows:
        if i[0] == query.from_user.id:
            urls = f'https://t.me/blahblat/{i[1]}'

            print(urls)
            back_button = InlineKeyboardButton("Back", callback_data="back_button")

            inline_keyboard = InlineKeyboardMarkup().add(back_button)

            await query.message.edit_text(f'Buyurtma: {urls}', reply_markup=inline_keyboard)




@dp.message_handler(lambda message: message.text == 'Sozlamalar')
async def settings(message: types.Message, state: FSMContext):
    await message.answer("Bu yerda Sozlamalar mavjud")



# ... (previous code)

@dp.callback_query_handler(lambda query: query.data.startswith('delete'))
async def callback_delete_handler(query: types.CallbackQuery, state: FSMContext):
    user_id = int(query.data.split('_')[1])  # Extract user_id from the callback data

    # Delete specific columns from the "orders" table
    cursor.execute("UPDATE orders SET user_id=NULL, name=NULL, pay_type=NULL, message_id=NULL, ordered_time=NULL WHERE user_id=?", (user_id,))
    connection.commit()
    
    # Inform the user that the data has been deleted
    await query.message.answer("Data has been successfully deleted.")

    # Return to the previous state (showing the list of users)
    await query.answer()
    await bot.edit_message_text(
        chat_id=query.message.chat.id,
        message_id=query.message.message_id,
        text=net,
        reply_markup=inline_keyboard
    )
