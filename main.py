
from views import UserView
from controllers import UserController
import mysql.connector
from mysql.connector import Error

class DatabaseConnection():
    conn = None

    #Her implementeres __new__ metoden, som overskriver __new__ metoden i superklassen   
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(DatabaseConnection, cls).__new__(cls)
        return cls.instance
    
    def __init__(self):
        if self.conn is None:
            try:
                self.conn = mysql.connector.connect(host='localhost',
                                                   database='kathrr',
                                                   user='kathrr',
                                                   password='1234')
                if self.conn.is_connected():
                    db_Info = self.conn.get_server_info()
                    print("Connected to MySQL Server version ", db_Info)
                    self.cursor = self.conn.cursor()
                    self.cursor.execute("select database();")
                    record = self.cursor.fetchone()
                    print("You're connected to database: ", record)
            except Error as e:
                print("Error while connecting to MySQL", e)
        else:
            print("Connection already exists")
        print("type of curser: ", type(self.cursor))

if __name__ == "__main__":
    db_connection = DatabaseConnection()  # Initialiser din databaseforbindelse her
    view = UserView()
    controller = UserController(view, db_connection)
    print(dir(view))
    print(view.__class__.__class__)
  
    view.setController(controller)
    view.run()




 