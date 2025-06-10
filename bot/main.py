import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from core.apscheduler.app import scheduler
from core.config import Settings
from core.providers.app import AppProvider
from core.providers.database import SQLAlchemyProvider
from core.providers.redis import RedisProvider
from core.providers.service import ServiceProvider
from core.providers.uow import UOWProvider
from dishka import make_async_container
from dishka.integrations.aiogram import setup_dishka
from routers import router

logger = logging.getLogger(name=__name__)


async def on_startup(bot: Bot, dispatcher: Dispatcher) -> None:
    logger.info("Bot is up")


async def on_shutdown(bot: Bot, dispatcher: Dispatcher) -> None:
    logger.info("Bot is down")


async def main() -> None:
    container = make_async_container(
        AppProvider(), SQLAlchemyProvider(), RedisProvider(), UOWProvider(), ServiceProvider()
    )

    settings = await container.get(Settings)

    bot = Bot(
        token=settings.bot_token,
        default=DefaultBotProperties(
            link_preview_is_disabled=True,
            parse_mode=ParseMode.HTML,
        ),
    )
    dp = Dispatcher()

    await bot.delete_webhook(drop_pending_updates=True)

    scheduler.start()

    dp.include_router(router)

    dp.startup.register(on_startup)
    dp.shutdown.register(on_shutdown)

    setup_dishka(container=container, router=dp)

    logging.basicConfig(
        level=settings.log.level,
        format=settings.log.format,
        handlers=[logging.StreamHandler()],
    )

    try:
        await dp.start_polling(bot)
    finally:
        await container.close()


if __name__ == "__main__":
    asyncio.run(main())
