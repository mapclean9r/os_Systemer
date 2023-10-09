'''
import tkinter as tk
from tkinter import *


root = tk.Tk()
root.title("basic GUI app")


# canvas
canvas = tk.Canvas(root, width=800, height=600)
canvas.pack()


# images

# image = tk.PhotoImage(file="C:/Users/save4/Pictures/IMG_1539.jpg")


# image placement
# canvas.create_image(150, 150, image=image)


# lables
label = tk.Label(root, text="Vetle tkinter app")
label = tk.Label(root, image=image)
label.pack()


# buttons
button = tk.Button(root, text="Knapp")
button.pack()


root.mainloop()
'''
