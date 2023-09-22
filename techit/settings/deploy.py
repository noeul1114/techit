from .base import *


def read_secret(secret_name):
    file = open('/run/secrets/' + secret_name)
    secret = file.read()
    secret = secret.lstrip().rstrip()
    file.close()
    return secret


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-1nr6-589u1-%893*qp)uewlkat$h0m$1q+)#&+tf)_0-bis7&m'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = [
    '*'
]


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": read_secret("MARIADB_DATABASE"),
        "USER": read_secret("MARIADB_USER"),
        "PASSWORD": read_secret("MARIADB_PASSWORD"),
        "HOST": "mariadb",
        "PORT": "3306",
    }
}
