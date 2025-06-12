from aiogram import types
from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder
from core.keyboard.registry import KeyboardRegistry


class KeyboardBuilderService:
    def __init__(self, keyboard_registry: KeyboardRegistry):
        self.keyboard_registry = keyboard_registry

    def build_reply_keyboard(
        self, feature_name: str
    ) -> types.ReplyKeyboardMarkup | types.ReplyKeyboardRemove:
        config = self.keyboard_registry.get_keyboard_data(feature_name)

        if not config or not config.reply_buttons:
            return types.ReplyKeyboardRemove()

        builder = ReplyKeyboardBuilder()
        for row in config.reply_buttons:
            builder.row(
                *[
                    types.KeyboardButton(
                        text=row.text,
                        web_app=types.WebAppInfo(url=row.web_app_url) if row.web_app_url else None,
                    )
                ]
            )

        return builder.as_markup(resize_keyboard=config.resize, one_time_keyboard=config.one_time)

    def build_inline_keyboard(self, feature_name: str) -> types.InlineKeyboardMarkup | None:
        config = self.keyboard_registry.get_keyboard_data(feature_name)

        if not config or not config.inline_buttons:
            return None

        builder = InlineKeyboardBuilder()
        for row in config.inline_buttons:
            buttons = [
                types.InlineKeyboardButton(
                    text=c.text,
                    callback_data=c.callback_data if c.callback_data else None,
                    web_app=types.WebAppInfo(url=c.web_app_url) if c.web_app_url else None,
                )
                for c in row
            ]
            builder.row(*buttons)

        return builder.as_markup()
