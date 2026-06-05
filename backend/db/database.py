import sqlite3

#connect database
conn = sqlite3.connect('marketplace.db')
cursor = conn.cursor()

#create table
cursor.execute("""
                CREATE TABLE IF NOT EXISTS listings
                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                description TEXT NOT NULL,
                price REAL NOT NULL)
               """);

#commit changes and close connection
conn.commit()

res = cursor.execute("SELECT * FROM sqlite_master")
print(res.fetchone())

conn.close()