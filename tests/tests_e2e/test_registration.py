import pytest
from core.schemas.user import UserCreate
from pydantic import ValidationError
from services.user import UserService


@pytest.mark.parametrize("register_passphrase,username", [("ASDF", "naz")])
async def test_registration_with_correct_register_passphrase(
    user_service: UserService,
    register_passphrase: str,
    username: str,
) -> None:
    user = await user_service.register(UserCreate(tg_id=1234, username=username), register_passphrase)

    assert user.tg_id == 1234
    assert user.username == username


@pytest.mark.parametrize("register_passphrase,username", [("dfs", "naz")])
async def test_registration_with_incorrect_register_passphrase(
    user_service: UserService,
    register_passphrase: str,
    username: str,
) -> None:
    with pytest.raises(ValueError, match="Incorrect register passphrase!"):
        await user_service.register(UserCreate(tg_id=1234, username=username), register_passphrase)


@pytest.mark.parametrize("register_passphrase,username", [(None, "naz")])
async def test_registration_without_register_passphrase(
    user_service: UserService,
    register_passphrase: str,
    username: str,
) -> None:
    user = await user_service.register(UserCreate(tg_id=1234, username=username), register_passphrase)

    assert user.tg_id == 1234
    assert user.username == username


@pytest.mark.parametrize("register_passphrase,username", [("ASDF", None)])
async def test_registration_without_username(
    user_service: UserService,
    register_passphrase: str,
    username: str,
) -> None:
    with pytest.raises(ValidationError):
        await user_service.register(UserCreate(tg_id=1234, username=username), register_passphrase)

