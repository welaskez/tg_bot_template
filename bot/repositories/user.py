from core.models import User
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql.functions import func

from .sqlalchemy import SQLAlchemyRepository


class UserRepository(SQLAlchemyRepository[User]):
    model = User

    def __init__(self, session: AsyncSession):
        super().__init__(session)

    async def get_all_taps(self) -> int:
        return await self._session.scalar(select(func.sum(User.taps))) or 0

    async def get_top_user(self) -> User | None:
        result: User | None = await self._session.scalar(
            select(User).where(User.taps > 0).order_by(User.taps.desc()).limit(1)
        )
        return result
