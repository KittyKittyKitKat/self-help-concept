from secrets import token_urlsafe

from argon2 import PasswordHasher
from flask import Flask
from flask_login import LoginManager
from flask_wtf import CSRFProtect

login_manager = LoginManager()
password_hasher = PasswordHasher()


def create_app():
    app = Flask(__name__)
    # csrf = CSRFProtect(app)
    # app.config['CSRF'] = csrf
    app.secret_key = token_urlsafe(32)  # TODO: extract into config file
    login_manager.init_app(app)
    from even_better_help.core.routes import core
    from even_better_help.errors.handlers import errors

    app.register_blueprint(core)
    app.register_blueprint(errors)
    return app
