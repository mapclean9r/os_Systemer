from src.userdata.tur_def import *
from src.userdata.bruker_def import *
from src.userdata.person_def import *

con = sqlite3.connect("guid.db")
cur = con.cursor()




def kobling_bruker_person(bruker_id, person_id):
    ID_bruker = cur.execute("SELECT ID FROM Bruker_konto WHERE Brukernavn = ?", (bruker_id,))
    ID_person = cur.execute("SELECT ID FROM Person WHERE Brukernavn = ?", (person_id,))
    ID_bruk = ID_bruker.fetchone()
    ID_pers = ID_person.fetchone()
    if ID_bruk and ID_pers:
        cur.execute("INSERT INTO kobling_person_Bruker(ID_Bruker, ID_Person) VALUES (?, ?)", (ID_bruk[0], ID_pers[0]))
    else:
        print("User or person not found.")
    con.commit()







#lag_brukerkonto("FFFF","TEST","FAKE@Fakis",1)
variabelnavn = "Tam"

#Variabelnavn skal bli byttet til hva variabelen som holder på brukeren sin brukernavn
# res = cur.execute("SELECT ? FROM Bruker_konto", (str(finne_id_bruker(variabelnavn)),))
# ID = res.fetchone()
# print(ID)


con.close()


