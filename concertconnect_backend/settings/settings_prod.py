import dj_database_url
import os
import pylast
from concertconnect_backend.settings.settings_base import *

DATABASES = dict(default=dj_database_url.config())

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
