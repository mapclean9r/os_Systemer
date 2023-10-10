import sqlite3
con = sqlite3.connect("src/userdata/guide.db")
cur = con.cursor()

from bruker_def import finne_id_bruker

def lag_tur_info(Title,Beskrivelse,TilbuddtAv,Land,Lokasjon,):
    cur.execute("INSERT INTO TurInfo(Titel, Beskrivelse, TilbudtAv, Land, Lokasjon) VALUES (?, ?, ?,?,?)", (Title, Beskrivelse, TilbuddtAv, Land,Lokasjon,))
    con.commit()

#se dokumentasjon på sql_lite
#https://www.youtube.com/watch?v=dQw4w9WgXcQ
def finne_tur_id():
     pass

#Skal legge inn booking til profil
def tur_kjøp(tur,bruker):
     cur.execute("INSERT INTO TurBooking(ID_tur, ID_Bruker) VALUES(?,?)",(tur,finne_id_bruker(bruker)))

def vise_turinfo(tur_id):
     cur.execute("SELECT Land, Sted, Beskrivelse, Anmelding FROM TurInfo WHERE ID = ?",(tur_id,))
     tur = cur.fetchone
     return tur
     