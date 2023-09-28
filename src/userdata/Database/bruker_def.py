import sqlite3
con = sqlite3.connect("guid.db")
cur = con.cursor()



def finne_id_bruker(bruker):
    cur.execute("SELECT ID FROM BrukerKonto WHERE Brukernavn = ?", (bruker,))
    result = cur.fetchone() 
    con.commit()
    return print(result)


def lag_brukerkonto(brukernavn, passord, email, isadmin):
    cur.execute("SELECT COUNT(*) FROM BrukerKonto WHERE Brukernavn = ?", (brukernavn,))
    bruker = cur.fetchone()
    
    if bruker > 0:
        return ("Dette brukernavnet er allerede i bruk")
    
    cur.execute("INSERT INTO Bruker_konto(Brukernavn, Passord, E-Mail, Admin) VALUES (?, ?, ?, ?)", (brukernavn, passord, email, isadmin))
    con.commit()
    return print("Brukerkonto opprettet suksessfullt") 
    