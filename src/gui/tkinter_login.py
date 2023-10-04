import tkinter as tk
import tkinter_homepage as homepage

root = tk.Tk()
root.title("Login site")
root.geometry("1200x700")

def show_homepage_user():  # viser hjem skjerm for bruekr
    clear_login_screen()
    homepage_content = homepage.open_home_site(root, "Bruker")
    homepage_label.config(text=homepage_content)


def register():
    username = username_entry.get()
    password = password_entry.get()

    # Her kan du legge til logikk for å lagre brukernavn og passord
    # for eksempel i en database eller fil

    registration_label.config(text="Brukeren er registrert!")


def clear_login_screen():  # fjerner loginside innhold
    login_button_user.pack_forget()
    login_label.pack_forget()





login_label = tk.Label(root, text="Velg brukertype:")
login_label.pack()

login_button_user = tk.Button(
    root, text="Login User", command=show_homepage_user)
#login_button_admin = tk.Button(
    #root, text="Login Admin", command=show_homepage_admin)

#login_button_admin.pack()
login_button_user.pack()

# Inputfelt for registrering
register_label = tk.Label(root, text="Registrering")
register_label.pack()

username_label = tk.Label(root, text="Brukernavn:")
username_label.pack()

username_entry = tk.Entry(root)
username_entry.pack()

password_label = tk.Label(root, text="Passord:")
password_label.pack()

password_entry = tk.Entry(root, show="*")  # Skjul passordet
password_entry.pack()

register_button = tk.Button(root, text="Registrer", command=register)
register_button.pack()

registration_label = tk.Label(root, text="")
registration_label.pack()

# jeg vet ikke helt hva det under gjør
homepage_label = tk.Label(root, text="")
homepage_label.pack()

root.mainloop()
