"""modules file"""
from flask import render_template, request, session

from app import app
from app.api import calculate_gcd, generate_truth_table, get_factors
from app.classes.factors import FactorsCls
from app.classes.pair import PairCls
from app.classes.proposition import PropositionCls
from app.html_helper import login_required


@app.route("/gcd", methods=["GET", "POST"])
@login_required
def gcd():
    """Find GCD and LCM for 2 numbers"""
    username = session["username"]
    token = session["token"]
    number1 = request.form.get("number1")
    number2 = request.form.get("number2")
    pair = None
    if number1 and number2:
        pair = PairCls(number1, number2)
        calculate_gcd(pair, token)
    return render_template(
        "modules/gcd.html",
        username=username,
        selected_page="GCD",
        pair=(pair if pair else None),
    )


@app.route("/factors", methods=["GET", "POST"])
@login_required
def factors():
    """factors and prime numbers"""
    username = session["username"]
    token = session["token"]
    number = request.form.get("number")
    num_factors = None
    if number:
        num_factors = FactorsCls(number)
        get_factors(num_factors, token)
    return render_template(
        "modules/factors.html",
        username=username,
        selected_page="Factors",
        num_factors=(num_factors if num_factors else None),
    )


@app.route("/truth", methods=["GET", "POST"])
def truth():
    """Truth table"""
    username = session["username"]
    token = session["token"]
    prop_exp = request.form.get("proposition")
    proposition = None
    if prop_exp:
        proposition = PropositionCls(prop_exp)
        generate_truth_table(proposition, token)
    return render_template(
        "modules/truth.html",
        username=username,
        selected_page="Truth table",
        proposition=(proposition if proposition else None),
    )
