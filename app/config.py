
class Config(object):
    DEBUG = True
    TESTING = False

class DevelopmentConfig(Config):
    SECRET_KEY = "this-is-a-super-secret-key"



config = {
    'development': DevelopmentConfig,
    'testing': DevelopmentConfig,
    'production': DevelopmentConfig
}



API_KEY = ''
API_KEY_SECRET = ''
BEARER_TOKEN = ''
ACCESS_TOKEN = ''
ACCESS_TOKEN_SECRET = ''
