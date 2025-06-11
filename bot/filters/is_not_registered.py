from aiogram import types
from aiogram.filters import Filter
from dishka import FromDishka
from dishka.integrations.aiogram import inject
from services.user import UserService


class IsNotRegistered(Filter):
    @inject
    async def __call__(self, message: types.Message, user_service: FromDishka[UserService]) -> bool:
        if message.from_user:
            user = await user_service.get_by_tg_id(tg_id=message.from_user.id)
            return user is None

        return False
