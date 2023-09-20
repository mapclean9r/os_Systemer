import sqlite3
con = sqlite3.connect("guid.db")
cur = con.cursor()

test = cur.execute("SELECT ID FROM Person")

#Bruk denne når man skal logge inn 
#Finner ID til brukeren som er akkurat innlogget
def finne_id_bruker(bruker):
     id = cur.execute("SELECT ID FROM Bruker_konto WHERE BRUKERNAVN == (?)",bruker)
     return id

def finne_tur_id():
     pass

#Funksjon for å legge inn informasjon om personen (Kan bli mere info hvis noen har ideer)
def lag_person(fornavn,etternavn,age,):
    cur.execute("INSERT INTO Person(FORNAVN,ETTERNAVN,AGE) VALUES (?,?,?)",(fornavn,etternavn,age))
#    cur.execute("INSERT INTO kobling_person_Bruker(ID_Person) VALUES (?)", (test,))


#Funksjonen for å lage kontoer
def lag_brukerkonto(brukernavn, passord,email,isadmin):
    #Bruker = cur.execute("SELECT BRUKERNAVN FROM Bruker_konto WHERE (?)==",brukernavn)
    #allerede = Bruker.fetchall
    #if brukernavn in allerede:
    #    return ("Dette brukernavnet er allede i bruk")
    #else:
        cur.execute("INSERT INTO Bruker_konto(BRUKERNAVN,PASSORD,EMAIL,IS_admin) VALUES (?,?,?,?)",(brukernavn, passord,email,isadmin))

def kobling_bruker_person(bruker_id,person_id):#Putt inn tkinter bruker input i parantesen
    Navn_bruker = cur.execute("SELECT BRUKERNAVN FROM Bruker_konto WHERE BRUKERNAVN = (?)",())
    ID_bruker = cur.execute("SELECT ID FROM Bruker_konto WHERE Brukernavn = (?)",(bruker_id))
    ID_bruk = ID_bruker.fetchall()
    ID_person = cur.execute("SELECT ID FROM Person WHERE Brukernavn = (?)",(person_id))
    ID_pers = ID_person.fetchall()
    cur.execute("INSERT INTO kobling_person_Bruker(ID_Bruker,ID_Person) VALUES (?,?)",(ID_bruk,ID_pers))


def lag_tur_info(sted,navn,beskrivelse):
    cur.execute("INSERT INTO Tur_info(STED,NAVN,BESKRIVELSE)",(sted,navn,beskrivelse))

def email_henter(brukernavn):
     cur.execute("SELECT EMAIL FROM Bruker_konto WHERE ID == (?)", finne_id_bruker(brukernavn))

#Skal legge inn booking til profil
#def tur_kjøp(tur,bruker):
#     cur.execute("INSERT INTO Tur_booking(ID_tur,ID_Bruker) VALUES(?,?)",(  ,finne_id_bruker(bruker)))
    



#lag_brukerkonto("Tam","dan","FAKE@Fakis",1)
variabelnavn = "dummy"

res = cur.execute("SELECT BRUKERNAVN FROM Bruker_konto WHERE ID==(?)",finne_id_bruker(variabelnavn))#Variabelnavn skal bli byttet til hva variabelen som holder på brukeren sin brukernavn 
ID = res.fetchall()
for x in ID:
    print(x)


con.commit()
