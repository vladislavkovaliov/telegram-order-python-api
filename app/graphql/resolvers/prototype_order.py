import strawberry

from typing import List
from app.crud import prototype_order as prototype_order_crud
from app.graphql.types.prototype_order import PrototypeOrderType


@strawberry.type
class Query:
    @strawberry.field
    def orders(self) -> List[PrototypeOrderType]:
        orders = prototype_order_crud.get_prototype_orders()

        return orders