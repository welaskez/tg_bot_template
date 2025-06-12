from aiogram import types
from core.feature.registry import FeatureRegistry

from services.ui.keyboard_builder import KeyboardBuilderService


class MenuService:
    def __init__(self, feature_registry: FeatureRegistry, keyboard_builder: KeyboardBuilderService):
        self.feature_registry = feature_registry
        self.keyboard_builder = keyboard_builder

    async def show_menu(self, message: types.Message, feature_name: str) -> None:
        feature = self.feature_registry.get_feature(feature_name)
        if feature:
            keyboard = self.keyboard_builder.build_reply_keyboard(feature_name)
            await message.answer(feature.text, reply_markup=keyboard)
