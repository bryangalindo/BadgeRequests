from fastapi import APIRouter, Depends
from Data.connection import Table
from dependencies import get_current_user

router = APIRouter(prefix="/api/v1/requests",
                   tags=["requests"], dependencies=[Depends(get_current_user)])


@router.get("/")
async def get_requests():
    table = Table('requests')
    data = table.query()
    return data.items


@router.get("/{item_id}")
async def get_request(item_id: int):
    table = Table('requests')
    item = table.query('RowKey', f'{item_id}')
    return item.items[0]
