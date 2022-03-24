#!/usr/bin/python3
""" adding second route to flask application """

from flask import Flask, render_template
from models.state import State
from models import storage
app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def stList():
    stateList = storage.all(State)
    return render_template('7-states_list.html', stateList=stateList)


@app.teardown_appcontext
def teardown(cont):
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')