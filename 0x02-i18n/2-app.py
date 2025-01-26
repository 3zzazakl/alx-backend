#!/usr/bin/env python3
"""summary_line

Keyword arguments:
argument -- description
Return: return_description
"""

from flask import Flask, render_template, request
from flask_babel import Babel, _

app = Flask(__name__)

# Define Config class


class Config:
    """summary_line

    Keyword arguments:
    argument -- description
    Return: return_description
    """

    LANGUAGES = ['en', 'fr']  # Supported languages
    BABEL_DEFAULT_LOCALE = 'en'  # Default locale (language)
    BABEL_DEFAULT_TIMEZONE = 'UTC'  # Default timezone


# Set the app's configuration to use Config
app.config.from_object(Config)

# Initialize Babel
babel = Babel(app)

# Define the get_locale function with the localeselector decorator


@babel.localeselector
def get_locale():
    """summary_line

    Keyword arguments:
    argument -- description
    Return: return_description
    """

    # Use request.accept_languages to get the user's preferred language
    return request.accept_languages.best_match(app.config['LANGUAGES'])

# Set up a simple route to test localization


@app.route('/')
def index():
    """summary_line

    Keyword arguments:
    argument -- description
    Return: return_description
    """

    return render_template('2-index.html')


if __name__ == '__main__':
    """summary_line

    Keyword arguments:
    argument -- description
    Return: return_description
    """

    app.run(debug=True)
