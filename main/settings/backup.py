from .dev import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'tabular_notes',
        'USER': 'tabular_notes',
        'PASSWORD': 'passw0rd',
        'HOST': 'localhost',
        'PORT': '5433'
    }
}
