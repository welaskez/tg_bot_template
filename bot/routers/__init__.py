__all__ = ("router",)

from aiogram import Router

from .callback_query import router as callback_query_router
from .message import router as message_router
from .my_chat_member import router as my_chat_member_router

router = Router(name=__name__)
router.include_router(message_router)
router.include_router(callback_query_router)
router.include_router(my_chat_member_router)
