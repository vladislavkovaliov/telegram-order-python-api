from pydantic import AnyUrl
from pydantic_settings import BaseSettings

class RedisSettings(BaseSettings):
    redis_url: AnyUrl = "redis://localhost:6379"
    api_key: str = ""

    class Config:
        env_file = ".env"