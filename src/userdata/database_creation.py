import os
import sqlite3
pathing = os.path.dirname(__file__) + "/guide.db"


# database Setup
conn = sqlite3.connect(pathing)
cursor = conn.cursor()


def create_database():
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        username TEXT UNIQUE,
        password TEXT
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS tours (
        id INTEGER PRIMARY KEY,
        title TEXT,
        description TEXT,
        offered_by INTEGER,
        FOREIGN KEY(offered_by) REFERENCES users(id)
    )
    ''')
    conn.commit()
