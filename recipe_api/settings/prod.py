from .common import *
from django.conf import settings
import os

DEBUG = False

SECRET_KEY = os.environ['SECRET_KEY']

ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS')

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

SESSION_COOKIE_SECURE = True
SECURE_SSL_REDIRECT = True
SECURE_HSTS_PRELOAD = True
CSRF_COOKIE_SECURE = True
SECURE_HSTS_SECONDS = 31536000 # Unit is seconds;
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
SECURE_REFERRER_POLICY = "strict-origin-when-cross-origin"

# Content Security Policy
CSP_IMG_SRC = ("'self'")
CSP_STYLE_SRC = ("'self'")
CSP_SCRIPT_SRC = ("'self'")

if not settings.DEBUG:
    MIDDLEWARE += ["csp.middleware.CSPMiddleware"]