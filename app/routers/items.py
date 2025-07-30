from fastapi import APIRouter, Query, HTTPException

from app.crud.item import get_items, get_item_id

router = APIRouter(prefix="/items", tags=["items"])

@router.get("/")
async def items(limit: int = Query(10, ge=1), offset: int = Query(0, ge=0)):
    return get_items(limit=limit, offset=offset)

@router.get("/{item_id}")
async def read_item(item_id: str):
    item = await get_item_id(item_id)

    if not item:
        raise HTTPException(status_code=404, detail="Item not found")

    return item