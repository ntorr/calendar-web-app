from flask import (Flask, Blueprint, render_template, current_app, request,
                   flash, url_for, redirect, session, abort, jsonify, send_from_directory)
from flask_login import login_required, current_user

frontend = Blueprint('frontend', __name__)


@frontend.route('/')
@frontend.route('/index')
@frontend.route('/<path:path>')
def index(path=None):
    if current_user.is_authenticated:
        return render_template('index.html', current_user=current_user)
    return render_template('index.html', current_user=None)
