from flask import render_template
from . import main

@main.app_errorhandler(404)
def news(error):
    return render_template('news.html'),404