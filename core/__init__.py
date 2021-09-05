# Imports
import logging
import sys
from flask import Flask, url_for, get_flashed_messages, abort, render_template
from jinja2 import Template, Environment, FileSystemLoader, exceptions

# Variables

jinja2_env = Environment(loader = FileSystemLoader('./views'))

#app = Flask(__name__, static_folder='app', static_url_path="/app")
app = Flask("monitoring-dashboard", static_url_path='/', static_folder='wwwroot', template_folder='html')

# Functions

def get_model(cookie_json=None):
    caller = sys._getframe(1)                       # '_getframe(1)' gets previous stack; 
                                                    # '_getframe()' gets current stack
    caller_name = caller.f_code.co_name             # returns 'view_home'
    module_name = caller.f_globals['__name__']      # returns 'modules.default_routes'
    package_name = caller.f_globals['__package__']  # returns 'modules'

    context = cookie_json if cookie_json is not None else {}
    context['view_name'] = caller_name
    context['view_module'] = module_name
    context['view_package'] = package_name
    context['view_id'] = f"{module_name}.{caller_name}"
    context['url_for'] = url_for                            # function for Flask
    context['get_flashed_messages'] = get_flashed_messages  # function for Flask

    # context['app_settings'] = app_settings                  # make application settings available

    # Authentication cookie check
    # app_token = request.cookies.get(app_settings['application']['app_token'])
    
    # # view_model["google_client_id"] = app_settings["application"]["google_client_id"]
    # context['google_client_id'] = app_settings["application"]["google_client_id"]
    
    # logging.info(app_token)
    
    # (is_token_valid, tokens) = is_valid_app_token(app_token)
    
    # context['valid_app_token'] = is_token_valid
    
    # if tokens is not None:
    #     context["user_id"] = tokens[0]
    # else:
    #     context["user_id"] = "UNKNOWN"

    # if is_valid_app_token(app_token):
    #     context['valid_app_token'] = True
    # else:
    #     context['valid_app_token'] = False
    # context['auth_cookie'] = request.cookies.get(appconfig["application"]["auth_cookie_name"])
    # context['current_datetime'] = datetime.now()
    # context = {
    #     'auth_cookie'       : request.cookies.get(appconfig["application"]["auth_cookie_name"]),
    #     'current_datetime'  : datetime.now()
    # }
    return context

def view(model=None, view_path=None):
    if view_path is None:
        caller = sys._getframe(1)                       # '_getframe(1)' gets previous stack; 
                                                        # '_getframe()' gets current stack
        caller_name = caller.f_code.co_name             # returns 'view_home'
        module_name = caller.f_globals['__name__']      # returns 'modules.default_routes'
        package_name = caller.f_globals['__package__']  # returns 'modules'

        view_path = module_name.split('.')
        view_path.remove(package_name)
        view_path.append("{0}.html".format(caller_name))
        view_path = '/'.join(view_path)                 # returns 'default_routes/view_home.html

    if model is None:
        model = get_model()
    
    logging.info(f"Getting view {view_path}, {model}")
    try:
        return jinja2_env.get_template(view_path).render(model)
    except exceptions.TemplateNotFound as ex:
        logging.error(f"TemplateNotFound [{view_path}]")
        abort(404)
    except Exception as ex:
        logging.error(ex)
        abort(500)
    

@app.errorhandler(404)
def http_404(e):
    # note that we set the 404 status explicitly
    return render_template('http_status/404.html'), 404

@app.errorhandler(500)
def http_500(e):
    # note that we set the 404 status explicitly
    return render_template('http_status/404.html'), 404