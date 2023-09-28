import sqlite3
con = sqlite3.connect("guid.db")
cur = con.cursor()

def lag_person(fornavn,etternavn,age,):
    cur.execute("INSERT INTO Person(FORNAVN,ETTERNAVN,AGE) VALUES (?,?,?)",(fornavn,etternavn,age))
    con.commit()


con.close()