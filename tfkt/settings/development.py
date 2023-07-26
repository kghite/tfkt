from .base import *

from dotenv import load_dotenv
import os

dotenv_path = os.path.join(ENVIRONMENTS['Development'])

load_dotenv(dotenv_path)

SECRET_KEY = os.environ.get('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.contrib.gis.db.backends.postgis",
        "NAME": os.environ.get('DB_NAME'),
        "USER": os.environ.get('DB_USER'),
        "PASSWORD": os.environ.get('DB_PASS'),
        "HOST": os.environ.get('DB_HOST'),
    },
}
