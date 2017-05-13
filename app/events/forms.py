from flask_wtf import FlaskForm
from wtforms import (BooleanField, StringField, HiddenField, PasswordField,
                     DateTimeField, validators, IntegerField, SubmitField, SelectField)


class CreateEventForm(FlaskForm):
    event_name = StringField('event_name', [validators.DataRequired()])
    start_datetime = DateTimeField('start_datetime', [validators.DataRequired()])
    end_datetime = DateTimeField('end_datime', [validators.DataRequired()])
    show_as = SelectField('show_as', choices=['Busy', 'Free', 'Tentative'])
    user_name = StringField('user_name', [validators.DataRequired()])
    description = StringField('description', [validators.Optional()])
