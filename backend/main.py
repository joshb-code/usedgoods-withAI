from fastapi import FastAPI
from db.database import init_db
from routes import listings, upload

app  = FastAPI(title = "Ai Marketplace")
init_db()

app.include_router(listings.router, prefix="/listings")
app.include_router(upload.router, prefix="/upload")


@app.get("/")
async def root():
    return {"message": "Hello World"}

