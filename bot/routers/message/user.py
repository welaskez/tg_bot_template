from aiogram import Router, types
from aiogram.filters import Command
from core.schemas.user import UserCreate
from dishka import FromDishka
from dishka.integrations.aiogram import inject
from services.user import UserService

router = Router(name=__name__)


@router.message(Command("start"))
@inject
async def start(message: types.Message, user_service: FromDishka[UserService]) -> None:
    if message.from_user:
        await user_service.register(
            user_create=UserCreate(tg_id=message.from_user.id, username=message.from_user.username)
        )
    await message.answer(text="Привет!")
