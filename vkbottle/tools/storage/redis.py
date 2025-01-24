import json

from typing import Self, Callable, Optional, Any

from redis.asyncio.connection import ConnectionPool
from redis.asyncio.client import Redis
from redis.typing import ExpiryT

from ..key_builder import BaseKeyBuilder, DefaultKeyBuilder, DefaultKeyStorage
from .base import BaseFsmStorage


class RedisFsmStorage(BaseFsmStorage):

    def __init__(
        self,
        redis: Redis,
        ttl: Optional[ExpiryT] = None,
        json_loads: Callable[..., Any] = json.loads,
        json_dumps: Callable[..., str] = json.dumps,
        key_builder: Optional[BaseKeyBuilder] = None
    ) -> None:
        self.redis = redis
        self.ttl = ttl
        self.json_loads = json_loads
        self.json_dumps = json_dumps

        if not key_builder:
            key_builder = DefaultKeyBuilder(prefix='redis_fsm')

        self.key_builder = key_builder

    @classmethod
    def from_url(
        cls,
        url: str,
        connection: Optional[dict[str, Any]] = None,
        **kwargs: Any
    ) -> Self:
        """
            ...
        """
        if connection is None:
            connection = {}

        redis_pool = ConnectionPool.from_url(url, **connection)
        redis = Redis.from_pool(connection_pool=redis_pool)

        return cls(redis=redis, **kwargs)

    async def close(self) -> None:
        """
            ...
        """
        await self.redis.aclose(close_connection_pool=True)

    async def set_state(
        self,
        key: DefaultKeyStorage,
        state: Optional[str] = None
    ) -> None:
        redis_key = self.key_builder.build(key, 'state')

        if state is None:
            return await self.redis.delete(redis_key)
        return await self.redis.set(redis_key, state, ex=self.ttl)

    async def get_state(self, key: DefaultKeyStorage) -> Optional[str]:
        redis_key = self.key_builder.build(key, 'state')
        value = await self.redis.get(redis_key)

        if isinstance(value, bytes):
            return value.decode('utf-8')
        return value

    async def set_data(
        self,
        key: DefaultKeyStorage,
        data: Optional[dict[str, Any]] = None
    ) -> None:
        redis_key = self.key_builder.build(key, 'data')

        if not data:
            return await self.redis.delete(redis_key)
        return await self.redis.set(
            name=redis_key,
            value=self.json_dumps(data),
            ex=self.ttl,
        )

    async def get_data(self, key: DefaultKeyStorage) -> dict[str, Any]:
        redis_key = self.key_builder.build(key, 'data')
        value = await self.redis.get(redis_key)

        if value is None:
            return {}
        if isinstance(value, bytes):
            value = value.decode('utf-8')
        return self.json_loads(value)
