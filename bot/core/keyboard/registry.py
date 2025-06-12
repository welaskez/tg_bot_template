from core.schemas.keyboard import KeyboardData


class KeyboardRegistry:
    KEYBOARDS: dict[str, KeyboardData] = {
        "start": KeyboardData(),
        "help": KeyboardData(),
        "settings": KeyboardData(),
        "empty": KeyboardData(),
    }

    @classmethod
    def get_keyboard_data(cls, feature_name: str) -> KeyboardData | None:
        return cls.KEYBOARDS.get(feature_name)
