from ..common.helpers import JsonSerializer, get_current_time, get_current_time_plus
from ..extensions import db
from .constants import MAX_COMMENT_LEN, MAX_EVENT_NAME_LEN, MAX_STRING_LEN


class Event(db.Model, JsonSerializer):
    __tablename__ = "events"

    id = db.Column(db.Integer, primary_key=True, unique=True)
    user_name = db.Column(db.String(MAX_STRING_LEN), nullable=False)
    event_name = db.Column(db.String(MAX_EVENT_NAME_LEN), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=get_current_time())
    start_datetime = db.Column(db.DateTime, nullable=False, default=get_current_time_plus(minutes=15))
    end_datetime = db.Column(db.DateTime, nullable=False, default=get_current_time())
    show_as = db.Column(db.String(MAX_STRING_LEN), nullable=False, default='Busy')
    description = db.Column(db.String(MAX_COMMENT_LEN), nullable=True)

