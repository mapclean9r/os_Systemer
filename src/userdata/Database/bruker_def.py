import sqlite3
con = sqlite3.connect("guid.db")
cur = con.cursor()



def finne_id_bruker(bruker):
    cur.execute("SELECT ID FROM Bruker_konto WHERE BRUKERNAVN = ?", (bruker,))
    result = cur.fetchone() 
    con.commit()
    return print(result)


def lag_brukerkonto(brukernavn, passord, email, isadmin):
    cur.execute("SELECT COUNT(*) FROM Bruker_konto WHERE BRUKERNAVN = ?", (brukernavn,))
    bruker = cur.fetchone()[0]
    
    if bruker > 0:
        return "Dette brukernavnet er allerede i bruk"
    
    cur.execute("INSERT INTO Bruker_konto(BRUKERNAVN, PASSORD, EMAIL, IS_admin) VALUES (?, ?, ?, ?)", (brukernavn, passord, email, isadmin))
    con.commit()
    return "Brukerkonto opprettet suksessfullt" 
    