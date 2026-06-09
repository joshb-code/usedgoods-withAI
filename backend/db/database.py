import sqlite3

def get_db():
    #connect database
    conn = sqlite3.connect('marketplace.db', check_same_thread=False)
    cursor = conn.cursor()
    
    yield cursor
    conn.commit()
    conn.close()

def init_db():
    conn = sqlite3.connect('marketplace.db', check_same_thread=False)
    cursor = conn.cursor()
    
    #create listings table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS listings (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT NOT NULL,
            price REAL NOT NULL,
            category TEXT NOT NULL
        )
    ''')

    #table with all the listing images
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS images (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            listing_id INTEGER,
            image_data BLOB,
            FOREIGN KEY (listing_id) REFERENCES listings (id)
        )
    ''')
    
    conn.commit()
    conn.close()