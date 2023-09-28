import sqlite3
con = sqlite3.connect("guid.db")
cur = con.cursor()


def lag_tur_info(sted, navn, beskrivelse):
    cur.execute("INSERT INTO Tur_info(STED, NAVN, BESKRIVELSE) VALUES (?, ?, ?)", (sted, navn, beskrivelse))
    con.commit


def finne_tur_id():
     pass

#Skal legge inn booking til profil
#def tur_kjøp(tur,bruker):
#     cur.execute("INSERT INTO Tur_booking(ID_tur,ID_Bruker) VALUES(?,?)",(  ,finne_id_bruker(bruker)))
    