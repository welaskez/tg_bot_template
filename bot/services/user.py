from typing import Callable

from core.models import User
from core.schemas.user import UserCreate, UserUpdate
from uow.abc import AbstractUOW

from .abc import AbstractService


class UserService(AbstractService):
    def __init__(self, uow_factory: Callable[[], AbstractUOW]) -> None:
        self._uow_factory = uow_factory

    async def get_by_id(self, user_id: int) -> User | None:
        async with self._uow_factory() as uow:
            return await uow.users.get(User.id == user_id)

    async def get_by_tg_id(self, tg_id: int) -> User | None:
        async with self._uow_factory() as uow:
            return await uow.users.get(User.tg_id == tg_id)

    async def add(self, user_create: UserCreate) -> User:
        async with self._uow_factory() as uow:
            user = await uow.users.add(**user_create.model_dump())
            await uow.commit()
            return user

    async def update(self, user_id: int, user_update: UserUpdate) -> User | None:
        async with self._uow_factory() as uow:
            user = await uow.users.get(User.id == user_id)

            if user:
                user = await uow.users.update(user, **user_update.model_dump(exclude_unset=True))
                await uow.commit()

                return user

            return None

    async def delete(self, user_id: int) -> None:
        async with self._uow_factory() as uow:
            user = await uow.users.get(User.id == user_id)
            if user:
                await uow.users.delete(user)
                await uow.commit()
