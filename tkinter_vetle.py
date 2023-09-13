import tkinter as tk
from tkinter import ttk


root = tk.Tk()
root.title("basic GUI app")


# lables
label = tk.Label(root, text="Vetle tkinter app")


# buttons
button = tk.Button(root, text="Knapp")


label.pack()
button.pack()


root.mainloop()