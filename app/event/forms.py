from flask_wtf import FlaskForm
from wtforms import (BooleanField, StringField, HiddenField, PasswordField,
                     validators, IntegerField, SubmitField)
from wtforms.fields.html5 import DateTimeField
from wtforms.widgets.html5 import DateTimeInput

from ..common.constants import MAX_DESCRIPTION_LEN, STRING_LEN
from ..common.helpers import get_current_time, get_nearest_time, get_nearest_time_plus


class NewEventForm(FlaskForm):
    event_name = StringField('event_name', [validators.DataRequired(), validators.Length(min=1, max=STRING_LEN)])
    date_fmt = '%Y-%m-%m %H:%M:%S'
    start_dt = DateTimeField('start_dt', [validators.DataRequired()], default=get_nearest_time(), format=date_fmt)
    end_dt = DateTimeField('end_dt', [validators.DataRequired()], default=get_nearest_time_plus(minutes=30),
                           format=date_fmt)
    show_as = StringField('show_as', [validators.DataRequired(), validators.AnyOf(['Free', 'Busy'])])
    description = StringField('description', [validators.Length(max=MAX_DESCRIPTION_LEN)], default=str())
    private = BooleanField('private', default=True)
