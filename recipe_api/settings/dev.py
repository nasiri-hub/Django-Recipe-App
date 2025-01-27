from .common import *
import os

ALLOWED_HOSTS = ['0.0.0.0']

DEBUG = True

SECRET_KEY = os.environ.get('SECRET_KEY')

DATABASES = {
    'default': {
        'ENGINE': os.environ['SQL_ENGINE'],
        'NAME': os.environ['SQL_DATABASE'],
        'USER': os.environ['SQL_USER'],
        'PASSWORD': os.environ['SQL_PASSWORD'],
        'HOST': os.environ['SQL_HOST'],
        'PORT': os.environ['SQL_PORT'],
    }
}

DEBUG_TOOLBAR_CONFIG = {
    'SHOW_TOOLBAR_CALLBACK': lambda request: True
}
