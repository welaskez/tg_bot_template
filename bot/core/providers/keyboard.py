from dishka import Provider, Scope, provide

from core.keyboard.registry import KeyboardRegistry


class KeyboardProvider(Provider):
    scope = Scope.REQUEST

    @provide
    def get_keyboard_registry(self) -> KeyboardRegistry:
        return KeyboardRegistry()
