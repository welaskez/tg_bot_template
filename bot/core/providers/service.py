from typing import Callable

from dishka import Provider, Scope, provide
from services.user import UserService
from uow.abc import AbstractUOW


class ServiceProvider(Provider):
    scope = Scope.REQUEST

    @provide
    def get_user_service(self, sqla_uow_factory: Callable[[], AbstractUOW]) -> UserService:
        return UserService(uow_factory=sqla_uow_factory)
