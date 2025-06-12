import logging
from pathlib import Path

from pydantic import BaseModel, PostgresDsn, RedisDsn
from pydantic_settings import BaseSettings, SettingsConfigDict
from redis.exceptions import ConnectionError, RedisError

from core.enums.envs import Envs

BASE_DIR = Path(__file__).resolve().parent.parent


class RedisConfig(BaseModel):
    url: RedisDsn
    decode_responses: bool = True
    retry_on_timeout: bool = True
    retry_on_error: list[type[RedisError]] = [ConnectionError]


class LoggingConfig(BaseModel):
    format: str = "[%(asctime)s.%(msecs)03d] %(module)10s:%(lineno)-3d %(levelname)-7s - %(message)s"
    level: int = logging.INFO


class DatabaseConfig(BaseModel):
    url: PostgresDsn
    echo: bool
    echo_pool: bool
    pool_size: int
    max_overflow: int

    naming_convention: dict[str, str] = {
        "ix": "ix_%(column_0_label)s",
        "uq": "uq_%(table_name)s_%(column_0_N_name)s",
        "ck": "ck_%(table_name)s_%(constraint_name)s",
        "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
        "pk": "pk_%(table_name)s",
    }


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=BASE_DIR.parent / ".env",
        env_prefix="BOT_CONFIG__",
        env_nested_delimiter="__",
        case_sensitive=False,
        extra="allow",
    )

    bot_token: str

    admin_id: int

    environment: Envs = Envs.local_test

    redis: RedisConfig

    db: DatabaseConfig

    log: LoggingConfig = LoggingConfig()

    register_passphrase: str
