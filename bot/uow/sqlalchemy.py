from types import TracebackType
from typing import Optional, Self

from repositories.user import UserRepository
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker

from .abc import AbstractUOW


class SQLAlchemyUOW(AbstractUOW):
    def __init__(self, session_pool: async_sessionmaker[AsyncSession]) -> None:
        self._session_pool = session_pool
        self._session: AsyncSession

    async def __aenter__(self) -> Self:
        self._session = self._session_pool()
        self.users = UserRepository(session=self._session)
        return self

    async def __aexit__(
        self,
        exc_type: Optional[type[BaseException]],
        exc_val: Optional[BaseException],
        exc_tb: Optional[TracebackType],
    ) -> None:
        if exc_type:
            await self.rollback()
        await self._session.close()

    async def rollback(self) -> None:
        await self._session.rollback()

    async def commit(self) -> None:
        await self._session.commit()
