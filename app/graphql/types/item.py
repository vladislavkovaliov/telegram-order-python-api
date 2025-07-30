import strawberry

from typing import List


@strawberry.type
class ItemType:
    id: str
    is_active: bool
    price: float
    currency: str
    picture: str
    title: str
    description: str
    tags: List[str]