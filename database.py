import sqlite3
con = sqlite3.connect("tutorial.sql")
cur = con.cursor()
cur.execute("CREATE TABLE movie(title, year, score)")
res = cur.execute("SELECT name FROM sqlite_master")
res.fetchone()
con.commit()
res = cur.execute("SELECT score FROM movie")
res.fetchall()
    