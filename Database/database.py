import sqlite3
con = sqlite3.connect("guid.db")
cur = con.cursor()


def lag_bruker(fornavn,etternavn,age,):
    cur.execute("INSERT INTO Person(FORNAVN,ETTERNAVN,AGE) VALUES (?,?,?)",(fornavn,etternavn,age))

lag_bruker("test","lest",50)


con.commit()

res = cur.execute("SELECT etternavn FROM Person")
res.fetchall()
for row in cur.execute("SELECT fornavn, etternavn FROM movie2"):
    print(row)

