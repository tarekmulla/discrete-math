'''modules file'''
from app import app
from flask import render_template, session  # type: ignore


@app.route("/gcd")
def gcd():
    """GCD"""
    username = session["username"]
    return render_template('modules/gcd.html',
                           username=username,
                           selected_page='GCD')


@app.route("/lcm")
def lcm():
    """LCM"""
    username = session["username"]
    return render_template('modules/lcm.html',
                           username=username,
                           selected_page='LCM')


@app.route("/prime")
def prime():
    """Prime numbers"""
    username = session["username"]
    return render_template('modules/prime.html',
                           username=username,
                           selected_page='Prime numbers')


@app.route("/truth")
def truth():
    """Truth tables"""
    username = session["username"]
    return render_template('modules/truth.html',
                           username=username,
                           selected_page='Truth tables')
