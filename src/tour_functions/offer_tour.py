def offer_tour(self):
    title = simpledialog.askstring("Offer a Tour", "Enter tour title:")
    description = simpledialog.askstring(
        "Offer a Tour", "Enter tour description:")

    cursor.execute('SELECT id FROM users WHERE username=?', (self.username,))
    user_id = cursor.fetchone()[0]

    cursor.execute('INSERT INTO tours (title, description, offered_by) VALUES (?, ?, ?)',
                   (title, description, user_id))
    conn.commit()

    self.tree.insert("", "end", values=(title, description, self.username))
    messagebox.showinfo("Success", "Tour offered successfully.")
