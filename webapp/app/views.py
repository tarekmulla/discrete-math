# pylint: disable=import-error
'''views file'''
from functools import wraps
from tempfile import mkdtemp
from enum import Enum
from json import loads
from app import app
from app.question import questionCls
from app.api import generate_questions
from flask import render_template, request, session, redirect


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


# decorator to check the login before accessing any page
def login_required(f):
    """Check the login details"""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get('username') is None:
            # redirect to login page in case not login yet
            return redirect("/login")
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
    if request.method == "POST":
        # Forget any cached username
        session.clear()
        username = request.form.get("username")
        password = request.form.get("password")
        # TODO: change to a more secure login-checking mechanism
        if username == 'rmit@rmit.au' and password == 'rmit':
            session["username"] = username
            return redirect("/")
        else:
            # redirect again to login page, if failed in login
            return redirect("/login")
    if 'username' in session:  # already login
        return redirect("/")

    return render_template("login.html", current_page='Home')


@app.route("/logout")
def logout():
    """Log user out"""
    # Forget any user_id
    session.clear()
    return redirect("/login")


@app.route("/", methods=["GET"])
@login_required
def index():
    '''Homepage, shows list of modules'''
    username = session["username"]
    alerts = []

    alert_args = request.args.get('alert')
    if alert_args:
        alert_dict = loads(alert_args)
        alert_msg = str(alert_dict['message'])
        alert_cat = Alert.Category[alert_dict['category']]
        alerts.append(Alert(alert_msg, alert_cat))

    questions = generate_questions()

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
