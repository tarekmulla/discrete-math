"""html helpers file"""
from functools import wraps

from flask import current_app, jsonify, redirect, session
from markupsafe import Markup

import app.config as CONFIG
from app import app

PAGES = {
    "Home": "/",
    "About": "/about",
    "Modules": {
        "GCD & LCM": "/gcd",
        "Factors": "/factors",
        "Truth Table": "/truth-table",
    },
}


@app.context_processor
def utility_processor():
    """Inject methods to call in html pages"""

    def generate_menu(menu: dict, selected_item, level=0):
        """generate the html menu"""
        html = ""
        li_class = "nav-item" if level == 0 else ""
        li_dropdown = " dropdown" if level == 0 else ""
        a_class = "nav-link" if level == 0 else "dropdown-item"
        a_dropdown = " dropdown-toggle" if level == 0 else ""
        a_data_bs = (
            ' role="button" data-bs-toggle="dropdown" aria-expanded="false"'
            if level == 0
            else ""
        )
        ul_class = "dropdown-menu" if level == 0 else "dropdown-submenu dropdown-menu"

        for key, val in menu.items():
            if isinstance(val, dict):
                menu_id = f' id="menu-{key}"' if level == 0 else ""
                menu_aria = f' aria-labelledby="menu-{key}"' if level == 0 else ""
                html += f'<li class="{li_class}{li_dropdown}"> \
                    <a class="{a_class}{a_dropdown}" href="#"{a_data_bs}{menu_id}>{key}</a> \
                    <ul class="{ul_class}"{menu_aria}>'
                html += generate_menu(val, selected_item, level + 1)
                html += "</ul></li>"
            else:
                active = " active" if key == selected_item else ""
                aria = ' aria-current="page"' if key == selected_item else ""
                html += f'<li class="{li_class}"><a class="{a_class}{active}"{aria} href="{val}">{key}</a></li>'
        return html.replace(' class=""', "")

    def generate_nav(selected_item):
        return Markup(generate_menu(PAGES, selected_item))

    return dict(generate_nav=generate_nav)


# decorator to check the login before accessing any page
def login_required(func):
    """Check the login details"""

    @wraps(func)
    def decorated_function(*args, **kwargs):
        if not session.get("token"):
            # redirect to login page in case not login yet
            current_app.logger.info("Token has expired")
            return redirect(CONFIG.LOGIN_URL)
        return func(*args, **kwargs)

    return decorated_function


@app.route("/health")
def health():
    """health check for the app"""
    return jsonify(healthy=True)
