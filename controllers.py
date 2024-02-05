





    
class UserController:
    def __init__(self, view, db_connection):
        self.view = view
        self.db = db_connection
        self.db.cursor.execute("create table if not exists users(id int primary key auto_increment, name varchar(255), password varchar(255) )")
        self.db.conn.commit()
        print("Table created")


    def create_user(self, username, password):
        # Her implementeres logik for at oprette brugeren i databasen
        # Brug self.db for at interagere med databasen
       
       

        print("create")
        print(username)
        db = self.db
        db.cursor.execute("SELECT * FROM users WHERE name = %s",(username,))
        result = db.cursor.fetchall()
        print(result)
        
        if result:
            self.view.L3.config(text="Navnet er allerede i brug. Skriv et andet navn")
        else:
            print("Navnet er ikke i brug")
            db.cursor.execute("insert into users(name, password) values(%s, %s)", (username, password))  
            self.view.L3.config(text="Brugeren er oprettet")  
            db.conn.commit()
        print("Brugeren er oprettet")

    def login_user(self, username, password):
      
        print("login")
        db = self.db
        db.cursor.execute("SELECT password FROM users WHERE name = %s",(username,))
        result = db.cursor.fetchall()
        print(result)
        if result:
            result = result[0][0]
            if result == password:
                print("Brugeren findes og password er korrekt")
                self.view.L3.config(text="Du er logget ind")
            else:
                self.view.L3.config(text="Password er forkert")
            print(result)
        else:
            print("Brugeren findes ikke")
            self.view.L3.config(text="Brugeren findes ikke")

            








