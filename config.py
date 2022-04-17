import os

def get_secret(sname):
    try:
        with open('/run/secrets/{}'.format(sname), 'r') as sfile:
            return sfile.read()
    except IOError:
        return None

class Config(object):
    DEBUG = False
    TESTING = False
    
    SECRET_KEY = get_secret('FP_SK') if get_secret('FP_SK') is not None else os.environ.get('FP_SK')
    if SECRET_KEY is None:
        raise RuntimeError("Secret Key not setup, exiting...")

    SQLALCHEMY_DATABASE_URI = 'sqlite:///boterham_stash.db'
    # SQLALCHEMY_DATABASE_URI = "access:///?DataSource=OefenvragenCWO.mdb"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Fixes issue with HTTPS redirect failures
    PREFERRED_URL_SCHEME = 'https'
    
class ProdConfig(Config):
    pass

class DevConfig(Config):
    DEBUG = True
    SESSION_COOKIE_SECURE = False

class TestConfig(Config):
    TESTING = True
    SESSION_COOKIE_SECURE = False
