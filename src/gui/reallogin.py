import tkinter

def start_program():
    root = tkinter.Tk()
    root.title("Autentication window")
    root.geometry("1000x800")
    custom_color = "#212121"
    custom_color2 = "#3d3d3d"
    root.configure(bg=custom_color)


    #login
    login_button = tkinter.Button(root, text="Login", highlightthickness=2)
    login_button.place(x=480, y=500)

    username_label = tkinter.Label(root, text=f"Logged in as: ", fg="white")
    username_label.place(x=450, y=50)

    #tekstfelt login username
    username_input = tkinter.Entry(root)
    username_input.place(x=450, y=150)

    password_input = tkinter.Label(root, text="Registrering")

    #register
    register_button = tkinter.Button(root, text="Create an account", highlightthickness=2)
    register_button.place(x=450, y=180)



    root.mainloop()


if __name__ == '__main__':
    start_program()
