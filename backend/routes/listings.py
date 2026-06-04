from fastapi import APIRouter
router = APIRouter()

@router.post("/listings")
async def create_listing(title: str, description:str, price: float):
    return {"listing": {"title": title, "description": description, "price": price}}

@router.get("/listings")
async def get_listings():
    return {"listings": [
        {"id": 1, "title": "Sample Listing", "description": "This is a sample listing", "price": 9.99}
    ]}
