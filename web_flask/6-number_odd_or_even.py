#!/usr/bin/python3
""" adding second route to flask application """

from flask import Flask, render_template
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    no_ = text.replace('_', ' ')
    return 'C %s' % no_


@app.route("/python/", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python(text='is cool'):
    no_ = text.replace('_', ' ')
    return 'Python %s' % no_


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    return '%d is a number' % n


@app.route("/number_template/<int:n>", strict_slashes=False)
def numberHtml(n):
        return render_template('templates/5-number.html', n=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def numberEorO(n):
    if n % 2 == 0:
        eORo = 'even'
    else:
        eORo = 'odd'
    return render_template('templates/6-number_odd_or_even.html', n=n, eORo=eORo)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
