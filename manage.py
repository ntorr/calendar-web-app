from flask_script import Manager, Shell, Server
from flask import current_app
from app import create_app
from app.extensions import db
import app.models as Models
from app.config import DefaultConfig


def create_my_app(config=DefaultConfig):
    return create_app(config)


manager = Manager(create_my_app)

# runs Flask development server locally at port 5000
manager.add_command("runserver", Server(host="0.0.0.0", port=5000))


# start a Python shell with contexts of the Flask application
@manager.shell
def make_shell_context():
    return dict(app=current_app, db=db, models=Models)


@manager.option('--user_name', help='User name')
def delete_user(user_name):
    Models.User.query.filter(Models.User.user_name == user_name).delete()
    db.session.commit()


@manager.option('--user_name', help='User name')
@manager.option('--first_name', help='User\'s first name')
@manager.option('--last_name', help='User\'s last name')
@manager.option('--email', help='User\'s e-mail address')
@manager.option('--password', help='Temporary password')
def add_user(user_name, first_name, last_name, email, password):
    user = Models.User(**locals())
    db.session.add(user)
    db.session.commit()


# init/reset database
@manager.command
def initdb():
    db.drop_all(bind=None)
    db.create_all(bind=None)

    # add sample user
    user = Models.User(
        first_name=u'Sam',
        last_name=u'Chuang',
        user_name=u'spchuang',
        password=u'123456',
        email=u"test@gmail.com")
    db.session.add(user)
    db.session.commit()


@manager.command
def create_test_event():
    db.create_all(bind=None)

    event = Models.Event(
        user_name='ntorr',
        event_name='Test Event',
        description='This is a test event',
        show_as='Tentative'
    )
    db.session.add(event)
    db.session.commit()


if __name__ == "__main__":
    manager.run()
