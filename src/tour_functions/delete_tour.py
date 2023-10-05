def delete_tour(self):
    selected_tour = self.tree.selection()

    if not selected_tour:
        messagebox.showerror("Error", "No tour selected.")
        return

    confirm = messagebox.askyesno(
        "Delete Tour", "Are you sure you want to delete the selected tour?")
    if not confirm:
        return
    tour_title = self.tree.item(selected_tour)['values'][0]
    cursor.execute("DELETE FROM tours WHERE title=?", (tour_title,))
    conn.commit()

    self.tree.delete(selected_tour)
    messagebox.showinfo("Success", "Tour deleted successfully.")
