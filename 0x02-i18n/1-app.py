#!/usr/bin/env python3
"""summary_line

Keyword arguments:
argument -- description
Return: return_description
"""

from flask import Flask, render_template
from flask_babel import Babel

# Create Flask app instance
app = Flask(__name__)

# Define Config class


class Config:
    """summary_line

    Keyword arguments:
    argument -- description
    Return: return_description
    """

    LANGUAGES = ['en', 'fr']  # Available languages: English and French
    BABEL_DEFAULT_LOCALE = 'en'  # Default locale (language)
    BABEL_DEFAULT_TIMEZONE = 'UTC'  # Default timezone


# Set the app's configuration to use Config
app.config.from_object(Config)

# Initialize Babel
babel = Babel(app)

# Set up a simple route


@app.route('/')
def index():
    """summary_line

    Keyword arguments:
    argument -- description
    Return: return_description
    """

    return render_template('1-index.html')


# Run the app
if __name__ == '__main__':
    """summary_line

    Keyword arguments:
    argument -- description
    Return: return_description
    """
    app.run(debug=True)
