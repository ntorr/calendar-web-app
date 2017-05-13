from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_wtf.csrf import CSRFProtect

# Flask-SQLAlchemy extension instance
db = SQLAlchemy()

# Flask-Login
login_manager = LoginManager()

# Flask-WTF CSRF protection
csrf = CSRFProtect()
