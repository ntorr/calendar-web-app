from werkzeug.security import generate_password_hash, check_password_hash

from sqlalchemy.exc import OperationalError
from flask_login import UserMixin
from ..common.helpers import JsonSerializer, get_current_time
from ..extensions import db

from .constants import STRING_LEN, USER, PW_STRING_LEN, USER_ROLE


class UserJsonSerializer(JsonSerializer):
    __json_public__ = ['id', 'email', 'user_name', 'first_name']
    __json_modifiers__ = {
        'role_code': ['role', (lambda code: USER_ROLE[code])]
    }


class User(db.Model, UserMixin, UserJsonSerializer):
    __tablename__ = "user"

    def __repr__(self):
        return '<User %r>' % (self.user_name)

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(STRING_LEN), nullable=False)
    last_name = db.Column(db.String(STRING_LEN), nullable=False)
    user_name = db.Column(db.String(STRING_LEN), index=True, unique=True, nullable=False)
    email = db.Column(db.String(STRING_LEN), index=True, unique=True, nullable=False)
    created_on = db.Column(db.DateTime, nullable=False, default=get_current_time)
    role_code = db.Column(db.SmallInteger, default=USER, nullable=False)

    # User Password
    _password = db.Column('password', db.String(PW_STRING_LEN), nullable=False)

    def _get_password(self):
        return self._password

    def _set_password(self, password):
        self._password = generate_password_hash(password)

    password = db.synonym('_password',
                          descriptor=property(_get_password,
                                              _set_password))

    def check_password(self, password):
        if self.password is None:
            return False
        return check_password_hash(self.password, password)

    # methods
    @classmethod
    def authenticate(cls, user_name, password):
        user = User.query.filter(db.or_(User.user_name == user_name)).first()

        if user:
            authenticated = user.check_password(password)
        else:
            authenticated = False
        return user, authenticated

    @classmethod
    def is_user_name_taken(cls, user_name):
        try:
            return db.session.query(db.exists().where(User.user_name == user_name)).scalar()
        except OperationalError:
            return False

    @classmethod
    def is_email_taken(cls, email_address):
        try:
            return db.session.query(db.exists().where(User.email == email_address)).scalar()
        except OperationalError:
            return False
