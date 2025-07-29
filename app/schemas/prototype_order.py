from pydantic import BaseModel
from typing import Optional

class PrototypeOrder(BaseModel):
    id: int
    name: str
    description: Optional[str] = None