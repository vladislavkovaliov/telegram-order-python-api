import strawberry

from app.graphql.resolvers.prototype_order import Query as PrototypeOrderQuery
from app.graphql.resolvers.item import Query as ItemQuery

@strawberry.type
class Query(PrototypeOrderQuery, ItemQuery):
    pass

schema = strawberry.Schema(query=Query)
