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


class RAM(Database):
    def __init__(self, file_path: str):
        super().__init__(file_path)
        self.users = self.get_data()
        self.admins = self.get_data(admin = True)
        self.registdata = {}
        self.orders = {}
    
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
            self.orders[id]['order_id'] = name
        
        elif buy_type:
            self.orders[id]['order_type'] = buy_type
        
    

    

    

    

    




    
    