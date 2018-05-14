import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'xxxxx'
    USER_ID = os.environ.get('USER_ID') or 'xxxxx'