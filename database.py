import sqlite3
con = sqlite3.connect("tutorial.sql")
cur = con.cursor()
#cur.execute("CREATE TABLE movie(title, year, score)")
res = cur.execute("SELECT name FROM sqlite_master")
res.fetchone()
con.commit()
res = cur.execute("SELECT name FROM sqlite_master")
res.fetchone()
res = cur.execute("SELECT name FROM sqlite_master WHERE name='spam'")
res.fetchone() is None
cur.execute("""
    INSERT INTO movie VALUES
        ('Monty Python and the Holy Grail', 1975, 8.2),
        ('And Now for Something Completely Different', 1971, 7.5)
""")
con.commit()
res = cur.execute("SELECT score FROM movie")
res.fetchall()
for row in cur.execute("SELECT year, title FROM movie ORDER BY year"):
    print(row)

res = cur.execute("SELECT year,title FROM movie")
title, year = res.fetchone()
print(f'The highest scoring Monty Python movie is {title!r}, released in {year}')
    