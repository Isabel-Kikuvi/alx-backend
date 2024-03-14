#!/usr/bin/env python3
""" Simple flask application """

from flask import Flask, render_template, request
from flask_babel import Babel, _


class Config(object):
    """ Configuring language and timezones"""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False
babel = Babel(app)


@babel.localeselector
def get_locale():
    """ Determines the best locale based on user pref and supported lang."""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def hello():
    """Method renders the index template"""
    return render_template('3-index.html')


if __name__ == '__main__':
    app.run(port="5000", host='0.0.0.0', debug=True)