import sqlite3
con = sqlite3.connect("guid.db")
cur = con.cursor()
cur.execute("""CREATE TABLE Person(
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            Fornavn TEXT NOT NULL, 
            Etternavn TEXT NOT NULL,
            Alder INT NOT NULL)"""
            )
cur.execute("""CREATE TABLE Bruker_konto(
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            Brukernavn TEXT NOT NULL,
            Passord TEXT NOT NULL,
            E-Mail TEXT,
            Admin BOOLEAN NOT NULL)"""
            )
cur.execute("""CREATE TABLE Tur_info(
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            Land TEXT,
            Sted TEXT NOT NULL,
            Navn TEXT,
            Beskrivelse TEXT,
            Anmelding TEXT)""")
cur.execute("""CREATE TABLE Tur_booking(
            Dato DATE PRIMARY KEY,
            ID_tur INTEGER,
            ID_Bruker INTEGER)"""
            )
cur.execute("""CREATE TABLE kobling_person_Bruker(
            ID_Person INTEGER,
            ID_Bruker INTEGER)"""
)
