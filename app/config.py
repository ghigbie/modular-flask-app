import os

class config(object):
    SECRET_KEY = os.enivron.get('SECRET_KEY') or 'you-will-never-guess-this' 

# This uses an environment variable or then uses the string