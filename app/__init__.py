from flask import Flask
from config import config_options
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
def create_app(config_name):
    '''
    Function that takes configuration setting key as an argument

    Args:
        config_name: name of the configuration to be used
    '''
    # Initializing application
    app = Flask(__name__)
    return app