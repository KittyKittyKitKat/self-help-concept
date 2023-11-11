import sqlite3 as sql
from pathlib import Path
from typing import Any
from uuid import uuid4 as create_uuid

from flask import current_app, g

from .user_model import User

USER_TABLE_NAME_FORMAT = 'DATES:{}'


def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


class UserLookUpError(Exception):
    pass


class UserAttributeError(Exception):
    pass


def get_db() -> sql.Connection:
    db: sql.Connection | None = getattr(g, '_database', None)
    if db is None:
        assert isinstance(current_app.static_folder, str)
        con = sql.connect(Path(current_app.static_folder) / 'database.db')
        con.row_factory = dict_factory
        db = g._database = con
    return db


def create_new_user(email: str, password: str, display_name: str):
    """Creates a new user in the database.

    Arguments:
        email: User email
        password: User password
        display_name: User display name.

    """
    con = get_db()
    cur = con.cursor()

    new_user_uuid = str(create_uuid())
    new_user_data = [
        new_user_uuid,
        email,
        password,
        display_name,
    ]

    cur.execute(
        'INSERT INTO users VALUES(?, ?, ?, ?);',
        new_user_data,
    )

    user_date_table_name = USER_TABLE_NAME_FORMAT.format(new_user_uuid)
    cur.execute(
        'CREATE TABLE IF NOT EXISTS ? (Date TEXT PRIMARY KEY, Main_text TEXT, Attachment BLOB)',
        (user_date_table_name,),
    )
    con.commit()


def update_user_email(user: User, email: str):
    """Update a user's email."""
    con = get_db()
    cur = con.cursor()


def update_user_password(user: User, password: str):
    """Update a user's password."""
    con = get_db()
    cur = con.cursor()


def update_user_display_name(user: User, display_name: str):
    """Update a user's display name."""
    con = get_db()
    cur = con.cursor()


def get_user_data_by_email(email: str) -> dict[str, Any] | None:
    con = get_db()
    cur = con.cursor()
    data = cur.execute(
        'SELECT * FROM users WHERE email = ?',
        (email,),
    ).fetchone()
    if data is None:
        return None
    return data[0]


def get_dates_data_by_user(user: User) -> dict[str, Any] | None:
    ...