#!/usr/bin/python3
"""
    Basic roue script
"""
from flask import Flask
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_hbnb():
    """
        Return HBNB! from
        http://192.168.1.11:5000/
    """
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    """
        Return HBNB from
        http://192.168.1.11:5000/hbnb
    """
    return 'HBNB'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000', debug=True)
