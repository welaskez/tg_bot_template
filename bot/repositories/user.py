from core.models import User
from sqlalchemy.ext.asyncio import AsyncSession

from .sqlalchemy import SQLAlchemyRepository


class UserRepository(SQLAlchemyRepository[User]):
    model = User

    def __init__(self, session: AsyncSession):
        super().__init__(session)
