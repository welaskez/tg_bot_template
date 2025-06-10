from typing import Any, Generic, Optional, cast

from core.models import Base
from sqlalchemy import ColumnExpressionArgument, select
from sqlalchemy.ext.asyncio import AsyncSession
from typing_extensions import TypeVar

from .abc import AbstractRepository

T = TypeVar("T", bound=Base)


class SQLAlchemyRepository(Generic[T], AbstractRepository):
    model: type[T]

    def __init__(self, session: AsyncSession) -> None:
        self._session = session

    async def get(self, *conditions: ColumnExpressionArgument[Any]) -> Optional[T]:
        return cast(Optional[T], await self._session.scalar(select(self.model).where(*conditions)))

    async def add(self, **kwargs: Any) -> T:
        entity = self.model(**kwargs)
        self._session.add(entity)
        return entity

    async def update(self, entity: T, **kwargs: Any) -> T:
        for k, v in kwargs.items():
            setattr(entity, k, v)
        return entity

    async def delete(self, entity: T) -> None:
        await self._session.delete(entity)
