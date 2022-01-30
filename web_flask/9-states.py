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
def states():
    """
        Retern state object
        from route /states_list
    """
    states = storage.all("State")
    return render_template('9-states.html', state_list=states)


@app.route('/states')
@app.route('/states/<id>')
def states_id(id):
    """Displays an HTML page with info about <id>, if it exists."""
    for state in storage.all("State").values():
        if state.id == id:
            return render_template("9-states.html", state_list=state)
    return render_template("9-states.html")


@app.teardown_appcontext
def teardown(exc):
    """
        After each request you must remove
        the current SQLAlchemy Session
    """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000', debug=True)
