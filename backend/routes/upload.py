from fastapi import APIRouter, Depends, File, UploadFile, HTTPException
from db.database import get_db
router = APIRouter()


@router.post("/upload")
async def upload_file(db = Depends(get_db), file: UploadFile = File(...), listing_id: int = -1):
    # validate content type
    if not file.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="Invalid file type. Only images are allowed.")
    
    # process file
    contents = await file.read()

    #need to upload to database
    db.execute("INSERT INTO images (listing_id, image_data) VALUES (?, ?)", (listing_id, contents))

    return {"file uploaded successfully": file.filename}