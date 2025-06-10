from aiogram import types
from aiogram.filters import Filter
from core.config import Settings
from dishka import FromDishka


class IsAdmin(Filter):
    async def __call__(self, message: types.Message, settings: FromDishka[Settings]) -> bool:
        return message.from_user.id == settings.admin_id if message.from_user else False
