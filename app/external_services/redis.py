import aioredis

from typing import Optional

async def initialize_redis(redis_url: str) -> aioredis.Redis:
    redis = aioredis.from_url(redis_url)
    # Optionally test connection
    await redis.ping()

    return redis