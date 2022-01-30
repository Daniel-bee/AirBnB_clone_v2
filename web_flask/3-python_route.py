#!/usr/bin/python3
"""
    Basic route script with variable default value
"""
from flask import Flask
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_hbnb():
    """
        Return Hello HBNB! from
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


@app.route('/c/<text>')
def c_fun(text):
    """
        Return C <text> from
        http://192.168.1.11:5000/c/<text>
    """
    if '_' in list(text):
        return 'C '+text.replace("_", " ")
    return 'C '+text


@app.route('/python')
@app.route('/python/<text>')
def python(text='is cool'):
    """
        Return C <text> from
        http://192.168.1.11:5000/python/<text>
    """
    if '_' in list(text):
        return 'Python '+text.replace("_", " ")
    return 'Python '+text


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000', debug=True)
