from redis.asyncio import ConnectionPool, Redis

from core.config import settings

connection_pool = ConnectionPool.from_url(url=str(settings.redis.url))
connection_pool.retry_on_timeout = settings.redis.retry_on_timeout  # type: ignore[attr-defined]
connection_pool.decode_responses = settings.redis.decode_responses  # type: ignore[attr-defined]
connection_pool.retry_on_error = settings.redis.retry_on_error  # type: ignore[attr-defined]

redis_client = Redis(connection_pool=connection_pool)
