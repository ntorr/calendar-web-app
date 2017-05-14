from flask import (Flask, Blueprint, render_template, current_app, request,
                   flash, url_for, redirect, session, abort, jsonify, send_from_directory)

frontend = Blueprint('frontend', __name__)


@frontend.route('/index.html')
@frontend.route('/')
def index():
    return render_template('index.html')


@frontend.route('/home.html')
def home():
    return render_template('home.html')
