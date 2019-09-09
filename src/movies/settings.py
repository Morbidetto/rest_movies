import os

try:
    OMBD_KEY = os.environ['OMDB_KEY']
except KeyError:
    OMBD_KEY = ''