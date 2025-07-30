import strawberry

from typing import Optional

from app.crud import item as item_crud
from app.graphql.types.item import ItemType
from app.graphql.types.pagination_items import PaginatedItems


@strawberry.type
class Query:
    @strawberry.field
    def items(self, limit: int = 10, offset: int = 0) -> PaginatedItems:
        data = item_crud.get_items(limit=limit, offset=offset)

        return PaginatedItems(
            total=data["total"],
            items=data["items"],
        )

    @strawberry.field
    async def item(self, item_id: str) -> Optional[ItemType]:
        item = await item_crud.get_item_id(item_id=item_id)

        if not item:
            raise ValueError("Item not found")
        return ItemType(
            id=item["_id"],
            is_active=item["is_active"],
            price=item["price"],
            currency=item["currency"],
            picture=item["picture"],
            title=item["title"],
            description=item["description"],
            tags=item["tags"],
        )