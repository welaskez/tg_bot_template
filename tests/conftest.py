from typing import Any, AsyncGenerator, Callable

import pytest
from core.config import Settings
from core.models import Base, User
from core.models.engine import DatabaseHelper
from core.providers.app import AppProvider
from core.schemas.user import UserCreate
from dishka import AsyncContainer, make_async_container
from services.user import UserService
from testcontainers.postgres import PostgresContainer
from uow.abc import AbstractUOW
from uow.sqlalchemy import SQLAlchemyUOW


@pytest.fixture()
async def container() -> AsyncGenerator[AsyncContainer, Any]:
    container = make_async_container(AppProvider())

    yield container

    await container.close()


@pytest.fixture(scope="session")
def postgres_container():
    with PostgresContainer(image="postgres:15", driver="asyncpg") as postgres:
        yield postgres


@pytest.fixture(scope="session")
def db_helper(postgres_container: PostgresContainer) -> DatabaseHelper:
    return DatabaseHelper(
        url=postgres_container.get_connection_url(driver="asyncpg"),
        pool_size=50,
        max_overflow=10,
        echo=True,
        echo_pool=True,
    )


@pytest.fixture(scope="session", autouse=True)
async def setup_db(db_helper: DatabaseHelper):
    async with db_helper.engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    yield

    async with db_helper.engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)


@pytest.fixture()
async def settings(container: AsyncContainer) -> Settings:
    return await container.get(Settings)


@pytest.fixture()
async def sqla_uow_factory(db_helper: DatabaseHelper) -> Callable[[], AbstractUOW]:
    return lambda: SQLAlchemyUOW(session_pool=db_helper.session_pool)


@pytest.fixture()
def user_service(sqla_uow_factory: Callable[[], AbstractUOW], settings: Settings) -> UserService:
    return UserService(sqla_uow_factory, settings)

@pytest.fixture()
async def user(user_service: UserService) -> User:
    return await user_service.add(UserCreate(tg_id=12345, username="zan"))
