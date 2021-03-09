from fastapi import APIRouter

router = APIRouter()


@router.get("/badges/", tags=["badges"])
async def get_badges():
