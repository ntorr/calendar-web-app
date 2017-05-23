from ..extensions import db
from ..common.constants import STRING_LEN, MAX_USERNAME_LEN, MAX_DESCRIPTION_LEN
from ..common.helpers import JsonSerializer, get_current_time, get_nearest_time, get_nearest_time_plus


class UserEvent(db.Model, JsonSerializer):
    __tablename__ = "user_events"

    def __repr__(self):
        return '<Event %r>' % (self.event_name)

    id = db.Column(db.Integer, primary_key=True)
    event_name = db.Column(db.String(STRING_LEN), nullable=False)
    start = db.Column(db.DateTime, nullable=False, default=get_nearest_time())
    end = db.Column(db.DateTime, nullable=False, default=get_nearest_time_plus(minutes=30))
    show_as = db.Column(db.String(STRING_LEN), nullable=False)
    private = db.Column(db.Boolean, nullable=False, default=True)
    created = db.Column(db.DateTime, nullable=False, default=get_current_time)
    user_name = db.Column(db.String(MAX_USERNAME_LEN), nullable=False)
    description = db.Column(db.String(MAX_DESCRIPTION_LEN), nullable=True)

