from fastapi import APIRouter, Depends
from db.database import get_db
router = APIRouter()


#returns all listings in the database
@router.get("/listings")
async def get_listings(db = Depends(get_db)):
    listings = db.execute("SELECT * FROM listings")
    listings = listings.fetchall()
    return listings
