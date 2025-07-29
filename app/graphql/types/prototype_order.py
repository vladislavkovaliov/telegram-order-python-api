from strawberry.experimental.pydantic import type as pydantic_type
from app.schemas.prototype_order import PrototypeOrder

@pydantic_type(model=PrototypeOrder, all_fields=True)
class PrototypeOrderType:
    pass