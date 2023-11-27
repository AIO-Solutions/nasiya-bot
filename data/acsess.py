import sqlite3
from datetime import datetime

def now():
    now = datetime.now()
    return str(now.strftime("%d.%m.%Y %H:%M"))

class Database:
    def __init__(self, file : str):
        self.file = file

        conection = sqlite3.connect(file)
        cursor = conection.cursor()
        
        cursor.execute(f"CREATE TABLE IF NOT EXISTS users ('id' INTEGER , 'name', 'number', 'registred');")
        cursor.execute(f"CREATE TABLE IF NOT EXISTS admins ('id' INTEGER , 'name', 'registred');")
        cursor.execute(f"CREATE TABLE IF NOT EXISTS orders ('id' INTEGER, 'user_id' INTEGER, 'name', 'pay_type', 'message_id' INTEGER, 'ordered_time', PRIMARY KEY('id' AUTOINCREMENT));")
        
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
                data[id] = {'name' : name, 'where' : None, 'registred' : registred_time}
        
        else:
            for row in cursor.execute(f"SELECT * FROM users;"):
                id, name, number, registred_time = row[0], row[1], row[2], row[3]
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


class RAM(Database):
    def __init__(self, file_path: str):
        super().__init__(file_path)
        self.users = self.get_data()
        self.admins = self.get_data(admin = True)
        self.registdata = {}
        self.orders = {}
        self.block = {}
    
    def is_admin(self, id : int):
        return self.admins.get(id)
    
    def is_user(self, id : int):
        return self.users.get(id)
    
    def registr_data(self, id = None, name = None, number = None, order_id = None, get_data = False):
        if get_data:
            return self.registdata.get(id)
        
        if not self.registdata.get(id):
            self.registdata[id] = {}
        
        if name:
            self.registdata[id]['name'] = name

        if order_id:
            self.registdata[id]['order'] = order_id
        
        if number:
            self.registdata[id]['number'] = number
    
    def registir_user(self, id = None):
        if self.registdata.get(id) and self.registdata[id].get('name') and self.registdata[id].get('number'):
            
            registred = now()
            self.users[id] = {'name' : self.registdata[id]['name'], 'number' : self.registdata[id]['number'], 'where' : 'head_menu', 'registred' : registred}
            self.registir(id = id, name = self.registdata[id]['name'], registred = registred, number = self.registdata[id]['number'])

            return True
        return False
    
    def save_order(self, id = None, name = None, order_id = None, buy_type = None):
        if not self.orders.get(id):
            self.orders[id] = {}
        
        if name:
            self.orders[id]['name'] = name
        
        elif order_id:
            self.orders[id]['order_id'] = order_id
        
        elif buy_type:
            self.orders[id]['order_type'] = buy_type
    
    def update_name(self, id = None, name = None):
        self.users[id]['name'] = name
        self.update_user_data(id = id, name = name)
    
    def update_number(self, id = None, number = None):
        self.users[id]['number'] = number
        self.update_user_data(id = id, number = number)

    def admin_login(self, id : int, block : bool = False):
        if block:
            if self.block.get(id):
                self.block[id] += 1
            else:
                self.block[id] = 1

            return self.block[id]
        
        elif self.block.get(id):
            return self.block[id]
        return 0
    
    def registir_admin(self, id):
        data = self.users[id]
        self.registir(id = id, name = data['name'], registred = now(), admin = True)
        del self.users[id]
        self.admins = self.get_data(admin=True)
        return True

    def logout_admin(self, id: int):
        self.delet_admin(id=id)
        if self.block.get(id):
            del self.block[id]
        del self.admins[id]
    

    


    

    

    

    

    




    
    