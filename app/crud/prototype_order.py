from app.schemas.prototype_order import PrototypeOrder


def get_prototype_orders():
    return [
        PrototypeOrder(id=1, name="<NAME> 1"),
    ]