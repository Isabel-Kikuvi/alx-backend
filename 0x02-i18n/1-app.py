#!/usr/bin/env python3
""" Basic Flask App"""

from flask import Flask, render_template
from flask_babel import Babel


class Config(object):
    """ Configuring language and timezone"""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
babel = Babel(app)
app.config.from_object(Config)

@app.route('/')
def index():
    """Method renders the index template"""
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run()
    