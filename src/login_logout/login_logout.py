from tkinter import messagebox


def login(self):
    username = self.entry_username.get()
    password = self.entry_username.get()

    cursor.execute(
        'SELECT * FROM users WHERE username=? AND password=?', (username, password))
    user = cursor.fetchone()

    if user:
        self.username = username
        self.show_marketplace()
    else:
        messagebox.showerror("Error", "Incorrect username or password.")


def logout(self):
    answer = messagebox.askyesno("Logout", "Are you sure you want to log out?")
    if not answer:
        return

    for widget in self.winfo_children():
        widget.destroy()
    self.username = None
    self.show_login()
