import tkinter as tk


def open_home_site(root, user_type):
    clear_page(root)

    homepage_label = tk.Label(root, text=f"Velkommen, {user_type}!")
    homepage_label.pack()
    if (user_type == "Admin"):
        bann_button = tk.Button(root, text="Block / Bann users")
        bann_button.pack()

    create_experience_button = tk.Button(root, text="Create experience")
    create_experience_button.pack()

    logout_button = tk.Button(root, text="logout", command=logout)
    logout_button.pack()

    # TODO her kan det legges til mer innhold


def clear_page(root):
    for widget in root.winfo_children():
        widget.pack_forget()


def logout():
    clear_page(root)
    go_to_loginsite()


def go_to_loginsite():
    clear_page()
    homepage_content = homepage.open_home_site(root, "Bruker")
    homepage_label.config(text=homepage_content)

    login_label = tk.Label(root, text="Velg brukertype:")
    login_label.pack()

    login_button_user = tk.Button(
        root, text="Login User", command=show_homepage_user)
    login_button_admin = tk.Button(
        root, text="Login Admin", command=show_homepage_admin)

    login_button_admin.pack()
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
