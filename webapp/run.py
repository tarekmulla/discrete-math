'''The entry point to the web app'''
from os import getenv
from app import app


if __name__ == "__main__":
    app_port = int(getenv('APP_PORT', '80'))
    app_address = str(getenv('APP_ADDRESS', '0.0.0.0'))
    from waitress import serve
    serve(app, host=app_address, port=app_port)
