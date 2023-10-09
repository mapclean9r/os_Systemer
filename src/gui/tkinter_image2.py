import tkinter as tk
from tkinter import filedialog
import sqlite3
from PIL import Image, ImageTk
import io


class TourGuideApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Tour Guide Application")
        self.geometry("400x400")

        # Create a container to hold the pages
        self.page_container = tk.Frame(self)
        self.page_container.pack(fill="both", expand=True)

        # Create a dictionary to hold pages
        self.pages = {}

        # Create the page for selecting pages
        self.create_page("Select Page", StartPage)
        self.create_page("Add Image", AddImagePage)

        self.show_page("Select Page")

        # Initialize the SQLite database
        self.db_connection = sqlite3.connect("tour_guide.db")
        self.create_table_if_not_exists()


    def create_page(self, name, page_class):
        page = page_class(self.page_container, self)
        self.pages[name] = page
        page.grid(row=0, column=0, sticky="nsew")

    def show_page(self, name):
        page = self.pages[name]
        page.tkraise()


class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        label = tk.Label(self, text="Welcome to the Tour Guide App", font=("Helvetica", 16))
        label.pack(pady=20)

        button1 = tk.Button(self, text="Add Image", command=lambda: controller.show_page("Add Image"))
        button1.pack()


class AddImagePage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        label = tk.Label(self, text="Add Image to Tour Guide", font=("Helvetica", 16))
        label.pack(pady=20)

        self.image_label = tk.Label(self, text="No Image Selected")
        self.image_label.pack()

        browse_button = tk.Button(self, text="Browse", command=self.open_file)
        browse_button.pack()

        back_button = tk.Button(self, text="Back", command=lambda: controller.show_page("Select Page"))
        back_button.pack()


    def open_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png *.jpg *.jpeg *.gif *.bmp")])

        if file_path:
            image = Image.open(file_path)
            image.thumbnail((200, 200))  # Resize image to fit label
            photo = ImageTk.PhotoImage(image)

            self.image_label.config(image=photo, text="")
            self.image_label.photo = photo


if __name__ == "__main__":
    app = TourGuideApp()
    app.mainloop()
