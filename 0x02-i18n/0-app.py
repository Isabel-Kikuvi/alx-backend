#!/usr/bin/env python3
""" Basic Flask App"""

from flask import Flask, render_template
from flask_babel import Babel
from config import Config


app = Flask(__name__)
babel = Babel(app)
app.config.from_object(Config)


@app.route('/')
def index():
    """Method renders the index template"""
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run()
