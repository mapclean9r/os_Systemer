from tkinter import *
import tkinter as tk
from tkinter import messagebox
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

def display_login(self):
    frame = tk.Frame(self)
    frame.pack(pady=100)

    lbl_title = tk.Label(frame, text="Login", font=("Arial", 24))
    lbl_title.pack()

    lbl_username = tk.Label(frame, text="Username")
    lbl_username.pack(pady=5)
    self.entry_username = tk.Entry(frame)
    self.entry_username.pack(pady=5)

    lbl_password = tk.Label(frame, text="Password")
    lbl_password.pack(pady=5)
    self.entry_password = tk.Entry(frame, show="*")
    self.entry_password.pack(pady=5)

    # TODO Gjør så checkboksen har en funksjonalitet, som den ser ut nå, så har den ingen funksjon.
    check_val = IntVar()
    checkbox = Checkbutton(frame, text="Login as Admin?", variable=check_val)
    checkbox.pack()

    btn_login = tk.Button(frame, text="Login", command=self.login)
    btn_login.pack(pady=20)
    btn_register = tk.Button(frame, text="Register", command=self.register)
    btn_register.pack()

