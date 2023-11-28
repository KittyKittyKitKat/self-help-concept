import sqlite3 as sql
from datetime import date
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

    cur.execute(
        'INSERT INTO users VALUES(?, ?, ?, ?);',
        (
            str(create_uuid()),
            email,
            password,
            display_name,
        ),
    )
    con.commit()


def update_user_email(user: User, new_email: str):
    """Update a user's email."""
    con = get_db()
    cur = con.cursor()

    cur.execute('UPDATE users SET email = ? WHERE uuid = ?', (new_email, user.uuid))
    con.commit()


def update_user_password(user: User, new_password: str):
    """Update a user's password."""
    con = get_db()
    cur = con.cursor()

    cur.execute(
        'UPDATE users SET password = ? WHERE uuid = ?', (new_password, user.uuid)
    )
    con.commit()


def update_user_display_name(user: User, new_display_name: str):
    """Update a user's display name."""
    con = get_db()
    cur = con.cursor()

    cur.execute(
        'UPDATE users SET display_name = ? WHERE uuid = ?',
        (new_display_name, user.uuid),
    )
    con.commit()


def get_user_data_by_email(email: str) -> dict[str, Any] | None:
    con = get_db()
    cur = con.cursor()

    data = cur.execute(
        'SELECT * FROM users WHERE Email = ?',
        (email,),
    ).fetchone()
    return data


def get_dates_data_by_user(user: User) -> list[dict[str, Any]]:
    con = get_db()
    cur = con.cursor()

    data = cur.execute(
        'SELECT * FROM dates WHERE uuid = ?',
        (user.uuid,),
    ).fetchall()
    return data


def add_date_data_to_user(user: User, date: date, entry_text: str) -> None:
    con = get_db()
    cur = con.cursor()

    cur.execute(
        'INSERT INTO dates VALUES(?, ?, ?);',
        (
            user.uuid,
            str(date),
            entry_text,
        ),
    )
    con.commit()
