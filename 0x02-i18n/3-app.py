#!/usr/bin/env python3
"""sumary_line

Keyword arguments:
argument -- description
Return: return_description
"""

from flask import Flask, render_template
from flask_babel import Babel, _

app = Flask(__name__)

# Define Config class


class Config:
    """sumary_line

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
    """
    This function selects the best language match for the user's request.

    It uses the 'accept_languages' header from the request to determine the 
    preferred language. The '_()' function provided by Flask-Babel is used 
    to mark strings for translation based on the selected locale.

    Returns:
        str: The best matching language code (e.g., 'en' or 'fr').
    """
    # Use request.accept_languages to get the user's preferred language
    return request.accept_languages.best_match(app.config['LANGUAGES'])

# Define the route and add translations


@app.route('/')
def index():
    """
    This route renders the main page with the translated content.

    The text on this page is wrapped in the '_()' function to mark it for
    translation, based on the user's selected locale.
    """
    return render_template('3-index.html')


if __name__ == '__main__':
    app.run(debug=True)
