import sqlite3
con = sqlite3.connect("guid.db")
cur = con.cursor()


#Bruk denne når man skal logge inn 
#Finner ID til brukeren som er akkurat innlogget
def finne_id_bruker(bruker):
    cur.execute("SELECT ID FROM Bruker_konto WHERE BRUKERNAVN = ?", (bruker,))
    result = cur.fetchone() 
    con.commit
    return print(result)

    


def finne_tur_id():
     pass

#Funksjon for å legge inn informasjon om personen (Kan bli mere info hvis noen har ideer)
def lag_person(fornavn,etternavn,age,):
    cur.execute("INSERT INTO Person(FORNAVN,ETTERNAVN,AGE) VALUES (?,?,?)",(fornavn,etternavn,age))
    con.commit




#Funksjonen for å lage kontoer
def lag_brukerkonto(brukernavn, passord, email, isadmin):
    cur.execute("SELECT COUNT(*) FROM Bruker_konto WHERE BRUKERNAVN = ?", (brukernavn,))
    bruker = cur.fetchone()[0]
    
    if bruker > 0:
        return "Dette brukernavnet er allerede i bruk"
    
    
    cur.execute("INSERT INTO Bruker_konto(BRUKERNAVN, PASSORD, EMAIL, IS_admin) VALUES (?, ?, ?, ?)", (brukernavn, passord, email, isadmin))
    #return "Brukerkonto opprettet suksessfullt" 
    print("1")
    con.commit()
    print("2")
    print("3")




    

def kobling_bruker_person(bruker_id, person_id):
    ID_bruker = cur.execute("SELECT ID FROM Bruker_konto WHERE Brukernavn = ?", (bruker_id,))
    ID_person = cur.execute("SELECT ID FROM Person WHERE Brukernavn = ?", (person_id,))
    ID_bruk = ID_bruker.fetchone()
    ID_pers = ID_person.fetchone()
    if ID_bruk and ID_pers:
        cur.execute("INSERT INTO kobling_person_Bruker(ID_Bruker, ID_Person) VALUES (?, ?)", (ID_bruk[0], ID_pers[0]))
    else:
        print("User or person not found.")
    con.commit


def lag_tur_info(sted, navn, beskrivelse):
    cur.execute("INSERT INTO Tur_info(STED, NAVN, BESKRIVELSE) VALUES (?, ?, ?)", (sted, navn, beskrivelse))
    con.commit

def email_henter(brukernavn):
    cur.execute("SELECT EMAIL FROM Bruker_konto WHERE ID == (?)", finne_id_bruker(brukernavn))
    con.commit

#Skal legge inn booking til profil
#def tur_kjøp(tur,bruker):
#     cur.execute("INSERT INTO Tur_booking(ID_tur,ID_Bruker) VALUES(?,?)",(  ,finne_id_bruker(bruker)))
    



lag_brukerkonto("FFFF","TEST","FAKE@Fakis",1)
variabelnavn = "Tam"

#Variabelnavn skal bli byttet til hva variabelen som holder på brukeren sin brukernavn
# res = cur.execute("SELECT ? FROM Bruker_konto", (str(finne_id_bruker(variabelnavn)),))
# ID = res.fetchone()
# print(ID)


con.close


