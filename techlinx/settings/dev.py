from .base import *
import os

SECRET_KEY = 'ib37rab14!3nqv*v@kcfbnsk=5_fa-=!s0^+dq9l+v13^6ki#z'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME':   'blog',                      
        'USER': 'bloguser',
        'PASSWORD': 'blog2018',
        'HOST': 'localhost',
        'PORT': 5432,
    }
}


STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR,'static')]
#STATIC_ROOT = os.path.join(BASE_DIR,'static')


MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR,'media')

BITLY_LOGIN = "salgadolg5@hotmail.com"
BITLY_API_KEY = "b8ebd1afc77d7b830af0baabe531ba7d7ccfeaa5"

SITE_ID =2