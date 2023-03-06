# pylint: disable=import-error
'''views file'''
from functools import wraps
from tempfile import mkdtemp
from enum import Enum
from json import loads
from app import app
from app.api import generate_questions
from app.auth import get_session_details
from flask import render_template, request, session, redirect
from os import environ
import ast


# Templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True
# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"


# Ensure responses aren't cached
@app.after_request
def after_request(response):
    '''after_request'''
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


# Create dictionary for navbar and make it global for all templates
href_dict = {
    'Home': '/',
    'About': '/about'
    }

COGNITO_DOMAIN = f'cognito.{environ["website_domain"]}'
COGNITO_CLIENT_ID = environ['cognito_client_id']
CALLBACK_URLS = ast.literal_eval(environ['callback_urls'])
LOGOUT_URLS = ast.literal_eval(environ['logout_urls'])

LOGIN_URL = f'https://{COGNITO_DOMAIN}/oauth2/authorize?client_id={COGNITO_CLIENT_ID}&response_type=code&scope=aws.cognito.signin.user.admin+email+openid+phone+profile&redirect_uri={CALLBACK_URLS[0]}'
LOGOUT_URL = f'https://{COGNITO_DOMAIN}/logout?client_id={COGNITO_CLIENT_ID}&logout_uri={LOGOUT_URLS[0]}'


# decorator to check the login before accessing any page
def login_required(f):
    """Check the login details"""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get('access_token') is None:
            # redirect to login page in case not login yet
            return redirect(LOGIN_URL)
        return f(*args, **kwargs)
    return decorated_function


class Alert:
    '''Class to create alerts that show to the user'''
    class Category(Enum):
        '''Enumeration for alert types'''
        ERROR = 'danger'
        WARNING = 'warning'
        SUCCESS = 'success'
        INFO = 'info'

    def __init__(self, message, category: Category):
        self.message = message
        self.category = category


# Inject the href information to all flask templates
@app.context_processor
def inject_dict_for_all_templates():
    '''inject_dict_for_all_templates'''
    return dict(href_dict=href_dict)


@app.route("/login", methods=["GET", "POST"])
def login():
    '''Check login details and store cache for success login'''
    cognito_code = request.args.get('code')
    if cognito_code:
        access_token, username = get_session_details(cognito_code)
        session["access_token"] = access_token
        session["username"] = username
        return redirect("/")
    return redirect(LOGIN_URL)


@app.route("/logout")
def logout():
    """Log user out"""
    # Forget any user_id
    session.clear()
    return redirect(LOGOUT_URL)


@app.route("/", methods=["GET"])
@login_required
def index():
    '''Homepage, shows list of modules'''
    access_token = session["access_token"]
    username = session["username"]
    alerts = []

    alert_args = request.args.get('alert')
    if alert_args:
        alert_dict = loads(alert_args)
        alert_msg = str(alert_dict['message'])
        alert_cat = Alert.Category[alert_dict['category']]
        alerts.append(Alert(alert_msg, alert_cat))

    questions = generate_questions(access_token)

    return render_template("index.html",
                           questions=questions,
                           alerts=alerts,
                           username=username,
                           current_page='Home')


@app.route("/about", methods=["GET"])
@login_required
def about():
    '''Show information about the application'''
    username = session["username"]
    return render_template("about.html",
                           username=username,
                           current_page='About')
