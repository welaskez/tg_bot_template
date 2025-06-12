from typing import Any, AsyncGenerator

import pytest
from core.config import Settings
from core.providers.app import AppProvider
from core.providers.database import SQLAlchemyProvider
from core.providers.feature import FeatureProvider
from core.providers.keyboard import KeyboardProvider
from core.providers.redis import RedisProvider
from core.providers.service import ServiceProvider
from core.providers.ui import UIProvider
from core.providers.uow import UOWProvider
from dishka import AsyncContainer, make_async_container
from services.user import UserService


@pytest.fixture()
async def container() -> AsyncGenerator[AsyncContainer, Any]:
    container = make_async_container(
        AppProvider(),
        SQLAlchemyProvider(),
        RedisProvider(),
        UOWProvider(),
        ServiceProvider(),
        FeatureProvider(),
        UIProvider(),
        KeyboardProvider(),
    )

    yield container

    await container.close()


@pytest.fixture()
async def settings(container: AsyncContainer) -> Settings:
    return await container.get(Settings)


@pytest.fixture()
async def user_service(container: AsyncContainer) -> UserService:
    return await container.get(UserService)
