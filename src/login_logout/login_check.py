from tkinter import messagebox


def check_username(user_self, user, markedplace):
    if user:
        user_self = user
        markedplace()
    else:
        messagebox.showerror("Error", "Incorrect username or password.")