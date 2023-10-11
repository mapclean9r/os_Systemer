import tkinter as tk
from gui.homepage import clear_page

vindu = tk.Tk()
vindu.title("login")
vindu.geometry('1250x750')

# widgets:
label_login = tk.Label(vindu, text="Login")
label_brukernavn = tk.Label(vindu, text="brukernavn")
inputfelt_brukernavn = tk.Entry(vindu)
inputfelt_passord = tk.Entry(vindu, show="*")
label_passord = tk.Label(vindu, text="Passord")
login_knapp = tk.Button(vindu, text="Login", command=clear_page)

label_login.grid(row=0, column=0, columnspan=2)
label_brukernavn.grid(row=1, column=0)
inputfelt_brukernavn.grid(row=1, column=1)
label_passord.grid(row=2, column=0)
inputfelt_passord.grid(row=2, column=1)
login_knapp.grid(row=3, column=1)


vindu.mainloop()
