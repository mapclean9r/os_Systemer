import tkinter as tk
import tkinter_homepage as homepage


def show_homepage_user():  # viser hjem skjerm for bruekr
    clear_login_screen()
    homepage_content = homepage.open_home_site(root, "Bruker")
    homepage_label.config(text=homepage_content)


def show_homepage_admin():  # viser hjem skjerm for admin
    clear_login_screen()
    homepage_content = homepage.open_home_site(root, "Admin")
    homepage_label.config(text=homepage_content)


def clear_login_screen():  # fjerner loginside innhold
    login_button_user.pack_forget()
    login_button_admin.pack_forget()
    login_label.pack_forget()


root = tk.Tk()
root.title("Login site")
root.geometry("400x300")

login_label = tk.Label(root, text="Velg brukertype:")
login_label.pack()

login_button_user = tk.Button(
    root, text="Login User", command=show_homepage_user)
login_button_admin = tk.Button(
    root, text="Login Admin", command=show_homepage_admin)

login_button_user.pack()
login_button_admin.pack()

# jeg vet ikke helt hva det under gjør
homepage_label = tk.Label(root, text="")
homepage_label.pack()

root.mainloop()
