from .settings_dev import *

DEBUG = False

# It needs if DEBUG = false
ALLOWED_HOSTS = ['127.0.0.1', 'localhost']

STATIC_ROOT = os.path.join(BASE_DIR, 'static')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'data', 'db_prod.sqlite3'),
    }
}
