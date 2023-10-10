from tkinter import messagebox
from ..functions_gui import clear_widgets_from_screen

def logout_a_user(self):
    answer = messagebox.askyesno(
        "Logout", "Are you sure you want to log out?")
    if not answer:
        return

    clear_widgets_from_screen.clear_all_widgets(self)

    self.username = None
    self.show_login()