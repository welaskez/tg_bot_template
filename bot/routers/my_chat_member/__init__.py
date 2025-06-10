__all__ = ("router",)

from aiogram import Router

from .user import router as user_router

router = Router(name=__name__)
router.include_router(user_router)
