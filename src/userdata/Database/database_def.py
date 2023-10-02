import sqlite3

con = sqlite3.connect("guid.db")
cur = con.cursor()




def kobling_bruker_person(Brukernavn, Person_navn):
    ID_bruker = cur.execute("SELECT ID FROM BrukerKonto WHERE Brukernavn = ?", (Brukernavn,))
    ID_person = cur.execute("SELECT ID FROM Person WHERE Fornavn = ?", (Person_navn,))
    ID_bruk = ID_bruker.fetchone()
    ID_pers = ID_person.fetchone()
    if ID_bruk and ID_pers:
        cur.execute("INSERT INTO KoblingPersonBruker(ID_Bruker, ID_Person) VALUES (?, ?)", (ID_bruk[0], ID_pers[0]))
    else:
        print("User or person not found.")
    con.commit()







#lag_brukerkonto("FFFF","TEST","FAKE@Fakis",1)
variabelnavn = "Tam"

#Variabelnavn skal bli byttet til hva variabelen som holder på brukeren sin brukernavn
# res = cur.execute("SELECT ? FROM Bruker_konto", (str(finne_id_bruker(variabelnavn)),))
# ID = res.fetchone()
# print(ID)


#con.close()


