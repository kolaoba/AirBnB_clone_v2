#!/usr/bin/python3
"""starts a Flask web application"""
from flask import Flask, abort
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """print hello hbnb"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """prints hbnb"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_route(text):
    """print C + <name> with underscore"""
    return ("C {}".format(text.replace("_", " ")))


@app.route('/python/', strict_slashes=False)
@app.route('/python', strict_slashes=False)
def python_only():
    """Print Python is cool by default"""
    return ("Python is cool")


@app.route('/python/<text>', strict_slashes=False)
def python_route(text):
    """print Python + <text>"""
    return ("Python {}".format(text.replace("_", " ")))


@app.route('/number/<n>', strict_slashes=False)
def print_number(n):
    """Print a number if is a number"""
    if n.isdigit():
        return ("{} is a number".format(n))
    else:
        abort(404)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
