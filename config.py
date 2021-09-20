import os

class Config:
    '''
    General configuration parent class
    '''
    
class ProdConfig(Config):
    '''
    Production configuration child class

    Args:
        Config: The parent configuration class with general configuration settings
    '''
class TestConfig(Config):
    '''
    Testing configuration child class

    Args:
        Config: The parent configuration class with general configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    Development configuration child class

    Args:
        Config: The parent configuration class with general configuration settings
    '''
    DEBUG = True
    
    