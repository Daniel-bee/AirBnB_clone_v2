#!/usr/bin/python3
"""
    Flask basic route
"""
from flask import Flask
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_hbnb():
    """
        Returns Hello HBNB! from
        http://192.168.1.11:5000/
    """
    return 'Hello HBNB!'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000', debug=True)
