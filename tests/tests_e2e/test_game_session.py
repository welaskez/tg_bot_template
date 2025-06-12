from core.models import User
from core.schemas.user import UserUpdate
from services.user import UserService


async def test_incr_taps(user: User, user_service: UserService) -> None:
    old_taps = user.taps
    updated_user = await user_service.update(user, UserUpdate(taps=old_taps + 1))

    assert updated_user is not None
    assert updated_user.taps == old_taps + 1
    assert updated_user.id == user.id
