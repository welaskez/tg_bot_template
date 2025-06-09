from typing import Any

from redis.asyncio import Redis

from .abc import AbstractRepository


class RedisRepository(AbstractRepository):
    def __init__(self, client: Redis) -> None:
        self._client = client

    async def get(self, key: str) -> Any:
        return await self._client.get(name=key)

    async def add(self, key: str, value: Any) -> None:
        await self._client.set(name=key, value=value)

    async def update(self, key: str, value: Any) -> None:
        exists = await self.get(key)
        if exists:
            await self._client.set(name=key, value=value)

    async def delete(self, key: str) -> None:
        await self._client.delete(key)
