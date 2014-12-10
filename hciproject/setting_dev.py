import os

DEBUG = True  

DATABASES = {
'default': {
    'ENGINE': 'django.db.backends.sqlite3',
    'NAME': os.path.join(os.path.dirname(os.path.dirname(__file__)), 'db.sqlite3'),
}
}