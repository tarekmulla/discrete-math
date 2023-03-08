# pylint: disable=wrong-import-position
'''Initialize the web application module module'''
from datetime import timedelta
from os import getenv, urandom
import logging
from flask import Flask, session  # type: ignore


app = Flask(__name__)

app.secret_key = str(getenv('APP_SECRET_KEY', urandom(12)))
app.logger.setLevel(logging.INFO)

# Templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True
app.config["SESSION_PERMANENT"] = True
app.permanent_session_lifetime = timedelta(minutes=300)


# Ensure responses aren't cached
@app.after_request
def after_request(response):
    '''after_request'''
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


from app import views  # noqa: E402
from app import modules  # noqa: E402
from app import html_helper  # noqa: E402

__all__ = ('views', 'modules', 'html_helper')
