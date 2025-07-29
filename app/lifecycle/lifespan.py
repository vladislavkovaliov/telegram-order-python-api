from app.external_services.redis import initialize_redis

from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.configs.redis import RedisSettings

redis_settings = RedisSettings()

@asynccontextmanager
async def lifespan(app: FastAPI):
    app.state.redis = await initialize_redis(str(redis_settings.redis_url))

    yield # run application

    await app.state.redis.close()