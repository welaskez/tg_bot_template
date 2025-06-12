from typing import Callable

import pytest
from core.models import Base
from core.models.engine import DatabaseHelper
from services.user import UserService
from testcontainers.postgres import PostgresContainer
from uow.abc import AbstractUOW
from uow.sqlalchemy import SQLAlchemyUOW


@pytest.fixture()
def postgres_container():
    with PostgresContainer(
        image="postgres:15",
        driver="asyncpg"
    ) as postgres:
        yield postgres


@pytest.fixture()
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
async def sqla_uow_factory(db_helper: DatabaseHelper) -> Callable[[], AbstractUOW]:
    return lambda: SQLAlchemyUOW(session_pool=db_helper.session_pool)


@pytest.fixture()
def user_service(sqla_uow_factory: Callable[[], AbstractUOW]) -> UserService:
    return UserService(sqla_uow_factory)
