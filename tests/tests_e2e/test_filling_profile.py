import pytest
from core.models import User
from core.schemas.user import UserUpdateForm
from pydantic import ValidationError
from services.user import UserService


async def test_fill_form(user_service: UserService, user: User) -> None:
    user = await user_service.fill_form(
        tg_id=user.tg_id,
        form=UserUpdateForm(name="name", info="info", photo="photo"),
    )

    assert user.name == "name"
    assert user.info == "info"
    assert user.photo == "photo"


@pytest.mark.parametrize(
    "name, info, photo",
    [
        (None, "info", "photo"),
        ("name", None, "photo"),
        ("name", "info", None),
        (None, None, "photo"),
        (None, "info", None),
        ("name", None, None),
        (None, None, None),
    ]
)
async def test_fill_form_with_errors(
    user_service: UserService,
    user: User,
    name:str,
    info:str,
    photo:str,
) -> None:
    with pytest.raises(ValidationError):
        await user_service.fill_form(
            tg_id=user.tg_id,
            form=UserUpdateForm(name=name, info=info, photo=photo),
        )
