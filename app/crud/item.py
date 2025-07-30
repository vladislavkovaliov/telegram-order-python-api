from app.mocks.items import items
from app.schemas.item import Item


def get_items(limit: int = 10, offset: int = 0):
    total = len(items)

    paginated_items = items[offset:offset + limit]

    array = [Item(
        id=x["_id"],
        is_active=x["is_active"],
        price=x["price"],
        currency=x["currency"],
        picture=x["picture"],
        title=x["title"],
        description=x["description"],
        tags=x["tags"],
    ) for x in paginated_items]

    return {
        "total": total,
        "items": array,
    }


async def get_item_id(item_id: str):
    for x in items:
        if x["_id"] == item_id:
            return x

    return None