from .base import *
import os

SECRET_KEY = 'ib37rab14!3nqv*v@kcfbnsk=5_fa-=!s0^+dq9l+v13^6ki#z'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']
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

BITLY_LOGIN = "o_apad6ae0n"
BITLY_API_KEY = "R_e932b2dcae134fa79c1ecc000a3c8453"

SITE_ID = 4