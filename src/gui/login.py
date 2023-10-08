import tkinter as tk
import homepage as homepage

root = tk.Tk()
root.title("Login site")
root.geometry("800x600")

# Definere en variabel for å holde på innholdet på gjeldende side
current_page = None


def create_login_page():
    global login_label, login_button_user, login_button_admin, register_label
    global username_label, username_entry, password_label, password_entry
    global register_button, registration_label

    login_label = tk.Label(root, text="Velg brukertype:")
    login_label.pack()

    login_button_user = tk.Button(
        root, text="Login User", command=go_to_homepage_admin)
    login_button_admin = tk.Button(
        root, text="Login Admin", command=go_to_homepage_admin)

    login_button_admin.pack(side="left")
    login_button_user.pack(side="right")

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


def go_to_homepage_user():
    global current_page
    clear_login_screen()
    homepage_content = homepage.open_home_site(
        root, "Bruker")
    homepage_label.config(text=homepage_content)
    current_page = homepage_label


def go_to_homepage_admin():
    global current_page
    clear_login_screen()
    homepage_content = homepage.open_home_site(
        root, "Admin")
    homepage_label.config(text=homepage_content)
    current_page = homepage_label


def register():
    username = username_entry.get()
    password = password_entry.get()

    # Her kan du legge til logikk for å lagre brukernavn og passord
    # for eksempel i en database eller fil

    registration_label.config(text="Brukeren er registrert!")


def clear_login_screen():
    login_button_user.pack_forget()
    login_button_admin.pack_forget()
    login_label.pack_forget()


create_login_page()

# jeg vet ikke helt hva det under gjør
# homepage_label = tk.Label(root, text="")
# homepage_label.pack()

root.mainloop()
