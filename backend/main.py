from fastapi import FastAPI
from backend.routes import listings, upload

app  = FastAPI(title = "Ai Marketplace")

app.include_router(listings.router, prefix="/listings")
app.include_router(upload.router, prefix="/upload")


@app.get("/")
async def root():
    return {"message": "Hello World"}

