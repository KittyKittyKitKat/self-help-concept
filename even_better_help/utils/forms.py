from flask_wtf import FlaskForm
from wtforms.fields import BooleanField, EmailField, PasswordField
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
            EqualTo('email_confirm_r', message='Emails must match'),
        ],
    )
    password = PasswordField(
        'Password',
        validators=[
            InputRequired(),
            EqualTo('password_confirm_r', message='Passwords must match'),
        ],
    )
    password_confirm = PasswordField(
        'Confirm Password',
        validators=[
            InputRequired(),
        ],
    )
