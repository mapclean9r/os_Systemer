import sqlite3
import tkinter as tk
from tkinter import messagebox, simpledialog, ttk


def login_check(self):
    username = self.entry_username.get()
    password = self.entry_password.get()

    cursor.execute(
        'SELECT * FROM users WHERE username=? AND password=?', (username, password))
    user = cursor.fetchone()

    if user:
        self.username = username
        self.show_marketplace()
    else:
        messagebox.showerror("Error", "Incorrect username or password.")
