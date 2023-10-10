import os
import sqlite3
pathing = os.path.dirname(__file__) + "/guide.db"
con = sqlite3.connect(pathing)
cur = con.cursor()

cur.execute("""CREATE TABLE Person(
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            Fornavn TEXT NOT NULL, 
            Etternavn TEXT NOT NULL,
            Alder INT NOT NULL)"""
            )
cur.execute("""CREATE TABLE BrukerKonto(
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            Brukernavn TEXT NOT NULL,
            Passord TEXT NOT NULL,
            Admin BOOLEAN NOT NULL)"""
            )
cur.execute("""CREATE TABLE TurInfo(
            ID INTEGER PRIMARY KEY AUTOINCREMENT,Title,Beskrivelse,TilbuddtAv,Land,Lokasjon
            Titel TEXT,
            Beskrivelse TEXT,
            TilbudtAv TEXT,
            Land TEXT,
            Lokasjon TEXT)""")
cur.execute("""CREATE TABLE TurBooking(
            Dato DATE PRIMARY KEY,
            ID_tur INTEGER,
            ID_Bruker INTEGER)"""
            )
cur.execute("""CREATE TABLE KoblingPersonBruker(
            ID_Person INTEGER,
            ID_Bruker INTEGER)"""
)
