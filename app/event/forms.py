from flask_wtf import FlaskForm
from wtforms import (BooleanField, StringField, HiddenField, PasswordField,
                     DateTimeField, validators, IntegerField, SubmitField)

from ..common.constants import MAX_DESCRIPTION_LEN, STRING_LEN
from ..common.helpers import get_current_time, get_nearest_time, get_nearest_time_plus


class NewEventForm(FlaskForm):
    event_name = StringField('event_name', [validators.DataRequired(), validators.Length(min=1, max=STRING_LEN)])
    start_dt = DateTimeField('start_dt', [validators.DataRequired()], default=get_nearest_time())
    end_dt = DateTimeField('end_dt', [validators.DataRequired()], default=get_nearest_time_plus(minutes=30))
    show_as = StringField('show_as', [validators.DataRequired(), validators.AnyOf(['Free', 'Busy'])])
    description = StringField('description', [validators.Length(max=MAX_DESCRIPTION_LEN)], default=str())
    private = BooleanField('private', default=True)
