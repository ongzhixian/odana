import logging

from os import getenv

# from flask import Flask
# from jinja2 import Template, Environment, FileSystemLoader

# jinja2_env = Environment(loader = FileSystemLoader('./views'))

# #app = Flask(__name__, static_folder='app', static_url_path="/app")
# app = Flask("monitoring-dashboard", static_url_path='/', static_folder='wwwroot',)

from core import app, jinja2_env
from controllers.root import *


################################################################################
# Set default logging levels
################################################################################

if getenv('GAE_ENV', '').startswith('standard'):
    # Setup for logging in AppEngine environments
    logging.getLogger().setLevel(logging.DEBUG)
else:
    # Setup for logging in non-AppEngine environments
    root_logger = logging.getLogger()
    root_logger.setLevel(logging.DEBUG)
    for handler in root_logger.handlers:
        root_logger.removeHandler(handler)

    console_logger = logging.StreamHandler()
    # console_logger.setFormatter(logging.Formatter('%(asctime)-15s.%(msec)03d %(levelname)-8s %(funcName)-20s %(message)s', datefmt="%H:%M:%S"))
    root_logger.addHandler(console_logger)

    # Uncomment to log to file (Comment out for GCP)
    # logging_format = logging.Formatter('%(asctime)-15s %(levelname)-8s %(name)-5s %(message)s')
    logging_format = logging.Formatter('%(asctime)-15s %(levelname)-8s %(funcName)-20s %(message)s')
    file_logger = logging.FileHandler('logs/monitoring-dashboard.log')
    file_logger.setFormatter(logging_format)
    root_logger.addHandler(file_logger)



################################################################################
# Main function
################################################################################

if __name__ == '__main__':
    # Note: This is used when running locally only. 
    # When deploying to Google App Engine, a webserver process such as Gunicorn will serve the app. 
    # This can be configured by adding an `entrypoint` to app.yaml (to run under uwsgi).

    # Flask's development server will automatically serve static files in the "static" directory. See:
    # http://flask.pocoo.org/docs/1.0/quickstart/#static-files.
    # Once deployed, App Engine itself will serve those files as configured in app.yaml.
    # from modules import app_version
    # app_version.incr_revision()
    from datetime import datetime
    # logging.info("[PROGRAM START]")
    logging.critical("%8s test message %s" % ("CRITICAL", str(datetime.utcnow())))
    logging.error("%8s test message %s" % ("ERROR", str(datetime.utcnow())))
    logging.warning("%8s test message %s" % ("WARNING", str(datetime.utcnow())))
    logging.info("%8s test message %s" % ("INFO", str(datetime.utcnow())))
    logging.debug("%8s test message %s" % ("DEBUG", str(datetime.utcnow())))
    # Flask startup may print:
    # * Restarting with stat
    # 'stat' is a reloader used by Flask to reload, when there are changes made to files
    # See https://stackoverflow.com/questions/28241989/flask-app-restarting-with-stat
    # To avoid view the message, set 'use_reloader=False' option in run.
    # app.run(host='127.0.0.1', port=8080, debug=True, use_reloader=False) 
    app.run(host='127.0.0.1', port=8080, debug=True)