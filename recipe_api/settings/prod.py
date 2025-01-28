from .common import *
import os

DEBUG = False

SECRET_KEY = os.environ['SECRET_KEY']

ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', '*')

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