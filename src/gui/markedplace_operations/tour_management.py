import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
from src.userdata import database_creation
from src.gui.adminpanel import admin_prompt
from ..functions_gui import clear_widgets_from_screen

def display_marketplace(self):
    clear_widgets_from_screen.clear_all_widgets(self)

    frame = tk.Frame(self)
    frame.pack(pady=20)

    lbl_title = tk.Label(
        frame, text=f"Welcome, {self.username}", font=("Arial", 24))
    lbl_title.pack(pady=20)

    # TODO må gi denne knappen funksjonalitet.
    block_ban_button = tk.Button(frame, command=admin_prompt, text="Bann/Block users", fg="#8B0000")
    block_ban_button.pack()

    btn_offer_tour = tk.Button(frame, command=self.offer_tour, text="Offer a Tour", fg="green")
    btn_offer_tour.pack(pady=20)

    btn_logout = tk.Button(frame, text="Logout", command=self.logout, fg="#FFD700")
    btn_logout.pack(pady=20)

    btn_delete_tour = tk.Button(
        frame, text="Delete Tour", command=self.delete_tour, fg="red")
    btn_delete_tour.pack(pady=20)

    self.tree = ttk.Treeview(frame, columns=('Title', 'Description', 'Offered by'))
    self.tree.heading('Title', text='Title')
    self.tree.heading('Description', text='Description')
    self.tree.heading('Offered by', text='Offered by')
    self.tree.pack(pady=20)

    database_creation.cursor.execute(
        'SELECT title, description, username FROM tours JOIN users ON tours.offered_by=users.id')
    for tour in database_creation.cursor.fetchall():
        self.tree.insert("", "end", values=tour)


    # TODO command=admin_promt så slik ut tidligere "command=admin_promt()". Da kjørte koden hver gang man logget inn.
    Big = tk.Button(frame, command=admin_prompt, text="admin_tool", fg="#8B0000")
    Big.pack()

def offering_a_tour(self):
    title = simpledialog.askstring("Offer a Tour", "Enter tour title:")
    description = simpledialog.askstring(
        "Offer a Tour", "Give us your description:")

    database_creation.cursor.execute('SELECT id FROM users WHERE username=?',
                    (self.username,))
    user_id = database_creation.cursor.fetchone()[0]

    database_creation.cursor.execute('INSERT INTO tours (title, description, offered_by) VALUES (?, ?, ?)',
                    (title, description, user_id))
    database_creation.conn.commit()

    self.tree.insert("", "end", values=(title, description, self.username))
    messagebox.showinfo("Success", "Tour offered successfully.")

def deleting_a_tour(self):
    selected_tour = self.tree.selection()

    if not selected_tour:
        messagebox.showerror("Error", "No tour selected.")
        return

    confirm = messagebox.askyesno(
        "Delete Tour", "Are you sure you want to delete the selected tour?")
    if not confirm:
        return

    tour_title = self.tree.item(selected_tour)['values'][0]
    database_creation.cursor.execute("DELETE FROM tours WHERE title=?", (tour_title,))
    database_creation.conn.commit()

    self.tree.delete(selected_tour)
    messagebox.showinfo("Success", "Tour deleted successfully.")