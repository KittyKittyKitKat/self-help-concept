import calendar as calendar_py
from datetime import date

from flask import Blueprint, abort, flash, redirect, render_template, request, url_for
from flask_login import current_user, login_required, login_user, logout_user

from .. import login_manager
from ..utils.db_utils import (
    add_date_data_to_user,
    create_new_user,
    get_dates_data_by_user,
    get_user_data_by_email,
)
from ..utils.forms import JournalEntryForm, LogInForm, SignUpForm
from ..utils.user_model import User, validate_user_login

core = Blueprint('core', __name__)
login_manager.login_view = 'core.login'


@core.route('/calendar', methods=['GET', 'POST'])
@login_required
def calendar() -> str:
    year = request.args.get('year')
    month = request.args.get('month')
    try:
        year = int(year) if year else date.today().year
        month = int(month) if month else date.today().month
    except ValueError:
        abort(404)

    user_journal_data = list(
        filter(
            lambda r: r['year'] == year and r['month'] == month,
            get_dates_data_by_user(current_user),
        )
    )

    journal_entry_form = JournalEntryForm()
    if journal_entry_form.validate_on_submit():
        add_date_data_to_user(
            current_user,
            month,
            journal_entry_form.day_of_month.data,
            year,
            journal_entry_form.entry.data,
        )

    return render_template(
        'calendar.html',
        calendar=calendar_py,
        year=year,
        month=month,
        form=journal_entry_form,
        user_journal_data=user_journal_data,
    )


@core.route('/sign-up', methods=['GET', 'POST'])
def signup() -> str:
    sign_up_form = SignUpForm()

    if sign_up_form.validate_on_submit():
        print(sign_up_form.data)
        create_new_user(
            sign_up_form.email.data,
            sign_up_form.password.data,
            sign_up_form.email.data,
        )
        login_user(
            User(
                **get_user_data_by_email(
                    sign_up_form.email.data
                )
            )
        )

    return render_template('signup.html', form=sign_up_form)


@core.route('/', methods=['GET', 'POST'])
@core.route('/login', methods=['GET', 'POST'])
def login() -> str:
    log_in_form = LogInForm()

    if log_in_form.validate_on_submit():
        email = log_in_form.email.data
        success, msg = validate_user_login(email, log_in_form.password.data)
        if success:
            # If the validation was a success, then the user must be in the
            # database, so get_user_data_by_email be not None
            user = User(**get_user_data_by_email(email))  # type: ignore
            if login_user(user):
                flash('Signed in successfully', category='info')
                return redirect(url_for('core.calendar'))
            else:
                flash('Signed in failed', category='danger')
        else:
            flash(f'Could not sign in user: {msg}', category='danger')

    elif log_in_form.is_submitted():
        flash(f'Something went wrong trying to sign you in.', category='danger')

    return render_template('login.html', form=log_in_form)


@core.route('/sign-out')
def logout() -> str:
    if current_user.is_authenticated:
        logout_user()
        flash('Signed out successfully', category='info')
    return redirect(url_for('core.login'))
