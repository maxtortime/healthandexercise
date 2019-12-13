from .dev import *

ALLOWED_HOSTS = ['*']
DEBUG = False

DATABASES = {
    'default': {
        # If you are using Cloud SQL for MySQL rather than PostgreSQL, set
        # 'ENGINE': 'django.db.backends.mysql' instead of the following.
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'db_healthandexercise',
        'USER': os.getenv('DATABASE_USER'),
        'PASSWORD': os.getenv('DATABASE_PASSWORD'),
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}

STATIC_ROOT = 'static/'
STATIC_URL = 'https://storage.googleapis.com/wide-fx-261704/static/'
