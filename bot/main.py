import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from core.apscheduler.app import scheduler
from core.config import settings
from routers import router

logger = logging.getLogger(name=__name__)

bot = Bot(
    token=settings.bot_token,
    default=DefaultBotProperties(
        link_preview_is_disabled=True,
        parse_mode=ParseMode.HTML,
    ),
)
dp = Dispatcher()


async def on_startup(bot: Bot, dispatcher: Dispatcher) -> None:
    logger.info("Bot is up")


async def on_shutdown(bot: Bot, dispatcher: Dispatcher) -> None:
    logger.info("Bot is down")


async def main() -> None:
    await bot.delete_webhook(drop_pending_updates=True)

    scheduler.start()

    dp.include_router(router)

    dp.startup.register(on_startup)
    dp.shutdown.register(on_shutdown)

    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(
        level=settings.log.level,
        format=settings.log.format,
        handlers=[logging.StreamHandler()],
    )
    asyncio.run(main())
