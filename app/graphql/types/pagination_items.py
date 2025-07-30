import strawberry

from typing import List
from app.graphql.types.item import ItemType


@strawberry.type
class PaginatedItems:
    total: int
    items: List[ItemType]