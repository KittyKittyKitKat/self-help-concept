import sqlite3 as sql
from .user_model import User
from flask import current_app, g
from pathlib import Path


class UserLookUpError(Exception):
    pass


class UserAttributeError(Exception):
    pass


def get_db() -> sql.Cursor:
    db: sql.Cursor | None = getattr(g, '_database', None)
    if db is None:
        assert isinstance(current_app.static_folder, str)
        con = sql.connect(
            Path(current_app.static_folder) / 'database.db'
        )
        cur = con.cursor()
        db = g._database = cur
    return db


def create_new_user(email: str, password: str, display_name: str):
    """Creates a new user in the database.

    Arguments:
        email: User email
        password: User password
        display_name: User display name.

    """
    cur = get_db()


def update_user_email(user: User, email: str):
    """Update a user's email.
    """
    cur = get_db()


def update_user_password(user: User, password: str):
    """Update a user's password.
    """
    cur = get_db()


def update_user_display_name(user: User, display_name: str):
    """Update a user's display name.
    """
    cur = get_db()