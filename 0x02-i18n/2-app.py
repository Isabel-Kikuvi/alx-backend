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
app.url_map.strict_slashes = False
app.config.from_object(Config)


@babel.localeselector
def get_locale():
    """Determines the best locale based on user pref and supported lang."""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """Method renders the index template"""
    return render_template('2-index.html')


if __name__ == '__main__':
    app.run()
