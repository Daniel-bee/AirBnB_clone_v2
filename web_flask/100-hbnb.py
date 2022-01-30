#!/usr/bin/python3
"""
    Basic route script with variable default value
    with jinja templating and sqlalchemy
"""
from models import storage
from flask import Flask, render_template
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/hbnb")
def hbnb():
    """
        Display a HTML page like 6-index.html,
        which was done during the project 
        0x01.AirBnB clone - Web static
    """
    states = storage.all("State")
    amenities = storage.all("Amenity")
    return render_template("10-hbnb_filters.html",
                           states=states, amenities=amenities)


@app.teardown_appcontext
def teardown(exc):
    """
        After each request you must remove
        the current SQLAlchemy Session
    """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000', debug=True)
