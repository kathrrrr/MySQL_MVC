from tkinter import *

class UserView:
    def __init__(self):
        #self.controller = controller
        self.root = Tk()
        self.root.geometry("600x300")  
        L1 = Label(self.root, text="User Name") 
        L1.grid(row=0,column=0) 
        L2 = Label(self.root, text="Password") 
        L2.grid(row=1,column=0) 
        self.usernm = Entry()
        self.usernm.grid(row=0,column=1, 
                      padx=10,pady=10) 
        self.passwd = Entry()
        self.passwd.grid(row=1,column=1, 
                      padx=10,pady=10) 
       
        self.L3 = Label(self.root, text="") 
        self.L3.grid(row=4,column=1)
        self.btn = Button(self.root, text = 'Opret', bd = '5',
                          command = self.create).grid(row=3, column=1) 
        self.btn1 = Button(self.root, text = 'login', bd = '5',
                          command = self.login).grid(row=3, column = 2)

  

    def setController(self, controller):
        self.controller = controller

    def create(self):
        username = self.usernm.get()
        password = self.passwd.get()
        self.controller.create_user(username, password)

    def login(self):
        username = self.usernm.get()
        password = self.passwd.get()
        self.controller.login_user(username, password)

    def run(self):
        self.root.mainloop()

  
   
  

  
    