from aiogram import Router, types
from aiogram.filters import Command
from core.feature.registry import FeatureRegistry
from dishka import FromDishka
from dishka.integrations.aiogram import inject

router = Router(name=__name__)


@router.message(Command("ping"))
@inject
async def ping(message: types.Message, feature_registry: FromDishka[FeatureRegistry]) -> None:
    feature = feature_registry.get_feature("ping")
    if feature:
        await message.answer(feature.text)
