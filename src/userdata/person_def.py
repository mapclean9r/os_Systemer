import sqlite3
con = sqlite3.connect("src/userdata/guide.db")
cur = con.cursor()

def lag_person(fornavn,etternavn,alder,):
    cur.execute("INSERT INTO Person(Fornavn,Etternavn,Alder) VALUES (?,?,?)",(fornavn,etternavn,alder))
    con.commit()


#con.close()
