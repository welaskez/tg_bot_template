from dishka import Provider, Scope, provide

from core.config import Settings


class AppProvider(Provider):
    scope = Scope.APP

    @provide
    def get_settings(self) -> Settings:
        return Settings()
