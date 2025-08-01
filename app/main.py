from fastapi import FastAPI
from fastapi.routing import APIRoute

from strawberry.fastapi import GraphQLRouter
# app import
from app.routers import items, sessions
from app.graphql.schema import schema
from app.lifecycle.lifespan import lifespan

app = FastAPI(lifespan=lifespan)
graphql_app = GraphQLRouter(schema)

app.include_router(items.router)
app.include_router(sessions.router)

for route in graphql_app.routes:
    if isinstance(route, APIRoute):
        route.include_in_schema = False

app.include_router(graphql_app, prefix="/graphql")
