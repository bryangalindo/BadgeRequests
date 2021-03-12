from fastapi import APIRouter
from Data.connection import Table


router = APIRouter(prefix="/api/v1/requests",  tags=["requests"])


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
