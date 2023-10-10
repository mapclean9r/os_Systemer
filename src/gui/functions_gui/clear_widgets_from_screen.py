
def clear_all_widgets(self):
    for widget in self.winfo_children():
        widget.destroy()
