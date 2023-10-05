import sqlite3
import tkinter as tk
from tkinter import messagebox, simpledialog, ttk

from src.login_logout import login_check, registrer_user
from src.login_logout import registrer_user

# Database Setup
conn = sqlite3.connect('tour_marketplace.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    username TEXT UNIQUE,
    password TEXT
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS tours (
    id INTEGER PRIMARY KEY,
    title TEXT,
    description TEXT,
    offered_by INTEGER,
    FOREIGN KEY(offered_by) REFERENCES users(id)
)
''')
conn.commit()


# GUI
class MarketplaceApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('Guided Tour Marketplace')
        self.geometry('500x400')

        self.username = None
        self.show_login()

    def show_login(self):
        frame = tk.Frame(self)
        frame.pack(pady=100)

        lbl_title = tk.Label(frame, text="Login", font=("Arial", 24))
        lbl_title.pack()

        lbl_username = tk.Label(frame, text="Username")
        lbl_username.pack(pady=5)
        self.entry_username = tk.Entry(frame)
        self.entry_username.pack(pady=5)

        lbl_password = tk.Label(frame, text="Password")
        lbl_password.pack(pady=5)
        self.entry_password = tk.Entry(frame, show="*")
        self.entry_password.pack(pady=5)

        btn_login = tk.Button(frame, text="Login", command=self.login)
        btn_login.pack(pady=20)
        btn_register = tk.Button(frame, text="Register", command=self.register)
        btn_register.pack()

    def login(self):
        username = self.entry_username.get()
        password = self.entry_password.get()

        cursor.execute('SELECT * FROM users WHERE username=? AND password=?', (username, password))
        user = cursor.fetchone()

        login_check.check_username(self.username, username, self.show_marketplace)
    def register(self):

        registrer_user.making_a_user()

    def logout(self):
        answer = messagebox.askyesno("Logout", "Are you sure you want to log out?")
        if not answer:
            return

        for widget in self.winfo_children():
            widget.destroy()
        self.username = None
        self.show_login()

    def show_marketplace(self):
        for widget in self.winfo_children():
            widget.destroy()

        frame = tk.Frame(self)
        frame.pack(pady=20)

        lbl_title = tk.Label(frame, text=f"Welcome, {self.username}", font=("Arial", 24))
        lbl_title.pack(pady=20)

        btn_offer_tour = tk.Button(frame, text="Offer a Tour", command=self.offer_tour)
        btn_offer_tour.pack(pady=20)

        btn_logout = tk.Button(frame, text="Logout", command=self.logout)
        btn_logout.pack(pady=20)

        btn_delete_tour = tk.Button(frame, text="Delete Tour", command=self.delete_tour)
        btn_delete_tour.pack(pady=20)

        self.tree = ttk.Treeview(frame, columns=('Title', 'Description', 'Offered by'))
        self.tree.heading('Title', text='Title')
        self.tree.heading('Description', text='Description')
        self.tree.heading('Offered by', text='Offered by')
        self.tree.pack(pady=20)

        cursor.execute('SELECT title, description, username FROM tours JOIN users ON tours.offered_by=users.id')
        for tour in cursor.fetchall():
            self.tree.insert("", "end", values=tour)

    def offer_tour(self):
        title = simpledialog.askstring("Offer a Tour", "Enter tour title:")
        description = simpledialog.askstring("Offer a Tour", "Enter tour description:")

        cursor.execute('SELECT id FROM users WHERE username=?', (self.username,))
        user_id = cursor.fetchone()[0]

        cursor.execute('INSERT INTO tours (title, description, offered_by) VALUES (?, ?, ?)',
                       (title, description, user_id))
        conn.commit()

        self.tree.insert("", "end", values=(title, description, self.username))
        messagebox.showinfo("Success", "Tour offered successfully.")

    def delete_tour(self):
        selected_tour = self.tree.selection()

        if not selected_tour:
            messagebox.showerror("Error", "No tour selected.")
            return

        confirm = messagebox.askyesno("Delete Tour", "Are you sure you want to delete the selected tour?")
        if not confirm:
            return

        tour_title = self.tree.item(selected_tour)['values'][0]
        cursor.execute("DELETE FROM tours WHERE title=?", (tour_title,))
        conn.commit()

        self.tree.delete(selected_tour)
        messagebox.showinfo("Success", "Tour deleted successfully.")


if __name__ == '__main__':
    app = MarketplaceApp()
    app.mainloop()