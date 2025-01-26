#!/usr/bin/env python3
"""Flask web application"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index() -> str:
    """Renders the index page"""
    return render_template('0-index.html')


if __name__ == "__main__":
    """summary_line

    Keyword arguments:
    argument -- description
    Return: return_description
    """

    app.run(port="5000", host="0.0.0.0", debug=True)
