#!/usr/bin/python3
"""
    Basic route script with variable default value
    with jinja templating and sqlalchemy
"""
from models import storage
from flask import Flask, render_template
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/states')
@app.route('/states/<id>')
def states(id=None):
    """
        display the states and cities listed
        """
    states = storage.all("State")
    if id is not None:
        id = 'State.' + id
    return render_template('9-states.html', state_list=states, id=id)


@app.teardown_appcontext
def teardown(exc):
    """
        After each request you must remove
        the current SQLAlchemy Session
    """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000', debug=True)
