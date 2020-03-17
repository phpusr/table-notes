DEBUG = False

# It needs if DEBUG = false
ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'tabular_notes',
        'USER': 'tabular_notes',
        'PASSWORD': 'passw0rd',
        'HOST': 'db',
        'PORT': '5432'
    }
}

# TODO Change it
SECRET_KEY = 'l!h5vuplda*f!&pa9dr742i*ak^w-8+ifgrk_3=-g==!c)3ne('
