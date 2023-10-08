import sqlite3
from tkinter import simpledialog, messagebox
from src.userdata import database_creation

def making_a_user(self):
    username = simpledialog.askstring("Register", "Enter username:")
    password = simpledialog.askstring(
        "Register", "Enter password:", show="*")

    try:
        database_creation.cursor.execute(
            'INSERT INTO users (username, password) VALUES (?, ?)', (username, password))
        database_creation.conn.commit()
        messagebox.showinfo("Success", "Registered successfully.")
    except sqlite3.IntegrityError:
        messagebox.showerror("Error", "Username already exists.")
