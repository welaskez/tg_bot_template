from pydantic import BaseModel


class BaseButton(BaseModel):
    text: str
    web_app_url: str | None = None


class ReplyButton(BaseButton):
    pass


class InlineButton(BaseButton):
    callback_data: str | None = None


class KeyboardData(BaseModel):
    reply_buttons: list[ReplyButton] | None = None
    inline_buttons: list[list[InlineButton]] | None = None
    one_time: bool = False
    resize: bool = True
