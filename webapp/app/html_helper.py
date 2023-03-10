'''html helpers file'''
from functools import wraps
from app import app
from flask import session, redirect, current_app, jsonify  # type: ignore
import app.config as CONFIG
from markupsafe import Markup


PAGES = {
    'Home': '/',
    'About': '/about',
    'Modules': {
        'GCD': '/gcd',
        'LCM': '/lcm',
        'Prime Numbers': '/prime',
        'Truth Tables': '/truth'
    }
}


@app.context_processor
def utility_processor():
    '''Inject methods to call in html pages'''
    def generate_menu(menu: dict, selected_item, level=0):
        '''generate the html menu'''
        html = ''
        li_class = 'nav-item' if level == 0 else ''
        li_dropdown = ' dropdown' if level == 0 else ''
        a_class = 'nav-link' if level == 0 else 'dropdown-item'
        a_dropdown = ' dropdown-toggle' if level == 0 else ''
        a_data_bs = ' role="button" data-bs-toggle="dropdown" aria-expanded="false"' if level == 0 else ''
        ul_class = 'dropdown-menu' if level == 0 else 'dropdown-submenu dropdown-menu'

        for k, v in menu.items():
            if isinstance(v, dict):
                menu_id = f' id="menu-{k}"' if level == 0 else ''
                menu_aria = f' aria-labelledby="menu-{k}"' if level == 0 else ''
                html += f'<li class="{li_class}{li_dropdown}"> \
                    <a class="{a_class}{a_dropdown}" href="#"{a_data_bs}{menu_id}>{k}</a> \
                    <ul class="{ul_class}"{menu_aria}>'
                html += generate_menu(v, selected_item, level+1)
                html += '</ul></li>'
            else:
                active = ' active' if k == selected_item else ''
                aria = ' aria-current="page"' if k == selected_item else ''
                html += f'<li class="{li_class}"><a class="{a_class}{active}"{aria} href="{v}">{k}</a></li>'
        return html.replace(' class=""', '')

    def generate_nav(selected_item):
        return Markup(generate_menu(PAGES, selected_item))

    return dict(generate_nav=generate_nav)


# decorator to check the login before accessing any page
def login_required(func):
    """Check the login details"""
    @wraps(func)
    def decorated_function(*args, **kwargs):
        if not session.get('token'):
            # redirect to login page in case not login yet
            current_app.logger.info("Token has expired")
            return redirect(CONFIG.LOGIN_URL)
        return func(*args, **kwargs)
    return decorated_function


@app.route("/health")
def health():
    """health check for the app"""
    return jsonify(healthy=True)