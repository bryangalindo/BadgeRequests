from fastapi import APIRouter, Depends
from Data.connection import Table
from dependencies import get_current_user, get_current_admin

router = APIRouter(prefix="/api/v1/requests",
                   tags=["requests"], dependencies=[Depends(get_current_user)])


@router.get("/")
async def get_requests(admin=Depends(get_current_admin)):
    table = Table('requests')
    data = table.query()
    return data.items


@router.get("/{item_id}")
async def get_request(item_id: int, admin=Depends(get_current_admin)):
    table = Table('requests')
    item = table.query('RowKey', f'{item_id}')
    return item.items[0]
