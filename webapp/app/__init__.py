# type: ignore
# pylint: disable=import-error,wrong-import-position
'''Initialize the web application module module'''
from os import getenv, urandom
from flask import Flask

app = Flask(__name__)

app.secret_key = str(getenv('APP_SECRET_KEY', urandom(12)))

from app import views  # noqa: E402
__all__ = ('views',)
