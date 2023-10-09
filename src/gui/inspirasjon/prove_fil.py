import tkinter as tk

root = tk.Tk()
root.title("Navigasjonshåndtering")
root.geometry("800x600")

# Dette er en global variabel for å lagre innholdet på gjeldende side
current_page = None


def show_page(page_content):
    global current_page

    # Fjern gjeldende side hvis den eksisterer
    if current_page is not None:
        current_page.pack_forget()

    # Vis den nye siden
    current_page = page_content
    current_page.pack()


def show_login_page():
    # Lag innholdet for loginsiden
    login_label = tk.Label(root, text="Logg inn")
    username_label = tk.Label(root, text="Brukernavn:")
    username_entry = tk.Entry(root)
    password_label = tk.Label(root, text="Passord:")
    password_entry = tk.Entry(root, show="*")
    login_button = tk.Button(root, text="Logg inn", command=login)

    login_label.pack()
    username_label.pack()
    username_entry.pack()
    password_label.pack()
    password_entry.pack()
    login_button.pack()

    show_page(login_label)


def show_home_page(username):
    # Lag innholdet for hjemmesiden med brukerens navn
    welcome_label = tk.Label(root, text=f"Velkommen, {username}!")
    logout_button = tk.Button(root, text="Logg ut", command=show_login_page)

    welcome_label.pack()
    logout_button.pack()

    show_page(welcome_label)


def login():
    # Legg til logikk for å validere brukernavn og passord her
    # Her bruker vi et forenklet eksempel hvor innskrivet brukernavn blir brukt som brukernavn
    username = username_entry.get()

    # Kall show_home_page med brukernavnet hvis validering er vellykket
    show_home_page(username)


# Vis loginsiden som startside
show_login_page()

root.mainloop()
