from fastapi import APIRouter, Depends
from db.database import get_db
router = APIRouter()

@router.post("/listings")
async def create_listing(title: str, description:str, price: float, db = Depends(get_db)):
    db.execute("INSERT INTO listings (title, description, price) VALUES (?, ?, ?)", (title, description, price))
    return db.execute("SELECT last_insert_rowid()").fetchone()[0]

#returns all listings in the database
@router.get("/listings")
async def get_listings(db = Depends(get_db)):
    db.execute("SELECT * FROM listings")
    listings = db.fetchall()
    return listings
