from flask import (Flask, Blueprint, render_template, current_app, request,
                   flash, url_for, redirect, session, abort, jsonify, send_from_directory)
from flask_login import login_required

frontend = Blueprint('frontend', __name__)


@frontend.route('/')
@frontend.route('/index')
def index():
    return render_template('index.html')


@frontend.route('/user/home')
@login_required
def user_home():
    return render_template('home.html')
