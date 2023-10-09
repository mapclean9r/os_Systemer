import sqlite3

con = sqlite3.connect("src/userdata/guide.db")
cur = con.cursor()


def finne_id_bruker(bruker):
    cur.execute("SELECT ID FROM BrukerKonto WHERE Brukernavn = ?", (bruker,))
    result = cur.fetchone()
    con.commit()
    return print(result)


def finne_brukernavn_id(id):
    cur.execute("SELECT Brukernavn FROM BrukerKonto WHERE ID = ?", (id,))
    result = cur.fetchone()
    return result


def lag_brukerkonto(brukernavn, passord, email, isadmin):
    cur.execute("SELECT COUNT(*) FROM BrukerKonto WHERE EMail = ?", (email,))
    Email = cur.fetchone()[0]
    # if Email > email:
    #     return print("Emailen er allerede i bruk")
    # #BYTT TILBAKE TIL BARE RETURN NÅR DET SKAL BLI BRUKT I GUI DETTE ER FOR Å SE DET TYDLIGERE 
    # FIKS TIL SENERE FOR FUNGERER IKKE

    cur.execute("SELECT COUNT(*) FROM BrukerKonto WHERE Brukernavn = ?", (brukernavn,))
    bruker = cur.fetchone()[0]

    if bruker > 0:
        return print("Dette brukernavnet er allerede i bruk")
    # BYTT TILBAKE TIL BARE RETURN NÅR DET SKAL BLI BRUKT I GUI
    # FUNGERER MAGISK

    cur.execute("INSERT INTO BrukerKonto(Brukernavn, Passord, EMail, Admin) VALUES (?, ?, ?, ?)",
                (brukernavn, passord, email, isadmin))
    con.commit()
    return print("Brukerkonto opprettet suksessfullt")


def brukernavn_get(brukernavn):
    cur.execute("SELECT Brukernavn FROM BrukerKonto WHERE Brukernavn = ?", (brukernavn,))
    brukernav = cur.fetchone()
    return brukernav

def passord_get(brukernavn):
    cur.execute("SELECT Passord FROM BrukerKonto WHERE Brukernavn = ?",(brukernavn,))
    passo = cur.fetchone()
    return passo


#Skal kanskje fungere
def passord_endre(Brukernavn,passord):#Skal få det til å være sikkrere hvis jeg har tid
    # cur.execute("SELECT ID FROM BrukerKonto WHERE Brukernavn = ?",(Brukernavn,))
    # bruker_id = cur.fetchone
    cur.execute("UPDATE Brukerkonto SET Passord=? WHERE Brukernavn = ?",(passord,Brukernavn,))
    con.commit()

def email_endre(brukernavn, email):
    cur.execute("UPDATE Brukerkonto SET EMail=? WHERE Brukernavn = ?",(email,brukernavn,))
    con.commit()
    return print("VEllyket")

#Endre navnet på kontoen og sjekekr om det er allerede tatt
def brukernavn_endre(Brukernavn,Bruker):
    cur.execute("SELECT COUNT(*) FROM BrukerKonto WHERE Brukernavn = ?", (Bruker,))
    bruker = cur.fetchone()[0]
    
    if bruker > 0:
        return print("Dette brukernavnet er allerede i bruk")
    else:
        cur.execute("UPDATE Brukerkonto SET Brukernavn=? WHERE Brukernavn = ?",(Brukernavn,Bruker,))
        con.commit()

    


def is_admin(Brukernavn):
    cur.execute("SELECT Brukernavn,Admin FROM BrukerKonto WHERE Brukernavn = ?",(Brukernavn,))
    admin = cur.fetchone()
    return admin


    
con.close
