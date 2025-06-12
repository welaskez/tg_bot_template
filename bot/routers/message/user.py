from aiogram import Router, types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from core.feature.registry import FeatureRegistry
from dishka import FromDishka
from dishka.integrations.aiogram import inject
from services.ui.menu import MenuService

router = Router(name=__name__)


@router.message(Command("ping"))
@inject
async def ping(message: types.Message, feature_registry: FromDishka[FeatureRegistry]) -> None:
    feature = feature_registry.get_feature("ping")
    if feature:
        await message.answer(feature.text)


@router.message(Command("cancel"))
@inject
async def cancel(
    message: types.Message,
    state: FSMContext,
    feature_registry: FromDishka[FeatureRegistry],
    menu_service: FromDishka[MenuService],
) -> None:
    feature = feature_registry.get_feature("cancel")
    if feature:
        await message.answer(feature.text)

    if await state.get_state() is not None:
        await state.clear()

    await menu_service.show_menu(message, feature_name="start")
