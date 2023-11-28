from flask import Blueprint, render_template

accounts = Blueprint('accounts', __name__)


@accounts.route('/signup')
def signup():
    return render_template('signup.html')


@accounts.route('/login')
def login():
    return render_template('login.html')
