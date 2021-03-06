# Users API for authentication
'''
   Users API for authentication
'''
from flask import (Blueprint, render_template, current_app, request,
                   flash, url_for, redirect, session, abort, jsonify)
from flask_babel import gettext as _

from flask_login import login_required, login_user, current_user, logout_user, confirm_login, login_fresh
from ..common import response
from ..extensions import db

from ..users import User, SignupForm, LoginForm

auth = Blueprint('auth', __name__, url_prefix='/api/auth')


@auth.route('/verify_auth', methods=['GET'])
@login_required
def verify_auth():
    return response.make_data_resp(data=current_user.to_json())


@auth.route('/login', methods=['POST'])
def login():
    """ POST only operation. check login form. Log user in """
    if current_user.is_authenticated:
        return response.make_success_resp(msg="You are already logged in")

    form = LoginForm()
    if form.validate_on_submit():
        user, authenticated = User.authenticate(form.login.data,
                                                form.password.data)
        if user:
            if authenticated:
                login_user(user, remember=form.remember_me.data)
                return response.make_data_resp(data=current_user.to_json(), msg="You have successfully logged in")
            else:
                return response.make_error_resp(msg="Invalid username or password", type="Wrong Authentication",
                                                code=422)
        else:
            return response.make_error_resp(msg="Username does not exist", type="Wrong Authentication", code=422)
    return response.make_form_error_resp(form=form)


@auth.route('/logout', methods=['POST'])
@login_required
def logout():
    """ logout user """
    session.pop('login', None)
    first_name = current_user.first_name
    logout_user()
    return response.make_success_resp(msg="Goodbye %s!" % first_name)


@auth.route('/signup', methods=['POST'])
def signup():
    if current_user.is_authenticated:
        return response.make_success_resp("You're already signed up")

    form = SignupForm()

    if form.validate_on_submit():
        # check if user_name or email is taken
        if User.is_user_name_taken(form.user_name.data):
            return response.make_error_resp(msg="This username is already taken!", code=409)
        if User.is_email_taken(form.email.data):
            return response.make_error_resp(msg="This email is already taken!", code=409)

        try:
            # create new user
            user = User()
            form.populate_obj(user)

            db.session.add(user)
            db.session.commit()

        except Exception as e:
            # flash(_('Exception thrown when signing up user\nException: %s' % str(e)), 'error')
            return response.make_exception_resp(exception=e)

        # log the user in
        login_user(user)
        return response.make_success_resp(
            msg="You successfully signed up! Please check your email for further verification.")

    return response.make_form_error_resp(form=form)
