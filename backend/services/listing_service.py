def create_listing(db, title: str, description: str, price: float, category: str):
    db.execute("INSERT INTO listings (title, description, price, category) VALUES (?, ?, ?, ?)", (title, description, price, category))
    listing_id =db.execute("SELECT last_insert_rowid()").fetchone()[0]
    return listing_id
