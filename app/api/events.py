# Events API for creating, updating and viewing calendar events
"""
    Events API for creating, updating and viewing calendar events
"""
from flask import (Blueprint, render_template, current_app, request,
                   flash, url_for, redirect, session, abort, jsonify)

from flask_login import login_required, current_user

from ..events.forms import CreateEventForm
from ..events.models import Event
from ..extensions import db
from ..common import response

events = Blueprint('events', __name__, url_prefix='/api/events')


@events.route('/create', methods=['POST'])
@login_required
def create():
    form = CreateEventForm()
    if form.validate_on_submit():
        print('validated form')
        event = Event(user_name=current_user.name)
        form.populate_obj(event)
        print(event)

        db.session.add(event)
        db.session.commit()

        return response.make_data_resp(event, 'Event created!')

    return response.make_form_error_resp(form)
