import sqlite3

class Database:
    def __init__(self, file : str):
        self.file = file

        conection = sqlite3.connect(file)
        cursor = conection.cursor()
        
        cursor.execute(f"CREATE TABLE IF NOT EXISTS users ('id' INTEGER , 'name', 'number', 'registred');")
        cursor.execute(f"CREATE TABLE IF NOT EXISTS admins ('id' INTEGER , 'name', 'registred');")
        cursor.execute(f"CREATE TABLE IF NOT EXISTS orders ('id' INTEGER, 'user_id' INTEGER, 'name', 'pay_type', 'message_id' INTEGER, 'ordered_time', PRIMARY KEY('id' AUTOINCREMENT));")
        cursor.execute(f"CREATE TABLE IF NOT EXISTS arxiv ('id' INTEGER, 'user_id' INTEGER, 'name', 'pay_type', 'message_id' INTEGER, 'ordered_time');")
        
        conection.commit()
        conection.close()

    
    def save_order(self, by_name = False, by_id = False, user_id = None, order_name : str = None, pay_type = None, ordered_time = None, message_id = None):
        conection = sqlite3.connect(self.file)
        cursor = conection.cursor()
        if by_name:
            order_name = order_name.replace("'", '"')
            match = f"INSERT INTO orders ('user_id', 'name', 'pay_type', 'ordered_time') VALUES ({user_id}, '{order_name}', '{pay_type}', '{ordered_time}');"
            cursor.execute(match)

        elif by_id:
            match = f"INSERT INTO orders ('user_id', 'message_id', 'pay_type', 'ordered_time') VALUES ({user_id}, '{message_id}', '{pay_type}', '{ordered_time}');"
            cursor.execute(match)

        conection.commit()
        conection.close()


    def get_data(self, admin = False):
        conection = sqlite3.connect(self.file)
        cursor = conection.cursor()
        data = {}

        if admin:
            for row in cursor.execute(f"SELECT * FROM admins;"):
                id, name, registred_time = row[0], row[1], row[2]
                name = name.replace('"', "'")
                data[id] = {'name' : name, 'where' : None, 'registred' : registred_time}
        
        else:
            for row in cursor.execute(f"SELECT * FROM users;"):
                id, name, number, registred_time = row[0], row[1], row[2], row[3]
                name = name.replace('"', "'")
                data[id] = {'name' : name, 'where' : None, 'registred' : registred_time, 'number' : number}

        conection.commit()
        conection.close()
        
        return data
    

    def registir(self, id : int = None, name : str = None, registred = None, admin = False, number = None):
        conection = sqlite3.connect(self.file)
        cursor = conection.cursor()

        name = name.replace("'", '"')
        
        if admin:
            match = f"INSERT INTO admins ('id', 'name', 'registred') VALUES ({id}, '{name}', '{registred}');"
            match2 = f"DELETE  FROM users WHERE id == {id};"

            cursor.execute(match)
            cursor.execute(match2)
            
            print(f'New admin {name}')

        else:
            match = f"INSERT INTO users ('id', 'name', 'number', 'registred') VALUES ({id}, '{name}', '{number}', '{registred}');"
            cursor.execute(match)
            print('New user ', name)

        conection.commit()
        conection.close()
    
    def delet_admin(self, id : int):
        conection = sqlite3.connect(self.file)
        cursor = conection.cursor()
        
        cursor.execute(f"DELETE  FROM admins WHERE id == {id};")

        conection.commit()
        conection.close()
    
    def update_user_data(self, id = None, name : str = None, number = None):
        conection = sqlite3.connect(self.file)
        cursor = conection.cursor()

        if name:
            name = name.replace("'", '"')
            cursor.execute(f"UPDATE users SET 'name' == '{name}' WHERE id == {id};")

        elif number:
            cursor.execute(f"UPDATE users SET 'number' == '{number}' WHERE id == {id};")

        conection.commit()
        conection.close()
    
    #new
    def delet_order(self, order_id : int):
        conection = sqlite3.connect(self.file)
        cursor = conection.cursor()

        cursor.execute(f"DELET FROM orders WHERE id = {order_id};")

        conection.commit()
        conection.close()
    
    def save_arxiv(self, order_id):
        conection = sqlite3.connect(self.file)
        cursor = conection.cursor()
        
        cursor.execute(f"""INSERT INTO arxiv ('id', 'user_id', 'name', 'pay_type', 'message_id', 'ordered_time')
                        SELECT * FROM orders WHERE orders.id == {order_id};""")
        cursor.execute(f"DELETE FROM orders WHERE id = {order_id};")

        conection.commit()
        conection.close()

    
    def save_arxiv_to_orders(self, order_id):
        conection = sqlite3.connect(self.file)
        cursor = conection.cursor()

        cursor.execute(f"""INSERT INTO orders ('id', 'user_id', 'name', 'pay_type', 'message_id', 'ordered_time') 
                        SELECT * FROM arxiv WHERE arxiv.id == {order_id};""")
        cursor.execute(f"DELETE FROM arxiv WHERE id = {order_id};")
        
        conection.commit()
        conection.close()

    
    def delet_arxiv_order(self, arxiv_id):
        conection = sqlite3.connect(self.file)
        cursor = conection.cursor()

        cursor.execute(f"DELETE FROM arxiv  WHERE id = {arxiv_id};")

        conection.commit()
        conection.close()


        




    def get_orders(self, cash = False, loan = False, ofset : int = 0, limit : int = 10):
        conection = sqlite3.connect(self.file)
        cursor = conection.cursor()

        if cash:
            data = []
            orders_id = []
            command = f"""SELECT orders.id, user_id, users.name, orders.name AS order_name, ordered_time FROM orders 
                    INNER JOIN users ON users.id = orders.user_id 
                    WHERE pay_type LIKE 'naxt' 
                    ORDER BY orders.id DESC 
                    LIMIT {ofset}, {limit};"""
        
            for row in cursor.execute(command):
                orders_id.append(row[0])
                name = row[2]
                name = name.replace('"', "'")
                order_name = row[3]
                if order_name:
                    order_name = order_name.replace('"', "'")
                data.append({'user_id' : row[1], 
                         'user_name' : name,
                         'order_name' : order_name,
                         'ordered_time' : row[4]})
        
        else:
            data = []
            orders_id = []
            command = f"""SELECT orders.id, user_id, users.name, orders.name AS order_name, ordered_time FROM orders 
                    INNER JOIN users ON users.id = orders.user_id 
                    WHERE pay_type LIKE 'nasiya' 
                    ORDER BY orders.id DESC 
                    LIMIT {ofset}, {limit};"""
        
            for row in cursor.execute(command):
                orders_id.append(row[0])
                name = row[2]
                name = name.replace('"', "'")
                order_name = row[3]
                if order_name:
                    order_name = order_name.replace('"', "'")

                data.append({'user_id' : row[1], 
                         'user_name' : name,
                         'order_name' : order_name,
                         'ordered_time' : row[4]})


        conection.commit()
        conection.close()

        return data, orders_id


    def get_order(self, order_id):
        conection = sqlite3.connect(self.file)
        cursor = conection.cursor()
        data = None
        for row in cursor.execute(f"SELECT * FROM orders WHERE id = {order_id};"):
            data = {'id' : row[0], 'user_id' : row[1], 'order_name' : row[2], 'pay_type' : row[3], 'message_id' : row[4], 'time' : row[5]}
            break

        conection.commit()
        conection.close()

        return data


    def orders_len(self, loan = False):
        conection = sqlite3.connect(self.file)
        cursor = conection.cursor()
        if loan:
            for row in cursor.execute(f"SELECT COUNT(id) FROM orders WHERE pay_type LIKE 'nasiya';"):
                count = row[0]
                break
        else:
            for row in cursor.execute(f"SELECT COUNT(id) FROM orders WHERE pay_type LIKE 'naxt';"):
                count = row[0]
                break

        conection.commit()
        conection.close()

        return count

    def arxiv_len(self):
        conection = sqlite3.connect(self.file)
        cursor = conection.cursor()

        for row in cursor.execute(f"SELECT COUNT(id) FROM arxiv;"):
            count = row[0]
            break

        conection.commit()
        conection.close()

        return count

    def get_arxiv(self, ofset : int = 0, limit : int = 10):
        conection = sqlite3.connect(self.file)
        cursor = conection.cursor()

        
        data = []
        orders_id = []
        command = f"""SELECT arxiv.id, user_id, users.name, arxiv.name AS order_name, ordered_time, arxiv.pay_type AS pay FROM arxiv 
                    INNER JOIN users ON users.id = arxiv.user_id 
                    ORDER BY arxiv.id DESC 
                    LIMIT {ofset}, {limit};"""
        
        for row in cursor.execute(command):
            orders_id.append(row[0])
            name = row[2]
            name = name.replace('"', "'")
            order_name = row[3]
            if order_name:
                order_name = order_name.replace('"', "'")
            data.append({'user_id' : row[1], 
                         'user_name' : name,
                         'order_name' : order_name,
                         'ordered_time' : row[4],
                         'pay' : row[5]})
        
        conection.commit()
        conection.close()

        return data, orders_id


    def get_arxiv_data(self, order_id):
        conection = sqlite3.connect(self.file)
        cursor = conection.cursor()
        data = None
        for row in cursor.execute(f"SELECT * FROM arxiv WHERE id = {order_id};"):
            data = {'id' : row[0], 'user_id' : row[1], 'order_name' : row[2], 'pay_type' : row[3], 'message_id' : row[4], 'time' : row[5]}
            break

        conection.commit()
        conection.close()

        return data



if __name__ == '__main__':
    db = Database('test.db')
    db.registir(id = 2, name = "Shermuhammad", admin = True)
    print(db.get_data())