from flask_wtf import FlaskForm
from wtforms import (BooleanField, StringField, HiddenField, PasswordField,
                     DateTimeField, validators, IntegerField, SubmitField)

from ..common.constants import MIN_USERNAME_LEN, MAX_USERNAME_LEN, MIN_PASSWORD_LEN, MAX_PASSWORD_LEN


class LoginForm(FlaskForm):
    login = StringField('user_name', [validators.DataRequired()])
    password = StringField('password', [validators.DataRequired()])
    remember_me = BooleanField('remember_me', default=False)


class SignupForm(FlaskForm):
    user_name = StringField('user_name', [
        validators.Length(
            min=MIN_USERNAME_LEN,
            max=MAX_USERNAME_LEN
        ),
        validators.Regexp(
            "^[a-zA-Z0-9]*$",
            message="Username can only contain letters and numbers"
        )
    ])
    first_name = StringField('first_name', [validators.DataRequired()])
    last_name = StringField('last_name', [validators.DataRequired()])
    email = StringField('email', [validators.DataRequired(), validators.Email()])
    password = PasswordField(
        'New Password',
        [validators.Length(min=MIN_PASSWORD_LEN, max=MAX_PASSWORD_LEN)]
    )
    confirm = PasswordField('Repeat Password', [
        validators.DataRequired(),
        validators.EqualTo('password', message='Passwords must match')
    ])
