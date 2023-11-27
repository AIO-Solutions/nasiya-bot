from loader import dp, ram, types, admin_panel_states
from aiogram.dispatcher import FSMContext



# @dp.message_handler(state = admin_panel_states.cash_orders)
# async def cash_order_handler(update : types.Message, state : FSMContext):
#     if update == 