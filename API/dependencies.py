from starlette.requests import Request
from fastapi.responses import RedirectResponse
from fastapi import HTTPException
from Data.connection import Table

# Dependencies such as authorize can go here


async def get_current_user(request: Request):
    user = request.session.get('user')
    if user is not None:
        return user
    else:
        raise HTTPException(status_code=403)


async def get_current_admin(request: Request):
    admin_table = Table('admins')
    user = request.session.get('user')
    email = user['email']

    if user is not None:
        try:
            admin = admin_table.query('PartitionKey', f'{email}')
            if admin.items != []:
                return user
            else:
                raise HTTPException(status_code=403)
        except Exception as e:
            raise HTTPException(status_code=500)

    else:
        raise HTTPException(status_code=403)
