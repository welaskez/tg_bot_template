from typing import Generic

from repositories.sqlalchemy import SQLAlchemyRepository, T
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker

from .abc import AbstractUOW


class SQLAlchemyUOW(Generic[T], AbstractUOW):
    def __init__(self, session_pool: async_sessionmaker[AsyncSession]) -> None:
        self._session_pool = session_pool
        self._session: AsyncSession
        self.repo: SQLAlchemyRepository[T]

    async def __aenter__(self) -> "SQLAlchemyUOW[T]":
        self._session = self._session_pool()
        self.repo = SQLAlchemyRepository(session=self._session)
        return self

    async def __aexit__(self) -> None:
        await self.rollback()
        await self._session.close()

    async def rollback(self) -> None:
        await self._session.rollback()

    async def commit(self) -> None:
        await self._session.commit()
