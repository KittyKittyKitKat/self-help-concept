from flask import Blueprint, render_template

from ..utils.db_utils import *
from ..utils.user_model import *

core = Blueprint('core', __name__)
from datetime import date


@core.route('/')
def calendar():
    return render_template('calendar.html')
