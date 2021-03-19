from starlette.requests import Request
from fastapi.responses import RedirectResponse
from fastapi import HTTPException

# Dependencies such as authorize can go here


async def get_current_user(request: Request):
    user = request.session.get('user')
    if user is not None:
        return user
    else:
        raise HTTPException(status_code=403)
