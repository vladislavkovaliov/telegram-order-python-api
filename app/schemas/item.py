from pydantic import BaseModel
from typing import Union


class Item(BaseModel):
    id: str
    is_active: bool
    price: float
    currency: str
    picture: str
    title: str
    description: str
    tags: list[str]
