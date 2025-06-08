from aiogram import types
from aiogram.filters import Filter
from core.config import settings


class IsAdmin(Filter):
    async def __call__(self, message: types.Message) -> bool:
        return message.from_user.id == settings.admin_id if message.from_user else False
