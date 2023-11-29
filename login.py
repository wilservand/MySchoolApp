import tkinter as tk
from tkinter import messagebox
from dbConnect import *
from main import *
root = tk.Tk()
dbApp = mainDB()
conn_dbApp, curr_dbApp = dbApp.connect()

class LoginPage:
    def __init__(self, root):
        self.root = root
        self.conn = conn_dbApp
        self.curr = curr_dbApp
        self.root.title("Login Page")
        self.root.geometry("1920x1080")


        # Create and place the username label and entry
        self.username_label = tk.Label(root, text="Username:")
        self.username_label.pack(pady=10)
        self.username_entry = tk.Entry(root)
        self.username_entry.pack(pady=10)

        # Create and place the password label and entry
        self.password_label = tk.Label(root, text="Password:")
        self.password_label.pack(pady=10)
        self.password_entry = tk.Entry(root, show="*")  # 'show' attribute is used to hide the entered password
        self.password_entry.pack(pady=10)

        # Create and place the login button
        self.login_button = tk.Button(root, text="Login", command=self.login)
        self.login_button.pack(pady=20)

    def login(self):
        entered_username = self.username_entry.get()
        entered_password = self.password_entry.get()
        sql_user = "SELECT `username` FROM `user_account` WHERE `username` = (%s)"
        self.curr.execute(sql_user, entered_username)
        user_pop = self.curr.fetchone()
        for x in user_pop:
            userzz = x
        print(userzz)
        sql_password = "SELECT `user_password` FROM `user_account` WHERE `username` = (%s)"
        self.curr.execute(sql_password, entered_username)
        password_pop = self.curr.fetchone()
        for x in password_pop:
            passwordzz = x
        print(passwordzz)

        # Check if the username and password are correct (you would replace this with your own authentication logic)
        if entered_username == userzz and entered_password == passwordzz:
            messagebox.showinfo("Login", "Login successful!")
            self.root.destroy()
            appOperation()
        else:
            messagebox.showerror("Login Error", "Invalid username or password")

login_page = LoginPage(root)

root.mainloop()



