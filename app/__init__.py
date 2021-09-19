from flask import Flask
def create_app(config_name):
    '''
    Function that takes configuration setting key as an argument

    Args:
        config_name: name of the configuration to be used
    '''
    # Initializing application
    app = Flask(__name__)
    return app