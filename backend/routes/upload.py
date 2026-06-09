from fastapi import APIRouter, Depends, File, UploadFile, HTTPException
from db.database import get_db
from services.ai_service import analyze_image
from services.listing_service import create_listing
router = APIRouter()


@router.post("/upload")
async def upload_file(db = Depends(get_db), file: UploadFile = File(...)):
    # validate content type
    if not file.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="Invalid file type. Only images are allowed.")
    
    # process file
    contents = await file.read()

    #call ai_service to analyze image and get listing details
    ai_response = analyze_image(contents, file.content_type)

    # create listing with analyzed details
    listing_id = create_listing(
        db=db,
        title=ai_response["title"],
        description=ai_response["description"],
        price=ai_response["price"],
        category=ai_response["category"]
    )

    return {"listing created successfully": listing_id}