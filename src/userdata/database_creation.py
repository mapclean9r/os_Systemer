import sqlite3

# database Setup
conn = sqlite3.connect('src/database/tour_marketplace.db')
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
