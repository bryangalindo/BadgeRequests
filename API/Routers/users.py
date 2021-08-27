from pydantic import BaseModel
from fastapi import APIRouter, Depends

from Data.connection import Table
from dependencies import get_current_user, get_current_admin


router = APIRouter(prefix="/users",
                   tags=["users"], dependencies=[Depends(get_current_user)])


class User(BaseModel):
    PartitionKey: str
    RowKey: str
    Supervisor: str
    SupervisorGoogleChatID: str

@router.get("/")
async def get_users(admin=Depends(get_current_admin)):
    table = Table('users')
    data = table.query()
    return data.items


@router.get("/{user_id}")
async def get_user(user_id: str, admin=Depends(get_current_admin)):
    table = Table('users')
    item = table.query('RowKey', f'{user_id}')
    if item.items:
        return item.items[0]
    else:
        return


@router.post("/")
async def create_user(user: User):
    user_table = Table('users')
    user_dict = dict(
        PartitionKey=user.PartitionKey, 
        RowKey=user.RowKey,
        Supervisor=user.Supervisor,
        SupervisorGoogleChatID=user.SupervisorGoogleChatID,
    )
    user_table.insert(user_dict)
    return user

