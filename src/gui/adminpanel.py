import tkinter

def dummy():
    print("dummy")

def getuser():
    x = "Horse"
    return x

def admin_prompt():
    root = tkinter.Tk()
    root.title("Admin Panel")
    root.geometry("800x600")
    custom_color = "#212121"
    root.configure(bg=custom_color)

    username_label = tkinter.Label(root, text=f"Logged in as: {getuser()}", fg="white")
    username_label.pack()
    username_label.configure(bg=custom_color)
    username_label.grid(row=0, column=1)





    root.mainloop()

if __name__ == '__main__':
    admin_prompt()
