from tkinter import messagebox

def logout_a_user(self):
    answer = messagebox.askyesno(
        "Logout", "Are you sure you want to log out?")
    if not answer:
        return

    for widget in self.winfo_children():
        widget.destroy()
    self.username = None
    self.show_login()