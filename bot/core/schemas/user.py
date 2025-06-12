from pydantic import BaseModel


class UserCreate(BaseModel):
    tg_id: int
    username: str
    name: str | None = None
    info: str | None = None
    photo: str | None = None


class UserUpdate(BaseModel):
    taps: int | None = None
    username: str | None = None
    name: str | None = None
    info: str | None = None
    photo: str | None = None


class UserUpdateForm(BaseModel):
    name: str
    info: str
    photo: str
