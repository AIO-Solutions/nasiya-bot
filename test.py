from data.base import Database
from random import randint

db = Database('data/database.db')

names = ['Anvar', 'Hasan', 'Husan', 'Botir', 'Atabek', 'Aziza', 'Laziza', 'Nigina', 'Ozoda', 'Malika']
orders = ['Olma', 'Telvizor', 'Smartfo\'n', 'Kompyuter', 'Tefal', 'Banan', 'shaftoli', 'toshiba satlite 20g', 'samsung s23', 'pitsa']
message_ids = [192, 189, 197, 179, 182, 197, 195, 196]
order_type = ['nasiya', 'naxt']

data = db.get_data()

for key, value in data.items():
    date = f"{randint(1, 30)}.{randint(1, 12)}.{randint(2018, 2023)} {randint(0, 24)}:{randint(0, 60)}"
    id = key

    if randint(0, 1):
        db.save_order(by_name = True,
                      user_id = id,
                      order_name = orders[randint(0, len(orders)-1)],
                      pay_type = order_type[randint(0, 1)],
                      ordered_time = date)

    else:
        db.save_order(by_id = True,
                      user_id = id,
                      pay_type = order_type[randint(0, 1)],
                      message_id = message_ids[randint(0, 7)],
                      ordered_time = date)

    
# for n in range(200):
#     # number = f"+998{randint(90, 99)}{randint(300, 399)}{randint(0, 9999)}"
#     date = f"{randint(1, 30)}.{randint(1, 12)}.{randint(2018, 2023)} {randint(0, 24)}:{randint(0, 60)}"

#     if randint(0, 1):
#         db.save_order(by_name = True, order_name = randint(0, len(orders)-1), user_id = )
#     db.registir(id = randint(1000000000, 9999999999), name = names[randint(0, 9)], registred = date, number = number)

