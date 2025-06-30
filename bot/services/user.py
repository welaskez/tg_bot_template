from typing import Callable

from core.config import Settings
from core.models import User
from core.schemas.user import UserCreate, UserUpdate, UserUpdateForm
from uow.abc import AbstractUOW

from .abc import AbstractService


class UserService(AbstractService):
    def __init__(self, uow_factory: Callable[[], AbstractUOW], settings: Settings) -> None:
        self._uow_factory = uow_factory
        self._settings = settings

    async def get_by_id(self, user_id: int) -> User | None:
        async with self._uow_factory() as uow:
            return await uow.users.get(User.id == user_id)

    async def get_by_tg_id(self, tg_id: int) -> User | None:
        async with self._uow_factory() as uow:
            return await uow.users.get(User.tg_id == tg_id)

    async def add(self, user_create: UserCreate) -> User:
        async with self._uow_factory() as uow:
            user = await uow.users.add(**user_create.model_dump())
            return user

    async def update(self, user: User, user_update: UserUpdate | UserUpdateForm) -> User | None:
        async with self._uow_factory() as uow:
            user = await uow.users.update(user, **user_update.model_dump(exclude_unset=True))
            return user

    async def delete(self, user_id: int) -> None:
        async with self._uow_factory() as uow:
            user = await uow.users.get(User.id == user_id)

            if not user:
                raise ValueError("User not found!")

            await uow.users.delete(user)

    async def register(self, user_create: UserCreate, register_passphrase: str | None = None) -> User | None:
        if register_passphrase and register_passphrase != self._settings.register_passphrase:
            raise ValueError("Incorrect register passphrase!")

        user = await self.get_by_tg_id(tg_id=user_create.tg_id)
        if not user:
            user = await self.add(user_create)

        return user

    async def fill_form(self, tg_id: int, form: UserUpdateForm) -> User | None:
        user = await self.get_by_tg_id(tg_id=tg_id)

        if not user:
            raise ValueError("User not found!")

        return await self.update(user, form)
