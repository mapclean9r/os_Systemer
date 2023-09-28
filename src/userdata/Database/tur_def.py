import sqlite3
con = sqlite3.connect("guid.db")
cur = con.cursor()


def lag_tur_info(land, sted, navn, beskrivelse):
    cur.execute("INSERT INTO Tur_info(Land, Sted, Beskrivelse, Andmeldelse) VALUES (?, ?, ?,?)", (land, sted, navn, beskrivelse))
    con.commit()

#se dokumentasjon på sql_lite
#https://www.youtube.com/watch?v=dQw4w9WgXcQ
def finne_tur_id():
     pass

#Skal legge inn booking til profil
#def tur_kjøp(tur,bruker):
#     cur.execute("INSERT INTO Tur_booking(ID_tur,ID_Bruker) VALUES(?,?)",(  ,finne_id_bruker(bruker)))
    