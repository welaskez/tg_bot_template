from typing import Callable

from dishka import Provider, Scope, provide
from uow.abc import AbstractUOW
from uow.sqlalchemy import SQLAlchemyUOW

from core.models.engine import DatabaseHelper


class UOWProvider(Provider):
    scope = Scope.REQUEST

    @provide
    def get_sqla_uow_factory(self, db_helper: DatabaseHelper) -> Callable[[], AbstractUOW]:
        return lambda: SQLAlchemyUOW(session_pool=db_helper.session_pool)
