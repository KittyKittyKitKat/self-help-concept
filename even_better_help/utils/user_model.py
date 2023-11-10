from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError
from flask import Request
from flask_login import UserMixin

import uuid

from .. import login_manager, password_hasher
from dataclasses import dataclass

@dataclass
class User(UserMixin):
    uuid: uuid.UUID
    email: str
    password: str
    display_name: str


@login_manager.user_loader
def user_loader(email: str) -> User | None:
    ...

@login_manager.request_loader
def request_loader(request: Request) -> User | None:
    ...