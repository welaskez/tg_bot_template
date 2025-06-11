from typing import Optional

from core.feature.dto import FeatureData


class FeatureRegistry:
    FEATURES: dict[str, FeatureData] = {
        "start": FeatureData(
            name="start",
            text="Добро пожаловать в главное меню",
            triggers=["/start"],
            description="main menu",
        ),
        "ping": FeatureData(
            name="ping",
            text="200 pong",
            triggers=["/ping", "ping", "health", "healthcheck"],
        ),
        "cancel": FeatureData(
            name="cancel",
            text="Принял, отбой, возвращаюсь в главное меню.",
            triggers=["/cancel"],
            description="Отменить текущую операцию",
        ),
        "creator": FeatureData(
            name="creator",
            text="*Master?*",
            triggers=["creator"],
        ),
        "help": FeatureData(
            name="help",
            text=(
                "ℹ️ *Доступные команды:*\n\n/ping - проверить работу\n/cancel - отменить операцию"
                "\n/creator - о создателе"
            ),
            triggers=["/help", "help", "помощь", "/start"],
            description="Справка по командам",
        ),
        "empty": FeatureData(name="", text="", triggers=[]),
    }

    @classmethod
    def get_feature(cls, name: str) -> Optional[FeatureData]:
        return cls.FEATURES.get(name)

    @classmethod
    def find_by_trigger(cls, trigger: str) -> Optional[FeatureData]:
        trigger = trigger.lower().strip()
        for feature in cls.FEATURES.values():
            if trigger in [t.lower() for t in feature.triggers]:
                return feature
        return None

    @classmethod
    def get_bot_commands(cls) -> list[tuple[str, str]]:
        commands = []
        for feature in cls.FEATURES.values():
            for trigger in feature.triggers:
                if trigger.startswith("/") and feature.description:
                    commands.append((trigger, feature.description))
                    break
        return commands

    @classmethod
    def get_all_triggers(cls) -> list[str]:
        triggers = []
        for feature in cls.FEATURES.values():
            triggers.extend(feature.triggers)
        return triggers
