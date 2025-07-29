from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter

# app import
from app.routers import items
from app.graphql.schema import schema

app = FastAPI()

app.include_router(items.router)
graphql_app = GraphQLRouter(schema)
app.include_router(graphql_app, prefix="/graphql")
