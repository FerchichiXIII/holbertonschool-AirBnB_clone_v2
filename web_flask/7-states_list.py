#!/usr/bin/python3
"""
Write a script that starts a Flask web application
"""


from flask import Flask
from flask import render_template
from models import storage


app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """Return a HTML page with all states"""
    states = storage.all("State")
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def close_s(excetpion):
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
