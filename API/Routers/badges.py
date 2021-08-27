from fastapi import APIRouter, Depends
from Data.connection import Table
from dependencies import get_current_user


router = APIRouter(prefix="/badges",
                   tags=["badges"], dependencies=[Depends(get_current_user)])


@router.get("/")
async def get_badges():
    table = Table('badges')
    data = table.query()
    return data.items


@router.get("/{item_id}")
async def get_badge(item_id: int):
    table = Table('badges')
    item = table.query('RowKey', f'{item_id}')
    return item.items[0]
