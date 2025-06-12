from aiogram import F, Router, types
from core.feature.registry import FeatureRegistry
from dishka import FromDishka
from dishka.integrations.aiogram import inject
from filters import IsAdmin

router = Router(name=__name__)
router.message.filter(IsAdmin())


@router.message(F.text == "creator")
@inject
async def creator(message: types.Message, feature_registry: FromDishka[FeatureRegistry]) -> None:
    feature = feature_registry.get_feature("creator")
    if feature:
        await message.answer(feature.text)
