from sqlalchemy import BigInteger, String
from sqlalchemy.orm import Mapped, mapped_column

from core.models import Base
from core.models.mixins import CreatedAtMixin, IntPkMixin


class User(IntPkMixin, CreatedAtMixin, Base):
    tg_id: Mapped[int] = mapped_column(BigInteger)
    username: Mapped[str] = mapped_column(String(50))
    taps: Mapped[int] = mapped_column(BigInteger, default=0)
    name: Mapped[str | None]
    info: Mapped[str | None]
    photo: Mapped[str | None]
