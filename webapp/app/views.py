# pylint: disable=import-error
'''views file'''
from functools import wraps
from app import app
from app.api import generate_questions
from app.cognito import get_session_details
from flask import render_template, request, session, redirect, current_app
import app.config as CONFIG


# Create dictionary for navbar and make it global for all templates
href_dict = {
    'Home': '/',
    'About': '/about'
    }


# Inject the href information to all flask templates
@app.context_processor
def inject_dict_for_all_templates():
    '''inject_dict_for_all_templates'''
    return dict(href_dict=href_dict)


# decorator to check the login before accessing any page
def login_required(f):
    """Check the login details"""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not session.get('token'):
            # redirect to login page in case not login yet
            current_app.logger.info("Token has expired")
            return redirect(CONFIG.LOGIN_URL)
        return f(*args, **kwargs)
    return decorated_function


@app.route("/login", methods=["GET", "POST"])
def login():
    '''Check login details and store cache for success login'''
    cognito_code = request.args.get('code')
    if cognito_code:
        session_details = get_session_details(cognito_code)
        if 'token' in session_details and 'username' in session_details:
            session["token"] = session_details['token']
            session["username"] = session_details['username']
            return redirect("/")
    return render_template("500.html")


@app.route("/logout")
def logout():
    """Log user out"""
    # Forget any user_id
    session.clear()
    return redirect(CONFIG.LOGOUT_URL)


@app.route("/", methods=["GET"])
@login_required
def index():
    '''Homepage, shows list of modules'''
    token = session["token"]
    username = session["username"]
    questions = generate_questions(token)

    return render_template("index.html",
                           questions=questions,
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
