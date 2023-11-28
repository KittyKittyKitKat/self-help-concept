from dataclasses import dataclass

from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError
from flask import Request
from flask_login import UserMixin

from .. import login_manager, password_hasher


@dataclass
class User(UserMixin):
    uuid: str
    email: str
    password: str
    display_name: str


@login_manager.user_loader
def user_loader(email: str) -> User | None:
    from .db_utils import get_user_data_by_email

    if user_data := get_user_data_by_email(email):
        user = User(**user_data)
        return user
    return None


@login_manager.request_loader
def request_loader(request: Request) -> User | None:
    from .db_utils import get_user_data_by_email

    email = request.form.get('email')
    if email is None:
        return None
    if user_data := get_user_data_by_email(email):
        user = User(**user_data)
        return user
    return None
