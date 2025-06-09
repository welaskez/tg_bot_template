from aiogram import types
from aiogram.filters import Filter


class IsAdmin(Filter):
    def __init__(self, admin_ids: list[int]) -> None:
        self._admin_ids = admin_ids

    async def __call__(self, message: types.Message) -> bool:
        return message.from_user.id in self._admin_ids if message.from_user else False
