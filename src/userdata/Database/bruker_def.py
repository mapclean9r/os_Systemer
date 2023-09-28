import sqlite3
con = sqlite3.connect("guid.db")
cur = con.cursor()



def finne_id_bruker(bruker):
    cur.execute("SELECT ID FROM BrukerKonto WHERE Brukernavn = ?", (bruker,))
    result = cur.fetchone() 
    con.commit()
    return print(result)


def lag_brukerkonto(brukernavn, passord, email, isadmin):
    cur.execute("SELECT COUNT(*) FROM BrukerKonto WHERE EMail = ?", (email,))
    Email = cur.fetchone
    if Email > 0:
        return ("Emailen er allerede i bruk")
    #BYTT TILBAKE TIL BARE RETURN NÅR DET SKAL BLI BRUKT I GUI DETTE ER FOR Å SE DET TYDLIGERE 
    
    cur.execute("SELECT COUNT(*) FROM BrukerKonto WHERE Brukernavn = ?", (brukernavn,))
    bruker = cur.fetchone()
    
    if bruker > 0:
        return ("Dette brukernavnet er allerede i bruk")
    #BYTT TILBAKE TIL BARE RETURN NÅR DET SKAL BLI BRUKT I GUI
    
    cur.execute("INSERT INTO Bruker_konto(Brukernavn, Passord, E-Mail, Admin) VALUES (?, ?, ?, ?)", (brukernavn, passord, email, isadmin))
    con.commit()
    return print("Brukerkonto opprettet suksessfullt") 
    