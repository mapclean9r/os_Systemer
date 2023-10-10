from src.userdata import database_creation
from tkinter import messagebox
import tkinter as tk
from tkinter import *
import sys
sys.path.append('src')

check_if_admin=0;
def login_checker(self):
    username = self.entry_username.get()
    password = self.entry_password.get()

    database_creation.cursor.execute(
        'SELECT * FROM users WHERE username = ? AND password = ?', (username, password))
    user = database_creation.cursor.fetchone()

    if user:
        self.username = username
        self.show_marketplace()
    else:
        messagebox.showerror("Error", "Incorrect username or password.")


def display_login(self):
    frame = tk.Frame(self)
    frame.pack(pady=75)

    lbl_title = tk.Label(
        frame, text="Welcome to the greatest collection of experiences", font=("Arial", 24))
    lbl_title.pack()

    lbl_username = tk.Label(frame, text="Username")
    lbl_username.pack(pady=10)
    self.entry_username = tk.Entry(frame)
    self.entry_username.pack(pady=10)

    lbl_password = tk.Label(frame, text="Password")
    lbl_password.pack(pady=2)
    self.entry_password = tk.Entry(frame, show="*")
    self.entry_password.pack(pady=3)

    # TODO Gjør så checkboksen har en funksjonalitet, som den ser ut nå, så har den ingen funksjon.

    checkbox = Checkbutton(frame, text="Login as Admin?", variable=check_if_admin)
    checkbox.pack()

    btn_login = tk.Button(frame, text="Login", width=18, command=self.login)
    btn_login.pack(pady=40)
    btn_register = tk.Button(frame, text="Register", width=18, command=self.register)
    btn_register.pack()
