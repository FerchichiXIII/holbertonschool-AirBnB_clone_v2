#!/usr/bin/python3
"""flask app"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ Hello HBNB """
    return 'Hello HBNB!'


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """ Hello HBNB """
    return 'HBNB'


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    """ Hello HBNB """
    text = text.replace('_', ' ')
    return 'C {}'.format(text)


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python(text="is cool"):
    """ Hello HBNB """
    text = text.replace('_', ' ')
    return 'Python {}'.format(text)


if "__main__" == __name__:
    app.run(host='0.0.0.0', port=5000)
