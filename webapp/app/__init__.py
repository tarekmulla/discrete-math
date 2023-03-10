# pylint: disable=wrong-import-position, cyclic-import
"""Initialize the web application module module"""
import logging
from os import getenv, urandom

from flask import Flask  # type: ignore


def create_app():
    """create flask application"""
    flask_app = Flask(__name__)

    flask_app.secret_key = str(getenv("APP_SECRET_KEY", urandom(12)))
    flask_app.logger.setLevel(logging.INFO)  # pylint: disable=no-member

    # Templates are auto-reloaded
    flask_app.config["TEMPLATES_AUTO_RELOAD"] = True

    return flask_app


app = create_app()

from app import html_helper  # noqa: E402
from app import modules  # noqa: E402
from app import views  # noqa: E402

__all__ = ("views", "modules", "html_helper")
