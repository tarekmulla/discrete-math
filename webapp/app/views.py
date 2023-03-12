"""views file"""
from datetime import timedelta

from flask import redirect, render_template, request, session

import app.config as CONFIG
from app import app
from app.cognito import get_session_details
from app.html_helper import login_required


@app.before_request
def before_request():
    """make session permanent"""
    session.permanent = True
    app.permanent_session_lifetime = timedelta(minutes=300)


# Ensure responses aren't cached
@app.after_request
def after_request(response):
    """after_request"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/login", methods=["GET", "POST"])
def login():
    """Check login details and store cache for success login"""
    cognito_code = request.args.get("code")
    if cognito_code:
        session_details = get_session_details(cognito_code)
        if "token" in session_details and "username" in session_details:
            session["token"] = session_details["token"]
            session["username"] = session_details["username"]
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
    """Homepage, shows list of modules"""
    username = session["username"]
    return render_template(
        "index.html", username=username, selected_page="Home"
    )


@app.route("/about", methods=["GET"])
@login_required
def about():
    """Show information about the application"""
    username = session["username"]
    return render_template("about.html", username=username, selected_page="About")

@app.route("/architecture", methods=["GET"])
@login_required
def architecture():
    """Show information about the architecture"""
    username = session["username"]
    return render_template("architecture.html", username=username, selected_page="Architecture")
