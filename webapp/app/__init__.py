# type: ignore
# pylint: disable=import-error,wrong-import-position
'''Initialize the web application module module'''
from datetime import timedelta
from os import getenv, urandom
from tempfile import mkdtemp
import logging
from flask import Flask, session


app = Flask(__name__)

app.secret_key = str(getenv('APP_SECRET_KEY', urandom(12)))
app.logger.setLevel(logging.INFO)

# Templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True
# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"


@app.before_request
def before_request():
    '''make session permanent'''
    session.permanent = True
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
__all__ = ('views',)
