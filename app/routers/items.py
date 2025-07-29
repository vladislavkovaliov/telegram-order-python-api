from fastapi import APIRouter
from typing import Union
from app.schemas.item import Item as ItemSchema


router = APIRouter(prefix="/items", tags=["items"])


@router.get("/{item_id}")
async def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@router.put("/{item_id}")
async def update_item(item_id: int, item: ItemSchema):
    return {"item_name": item.name, "item_id": item_id}