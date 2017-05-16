from flask import (Flask, Blueprint, render_template, current_app, request,
                   flash, url_for, redirect, session, abort, jsonify, send_from_directory)

frontend = Blueprint('frontend', __name__)


@frontend.route('/')
@frontend.route('/index')
def index():
    return render_template('index.html')


@frontend.route('/user/<path>/home')
def user_home():
    return render_template('home.html')
