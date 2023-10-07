import sqlite3
from tkinter import messagebox, simpledialog, ttk
from src.markedplaceApp import database_creation


def login_checker(self):
    username = self.entry_username.get()
    password = self.entry_password.get()

    database_creation.cursor.execute(
        'SELECT * FROM users WHERE username=? AND password=?', (username, password))
    user = database_creation.cursor.fetchone()

    if user:
        self.username = username
        self.show_marketplace()
    else:
        messagebox.showerror("Error", "Incorrect username or password.")
