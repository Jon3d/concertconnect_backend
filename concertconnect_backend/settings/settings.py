"""
Django settings for concertconnect_backend project.
'
For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os, pylast

BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
assert 'CC_DJANGO_SECRET_KEY' in os.environ, 'Set CC_DJANGO_SECRET_KEY in your env vars!'
SECRET_KEY = os.environ['CC_DJANGO_SECRET_KEY']

assert 'LAST_FM_API_KEY' in os.environ, 'Set LAST_FM_API_KEY in your env vars!'
LAST_FM_API_KEY = os.environ['LAST_FM_API_KEY']

assert 'LAST_FM_SECRET_KEY' in os.environ, 'Set LAST_FM_SECRET_KEY in your env vars!'
LAST_FM_SECRET_KEY = os.environ['LAST_FM_SECRET_KEY']

assert 'LAST_FM_USERNAME' in os.environ, 'Set LAST_FM_USERNAME in your env vars!'
LAST_FM_USERNAME = os.environ['LAST_FM_USERNAME']

assert 'LAST_FM_PASSWORD' in os.environ, 'Set LAST_FM_PASSWORD in your env vars!'
LAST_FM_PASSWORD_HASH = pylast.md5(os.environ['LAST_FM_PASSWORD'])

LAST_FM_NETWORK = pylast.LastFMNetwork(api_key = LAST_FM_API_KEY, 
                               api_secret = LAST_FM_SECRET_KEY, 
                               username = LAST_FM_USERNAME, 
                               password_hash = LAST_FM_PASSWORD_HASH)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'artist',
    'taggit',
    'event',
    'rest_framework',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'concertconnect_backend.urls'

WSGI_APPLICATION = 'concertconnect_backend.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

#Rest framework
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': ('rest_framework.permissions.IsAdminUser',),
    'PAGINATE_BY': 10
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

DATABASES = {}

import dj_database_url
DATABASES['default'] = dj_database_url.config()

import sys
if 'test' in sys.argv or 'test_coverage' in sys.argv: #Covers regular testing and django-coverage unittests
    DATABASES['default']['engine'] = 'sqlite3'
    
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format' : "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
            'datefmt' : "%d/%b/%Y %H:%M:%S"
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': 'logs/cc_backend.log',
            'formatter': 'verbose'
        },
    },
    'loggers': {
        'django': {
            'handlers':['file'],
            'propagate': True,
            'level':'DEBUG',
        },
        'MYAPP': {
            'handlers': ['file'],
            'level': 'DEBUG',
        },
    }
}
