from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError
from flask import Request
from flask_login import UserMixin

from .. import login_manager, password_hasher


class User(UserMixin):
    def __init__(
        self,
        uuid: str,
        email: str,
        password: str,
        display_name: str,
    ):
        self.id = uuid
        self.uuid = uuid
        self.email = email
        self.password = password
        self.display_name = display_name


@login_manager.user_loader
def user_loader(uuid: str) -> User | None:
    from ..utils.db_utils import get_user_data_by_uuid

    if user_data := get_user_data_by_uuid(uuid):
        user = User(**user_data)
        return user
    return None


def validate_user_login(email: str, password: str) -> tuple[bool, str]:
    from ..utils.db_utils import get_user_data_by_email

    if (user_data := get_user_data_by_email(email)) is not None:
        try:
            password_hasher.verify(user_data['password'], password)
        except VerifyMismatchError:
            return (False, 'Incorrect Password')
        else:
            return (True, '')
    return (False, 'Unrecognized Email')
