from sqlalchemy import MetaData
from sqlalchemy.orm import DeclarativeBase, declared_attr
from utils.case_converter import camel_case_to_snake_case

from core.config import Settings

settings = Settings()


class Base(DeclarativeBase):
    __abstract__ = True

    metadata = MetaData(
        naming_convention=settings.db.naming_convention,
    )

    @declared_attr.directive
    def __tablename__(cls) -> str:
        return f"{camel_case_to_snake_case(cls.__name__)}s"
