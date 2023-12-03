from flask import Blueprint, flash, redirect, render_template, url_for
from flask_login import current_user, login_user, logout_user

from .. import login_manager
from ..utils.db_utils import *
from ..utils.forms import *
from ..utils.user_model import *

core = Blueprint('core', __name__)
from datetime import date

login_manager.login_view = 'accounts.login'


@core.route('/')
@core.route('/home')
def home():
    return render_template('calendar.html')


@core.route('/sign-up')
def signup():
    sign_up_form = SignUpForm()

    if sign_up_form.validate_on_submit():
        create_new_user(
            sign_up_form.email.data,
            sign_up_form.password.data,
        )
    else:
        print(sign_up_form.errors)

    return render_template('signup.html', form=sign_up_form)


@core.route('/login')
def login():
    log_in_form = SignUpForm()

    if log_in_form.validate_on_submit():
        email = log_in_form.email.data
        success, msg = validate_user_login(email, log_in_form.password.data)
        if success:
            # If the validation was a success, then the user must be in the
            # database, so get_user_data_by_email be not None
            user = User(**get_user_data_by_email(email))  # type: ignore
            if login_user(user):
                flash('Signed in successfully', category='info')
                return redirect(url_for('core.home'))
            else:
                flash('Signed in failed', category='danger')
        else:
            flash(f'Could not sign in user: {msg}', category='danger')

    if log_in_form.validate_on_submit():
        user = User(**get_user_data_by_email(log_in_form.email))
        login_user(user)

    return render_template('login.html', form=log_in_form)


@core.route('/sign-out')
def logout() -> str:
    if current_user.is_authenticated:
        logout_user()
        flash('Signed out successfully', category='info')
    return redirect(url_for('core.home'))
