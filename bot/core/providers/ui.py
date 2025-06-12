from dishka import Provider, Scope, provide
from services.ui.keyboard_builder import KeyboardBuilderService
from services.ui.menu import MenuService

from core.feature.registry import FeatureRegistry
from core.keyboard.registry import KeyboardRegistry


class UIProvider(Provider):
    scope = Scope.REQUEST

    @provide
    def get_keyboard_builder(self, keyboard_registry: KeyboardRegistry) -> KeyboardBuilderService:
        return KeyboardBuilderService(keyboard_registry)

    @provide
    def get_menu_service(
        self,
        feature_registry: FeatureRegistry,
        keyboard_builder: KeyboardBuilderService,
    ) -> MenuService:
        return MenuService(feature_registry, keyboard_builder)
