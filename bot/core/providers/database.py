from dishka import Provider, Scope, provide

from core.config import Settings
from core.models.engine import DatabaseHelper


class SQLAlchemyProvider(Provider):
    scope = Scope.APP

    @provide
    def get_db_helper(self, settings: Settings) -> DatabaseHelper:
        return DatabaseHelper(
            url=str(settings.db.url),
            pool_size=settings.db.pool_size,
            max_overflow=settings.db.max_overflow,
            echo=settings.db.echo,
            echo_pool=settings.db.echo_pool,
        )
