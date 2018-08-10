import os
import flask
from flask import render_template, redirect, url_for, request
from config import DEPLOY_DIR, DB_PROVIDER, DB_CONFIG

app = flask.Flask(__name__)

from models import db, db_session, Event

@app.route('/')
def events():
    with db_session:
        data = [{ 'date': e.date, 'type': e.type}
                for e in Event.select()]
    return render_template('events.html', data=data)

@app.route('/create', methods=['POST'])
def event_create():
    # Check to see if we are on the Raspberry Pi
    if os.uname()[4][:3] == 'arm':
        from gpiozero import LED
        led = LED(17)
        if request.form['type'] == 'LED ON':
            led.on()
        elif request.form['type'] == 'LED OFF':
            led.off()

    with db_session:
        Event(type=request.form['type'])
    return redirect(url_for('events'))


def run(*args, **kwargs):
    if not os.path.exists(DEPLOY_DIR):
        os.makedirs(DEPLOY_DIR)
    db.bind(DB_PROVIDER, **DB_CONFIG)
    db.generate_mapping(create_tables=True)
    return app.run(*args, **kwargs)

run(debug=True, host="0.0.0.0", port=3000)
