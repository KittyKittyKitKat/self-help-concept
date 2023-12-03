from flask_wtf import FlaskForm
from wtforms.fields import EmailField, HiddenField, PasswordField, TextAreaField
from wtforms.validators import EqualTo, InputRequired


class LogInForm(FlaskForm):
    email = EmailField(
        'Email Address',
        validators=[
            InputRequired(),
        ],
    )
    password = PasswordField(
        'Password',
        validators=[
            InputRequired(),
        ],
    )


class SignUpForm(FlaskForm):
    email = EmailField(
        'Email Address',
        validators=[
            InputRequired(),
        ],
    )
    password = PasswordField(
        'Password',
        validators=[
            InputRequired(),
            EqualTo('password_confirm', message='Passwords must match'),
        ],
    )
    password_confirm = PasswordField(
        'Confirm Password',
        validators=[
            InputRequired(),
        ],
    )


class JournalEntryForm(FlaskForm):
    entry = TextAreaField(
        'Today\'s Entry',
        validators=[],
    )
    day_of_month = HiddenField()
