import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk



class page_logic(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
    def show(self):
        self.lift()


class page_1(page_logic):
    def __init__(self, *args, **kwargs):
        page_logic.__init__(self, *args, **kwargs)
        label = tk.Label(self, text="Page 1 nav test")
        label.pack(side="top", fill="both", expand=True)


class page_2(page_logic):
    def __init__(self, *args, **kwargs):
        page_logic.__init__(self, *args, **kwargs)
        label = tk.Label(self, text="Page 2 nav test")
        label.pack(side="top", fill="both", expand=True)


class page_3(page_logic):
    def __init__(self, *args, **kwargs):
        page_logic.__init__(self, *args, **kwargs)
        label = tk.Label(self, text="Page 3 nav test")
        label.pack(side="top", fill="both", expand=True)


class page_4_image(page_logic):
    def __init__(self, *args, **kwargs):
        page_logic.__init__(self, *args, **kwargs)
        label = tk.Label(self, text="Page 3 nav test")

        # Function to open file through filedialog
        def open_image():
            file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png *.jpg *.jpeg *.gif *.bmp")])
            if file_path:
                img = Image.open(file_path)
                img.thumbnail((400, 400))
                img = ImageTk.PhotoImage(img)
                image_label.config(image=img)
                image_label.image = img


        # Button to open an image
        open_button = tk.Button(app, text="Open Image", command=open_image)
        open_button.pack(pady=10)


        # Label to display the image
        image_label = tk.Label(app)
        image_label.pack()

        label.pack(side="top", fill="both", expand=True)



class main_page(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        p1 = page_1(self)
        p2 = page_2(self)
        p3 = page_3(self)
        p4 = page_4_image(self)


        button = tk.Frame(self)
        container = tk.Frame(self)
        button.pack(side="top", fill="both", expand=False)
        container.pack(side="top", fill="both", expand=True)


        p1.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p2.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p3.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p4.place(in_=container, x=0, y=0, relwidth=1, relheight=1)


        b1 = tk.Button(button, text="To page 1", command=p1.show)
        b2 = tk.Button(button, text="To page 2", command=p2.show)
        b3 = tk.Button(button, text="To page 3", command=p3.show)
        b4 = tk.Button(button, text="To page 4", command=p4.show)


        b1.pack(side="left")
        b2.pack(side="left")
        b3.pack(side="left")
        b4.pack(side="left")


        p1.show()


if __name__ == "__main__":
    app = tk.Tk()
    main = main_page(app)
    main.pack(side="top", fill="both", expand=True)
    app.wm_geometry("500x500")
    app.mainloop()