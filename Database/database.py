import sqlite3
con = sqlite3.connect("guid.db")
cur = con.cursor()


def lag_person(fornavn,etternavn,age,):
    cur.execute("INSERT INTO Person(FORNAVN,ETTERNAVN,AGE) VALUES (?,?,?)",(fornavn,etternavn,age))



def lag_brukerkonto(brukernavn, passord):
    Bruker = cur.execute("SELECT BRUKERNAVN FROM Bruker_konto")
    allerede = Bruker.fetchall
    if brukernavn in allerede:
        return ("Dette brukernavnet er allede i bruk")
    else:
        cur.execute("INSERT INTO Bruker_konto(BRUKERNAVN,PASSORD) VALUES (?,?)",(brukernavn, passord))

def kobling_bruker_person(bruker_id,person_id):#Putt inn tkinter bruker input i parantesen
    Navn_bruker = cur.execute("SELECT BRUKERNAVN FROM Bruker_konto WHERE BRUKERNAVN = (?)",())
    ID_bruker = cur.execute("SELECT ID FROM Bruker_konto WHERE Brukernavn = (?)",(bruker_id))
    ID_bruk = ID_bruker.fetchall()
    ID_person = cur.execute("SELECT ID FROM Person WHERE Brukernavn = (?)",(person_id))
    ID_pers = ID_person.fetchall()
    cur.execute("INSERT INTO kobling_person_Bruker(ID_Bruker,ID_Person) VALUES (?,?)",ID_bruk,ID_pers)


def lag_tur_info(sted,navn,beskrivelse):
    cur.execute("INSERT INTO Tur_info(STED,NAVN,BESKRIVELSE)",(sted,navn,beskrivelse))

def konto_kobling():
    lag_brukerkonto("admin","admin")
    lag_person("test","lest",53)
    kobling_bruker_person()


res = cur.execute("SELECT ID FROM Bruker_konto")
ID = res.fetchall()
for x in ID:
    print(x)


con.commit()


res = cur.execute("SELECT etternavn FROM Person")
res.fetchall()
for row in cur.execute("SELECT fornavn, etternavn FROM Person"):
    print(row)

