import tkinter
import sys

from src.userdata.bruker_def import get_all_brukernavn

sys.path.append('src')

def dummy():
    print("dummy")


def getuser():
    x = "Horse"
    return x


def admin_prompt():
    root = tkinter.Tk()
    root.title("Admin Tool")
    root.geometry("400x300")
    custom_color = "#212121"
    custom_color2 = "#3d3d3d"
    root.configure(bg=custom_color)

    username_login = tkinter.Label(root, text=f"Logged in as: {getuser()}", fg="white")
    username_login.configure(bg=custom_color)
    username_login.place(x=0, y=0)

    # user list

    list_users = tkinter.Label(root, text="All Users:", fg="white")
    list_users.configure(bg=custom_color)
    list_users.place(x=250, y=20)

    listbox = tkinter.Listbox(root, fg="white", bg=custom_color, borderwidth=0, highlightthickness=1)
    listbox.configure(bg=custom_color)
    listbox.place(x=250, y=50)

    # commands

    commands_cat = tkinter.Label(root, text="Actons:", fg="white")
    commands_cat.configure(bg=custom_color)
    commands_cat.place(x=100, y=60)

    ban_button = tkinter.Button(root, text="Ban User", fg="white", bg=custom_color2, highlightthickness=2)
    ban_button.place(x=100, y=100)

    log_button = tkinter.Button(root, text="User logs", fg="white", bg=custom_color2, highlightthickness=2)
    log_button.place(x=100, y=140)


    all_users_list = get_all_brukernavn()

    brukernr = 0
    for all_names in all_users_list:
        listbox.insert(brukernr, all_names)
        brukernr = brukernr+1

    listbox.insert(0, "Turelsker Karl")
    listbox.insert(1, "Hest")
    listbox.insert(2, "Elg")
    listbox.insert(3, "oste enjoyer")

    root.mainloop()


if __name__ == '__main__':
    admin_prompt()
