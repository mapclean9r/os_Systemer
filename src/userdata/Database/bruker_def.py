import sqlite3
con = sqlite3.connect("guid.db")
cur = con.cursor()



def finne_id_bruker(bruker):
    cur.execute("SELECT ID FROM BrukerKonto WHERE Brukernavn = ?", (bruker,))
    result = cur.fetchone()
    con.commit()
    return print(result)


def lag_brukerkonto(brukernavn, passord, email, isadmin):
    cur.execute("SELECT EMail FROM BrukerKonto WHERE EMail = ?", (email,))
    Email = cur.fetchone
    if Email == email:
        return print("Emailen er allerede i bruk")
    #BYTT TILBAKE TIL BARE RETURN NÅR DET SKAL BLI BRUKT I GUI DETTE ER FOR Å SE DET TYDLIGERE

    cur.execute("SELECT COUNT(*) FROM BrukerKonto WHERE Brukernavn = ?", (brukernavn,))
    bruker = cur.fetchone()[0]

    if bruker > 0:
        return print("Dette brukernavnet er allerede i bruk")
    #BYTT TILBAKE TIL BARE RETURN NÅR DET SKAL BLI BRUKT I GUI

    cur.execute("INSERT INTO BrukerKonto(Brukernavn, Passord, EMail, Admin) VALUES (?, ?, ?, ?)", (brukernavn, passord, email, isadmin))
    con.commit()
    return print("Brukerkonto opprettet suksessfullt")

lag_brukerkonto("NEI", "JA", "SAMME", True)

con.close()
