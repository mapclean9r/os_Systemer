import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk


# Create the main application window
app = tk.Tk()
app.title("Bilde test")


# Function to open file through filedialog
def open_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png *.jpg *.jpeg *.gif *.bmp")])
    if file_path:
        img = Image.open(file_path)
        img.thumbnail((400, 400))  # Resize the image to fit in the window
        img = ImageTk.PhotoImage(img)
        image_label.config(image=img)
        image_label.image = img


# Create a button to open an image
open_button = tk.Button(app, text="Open Image", command=open_image)
open_button.pack(pady=10)


# Create a label to display the image
image_label = tk.Label(app)
image_label.pack()


# Tkinter main loop
app.mainloop()
