import strawberry

from app.graphql.resolvers.prototype_order import Query as PrototypeOrderQuery

@strawberry.type
class Query(PrototypeOrderQuery):
    pass

schema = strawberry.Schema(query=Query)