from fastapi import APIRouter, Depends
from Data.connection import Table
from dependencies import get_current_user
from starlette.requests import Request

router = APIRouter(prefix="/api/v1/auth",
                   tags=["auth"])


@router.get("/me")
async def get_me(request: Request):
    user = request.session.get('user')
    if user is not None:
        email = user['email']
        name = user['name']
        return {"email": email, "name": name}
    return {"email": ""}
