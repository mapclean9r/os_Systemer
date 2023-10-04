import tkinter as tk


def open_home_site(root, user_type):
    clear_home_page(root)

    homepage_label = tk.Label(root, text=f"Velkommen, {user_type}!")
    homepage_label.pack()

    new_button = tk.Button(root, text="hey")
    # TODO her kan det legges til mer innhold


def clear_home_page(root):
    for widget in root.winfo_children():
        widget.pack_forget()
