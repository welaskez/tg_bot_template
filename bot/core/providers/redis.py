from dishka import Provider, Scope, provide
from redis.asyncio import ConnectionPool, Redis

from core.config import Settings


class RedisProvider(Provider):
    scope = Scope.APP

    @provide
    def get_connection_pool(self, settings: Settings) -> ConnectionPool:
        connection_pool = ConnectionPool.from_url(str(settings.redis.url))
        connection_pool.decode_responses = settings.redis.decode_responses  # type: ignore[attr-defined]
        connection_pool.retry_on_timeout = settings.redis.retry_on_timeout  # type: ignore[attr-defined]
        connection_pool.retry_on_error = settings.redis.retry_on_error  # type: ignore[attr-defined]
        return connection_pool

    @provide
    def get_redis_client(self, connection_pool: ConnectionPool) -> Redis:
        client: Redis = Redis(connection_pool)
        return client
