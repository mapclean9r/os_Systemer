import tkinter as tk
from tkinter import filedialog
import sqlite3
import os
from PIL import Image, ImageTk
import io

pathing = os.path.dirname(__file__) + "/guide.db"

con = sqlite3.connect(pathing)
cursor = con.cursor()


# Fungerer men bruker egen database i samme directory


class TourGuideApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Tour Guide Application")
        self.geometry("600x600")

        userdata_directory = os.path.join(os.path.expanduser("~"), "userdata")
        db_path = os.path.join(userdata_directory, "guide.db")


        self.page_container = tk.Frame(self)
        self.page_container.pack(fill="both", expand=True)

        self.pages = {}

        self.db_connection = sqlite3.connect(pathing)
        self.create_table_if_not_exists()

        self.create_page("Select Page", StartPage)
        self.create_page("Add Image", AddImagePage)

        self.show_page("Select Page")


    def create_table_if_not_exists(self):
        cursor = self.db_connection.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS images (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                image_data BLOB
            )
        """)
        self.db_connection.commit()


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

        self.display_images(controller)

    def display_images(self, controller):
        cursor = controller.db_connection.cursor()
        cursor.execute("SELECT id, image_data FROM images")
        images = cursor.fetchall()

        if images:
            for idx, (image_id, image_data) in enumerate(images):
                image = Image.open(io.BytesIO(image_data))
                image.thumbnail((100, 100))
                photo = ImageTk.PhotoImage(image)

                image_label = tk.Label(self, image=photo)
                image_label.photo = photo
                image_label.pack(side="left", padx=10, pady=10)

                remove_button = tk.Button(self, text="Remove",
                                          command=lambda id=image_id: self.remove_image(controller, id))
                remove_button.pack(side="left")

    def remove_image(self, controller, image_id):
        cursor = controller.db_connection.cursor()
        cursor.execute("DELETE FROM images WHERE id=?", (image_id,))
        controller.db_connection.commit()

        self.destroy()
        self.__init__(self.master, controller)


class AddImagePage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

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
            image.thumbnail((200, 200))
            photo = ImageTk.PhotoImage(image)

            self.image_label.config(image=photo, text="")
            self.image_label.photo = photo

            image_data = io.BytesIO()
            image.save(image_data, format="PNG")
            image_data = image_data.getvalue()

            cursor = self.controller.db_connection.cursor()
            cursor.execute("INSERT INTO images (image_data) VALUES (?)", (sqlite3.Binary(image_data),))
            self.controller.db_connection.commit()


if __name__ == "__main__":
    app = TourGuideApp()
    app.mainloop()
