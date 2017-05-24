
from flask import (Blueprint, render_template, current_app, request,
                   flash, url_for, redirect, session, abort, jsonify)
from flask_login import login_required, current_user

from ..extensions import db
from ..common import response
from ..event.forms import NewEventForm
from ..event.models import UserEvent

event = Blueprint('event', __name__, url_prefix='/api/event')


@event.route('/<int:id>', methods=['GET'])
@event.route('/get/<int:id>', methods=['GET'])
@login_required
def get_event(id=None):
    if not id:
        return response.make_error_resp(msg="Could not find event with id = %s " % str(id), type="Not Found", code=404)
    return response.make_success_resp(msg='%s' % str(id))


@event.route('/delete/<int:id>', methods=['GET'])
@login_required
def delete_event(id):
    if not id:
        return response.make_error_resp(msg="Could not find event with id = %s " % str(id), type="Not Found", code=404)
    try:
        evt = UserEvent.query.get(id)
        db.session.delete(evt)
        db.session.commit()
    except Exception as e:
        return response.make_exception_resp(exception=e)

    return response.make_success_resp(msg='%s' % str(id))


@event.route('/create', methods=['POST'])
@login_required
def create_event():
    form = NewEventForm()
    if form.validate_on_submit():
        try:
            evt = UserEvent()
            form.populate_obj(evt)

            evt.user_name = current_user.user_name

            db.session.add(evt)
            db.session.commit()

        except Exception as e:
            return response.make_exception_resp(exception=e)

        return response.make_success_resp(msg='Event created!')

    return response.make_form_error_resp(form, msg='Something went wrong. Please check your input.')
