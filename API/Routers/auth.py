from fastapi import APIRouter, Depends
from starlette.requests import Request

from Data.connection import Table
from dependencies import get_current_user


router = APIRouter(prefix="/api/v1/auth",
                   tags=["auth"])


@router.get("/me")
async def get_me(request: Request):
    user = request.session.get('user')
    if user is not None:
        email = user['email']
        name = user['name']
        avatar = user['picture']
        return {"email": email, "name": name, "avatar": avatar}
    return {"email": ""}
