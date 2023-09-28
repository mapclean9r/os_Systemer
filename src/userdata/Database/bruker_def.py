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
    Email = cur.fetchone()[0]
    # if Email > email:
    #     return print("Emailen er allerede i bruk")
    # #BYTT TILBAKE TIL BARE RETURN NÅR DET SKAL BLI BRUKT I GUI DETTE ER FOR Å SE DET TYDLIGERE 
    #FIKS TIL SENERE FOR FUNGERER IKKE

    cur.execute("SELECT COUNT(*) FROM BrukerKonto WHERE Brukernavn = ?", (brukernavn,))
    bruker = cur.fetchone()[0]
    
    if bruker > 0:
        return print("Dette brukernavnet er allerede i bruk")
    #BYTT TILBAKE TIL BARE RETURN NÅR DET SKAL BLI BRUKT I GUI
    #FUNGERER MAGISK 
    
    cur.execute("INSERT INTO BrukerKonto(Brukernavn, Passord, EMail, Admin) VALUES (?, ?, ?, ?)", (brukernavn, passord, email, isadmin))
    con.commit()
    return print("Brukerkonto opprettet suksessfullt")

def brukernavn_get(brukernavn):
    cur.execute("SELECT Brukernavn FROM BrukerKonto WHERE Brukernavn = ?",(brukernavn,))
    brukernav = cur.fetchone()
    return brukernav

def passord_get(passord):
    cur.execute("SELECT Passord FROM BrukerKonto WHERE Passord = ?",(passord,))
    passo = cur.fetchone()
    return passo


lag_brukerkonto("DAS","NO","TEST",0) 
    
con.close