#!/usr/bin/env python3
'''
Basic flask app with babel setup
'''
from flask import Flask, render_template, request
from flask_babel import Babel, _


class Config(object):
    '''
        Configuration for Babel
    '''
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale():
    '''
     To determine the best match with our supported languages.
    '''
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', strict_slashes=False)
def index() -> str:
    '''
        Index page - Handles / route
    '''
    return render_template('3-index.html')


if __name__ == '__main__':
    app.run(port="5000", host="0.0.0.0", debug=True)
