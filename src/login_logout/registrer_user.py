import sqlite3
from tkinter import simpledialog, messagebox

from src.gui.markedplaceApp import cursor, conn


def making_a_user():
    username = simpledialog.askstring("Register", "Enter username:")
    password = simpledialog.askstring("Register", "Enter password:", show="*")

    try:
        cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))
        conn.commit()
        messagebox.showinfo("Success", "Registered successfully.")
    except sqlite3.IntegrityError:
        messagebox.showerror("Error", "Username already exists.")
