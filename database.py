import sqlite3
<<<<<<< Updated upstream
con = sqlite3.connect("Turguid.sql")
=======
con = sqlite3.connect("tutoria.sql")
>>>>>>> Stashed changes
cur = con.cursor()
cur.execute("CREATE TABLE movie(title, year, score)")
res = cur.execute("SELECT name FROM sqlite_master")
res.fetchone()
con.commit()
res = cur.execute("SELECT score FROM movie")
res.fetchall()
print(res) 
print("TEST")