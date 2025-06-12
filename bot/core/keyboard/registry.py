from core.schemas.keyboard import KeyboardData, ReplyButton


class KeyboardRegistry:
    KEYBOARDS: dict[str, KeyboardData] = {
        "start": KeyboardData(
            reply_buttons=[
                ReplyButton(text="Нажми меня"),
                ReplyButton(text="Рейтинг"),
                ReplyButton(text="Мой профиль"),
            ]
        )
    }

    @classmethod
    def get_keyboard_data(cls, feature_name: str) -> KeyboardData | None:
        return cls.KEYBOARDS.get(feature_name)
