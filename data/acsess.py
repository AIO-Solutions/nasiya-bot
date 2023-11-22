import sqlite3

class Database:
    def __init__(self, file : str):
        self.file = file

        conection = sqlite3.connect(file)
        cursor = conection.cursor()
        
        cursor.execute(f"CREATE TABLE IF NOT EXISTS users ('id' INTEGER , 'name', 'registred');")
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
                data[id] = {'name' : name, 'where' : 'none', 'registred' : registred_time}
        
        else:
            for row in cursor.execute(f"SELECT * FROM users;"):
                id, name, registred_time = row[0], row[1], row[2]
                data[id] = {'name' : name, 'where' : 'none', 'registred' : registred_time}

        conection.commit()
        conection.close()
        
        return data
    

    def registir(self, id : int = None, name : str = None, registred = None, admin = False):
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
            match = f"INSERT INTO users ('id', 'name', 'registred') VALUES ({id}, '{name}', '{registred}');"
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
    
    def is_admin(self, id : int):
        return self.admins.get(id)
    
    def is_user(self, id : int):
        return self.users.get(id)
    
    def registr_data(self, id = None, name = None, number = None, get_data = False):
        if get_data:
            return self.registdata.get(id)
        
        if not self.registdata.get(id):
            self.registdata[id] = {}
        
        if name:
            self.registdata[id]['name'] = name
        
        if number:
            self.registdata[id]['number'] = number
    




    
    