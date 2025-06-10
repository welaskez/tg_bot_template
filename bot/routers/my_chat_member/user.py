import logging

from aiogram import Router, types
from aiogram.enums import ChatMemberStatus

logger = logging.getLogger(name=__name__)

router = Router(name=__name__)


@router.my_chat_member()
async def my_chat_member_updates(chat_member_updated: types.ChatMemberUpdated) -> None:
    new_status = chat_member_updated.new_chat_member.status
    old_status = chat_member_updated.old_chat_member.status

    if new_status == ChatMemberStatus.KICKED:
        logger.info(f"User {chat_member_updated.from_user.id} blocked bot")

    if old_status == ChatMemberStatus.KICKED and new_status == ChatMemberStatus.MEMBER:
        logger.info(f"User {chat_member_updated.from_user.id} unblocked bot")
