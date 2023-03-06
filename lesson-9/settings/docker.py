from .base import * # noqa

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.getenv('POSTGRES_DB', 'lesson-9'),
        'USER': os.getenv('POSTGRES_USER', 'postgres'),
        'PASSWORD': os.getenv('POSTGRES_PASSWORD', '123'),
        'HOST': os.getenv('POSTGRES_HOST', 'db'),
        'PORT': os.getenv('POSTGRES_PORT', '5432'),
        'ATOMIC_REQUESTS': True
    }
}


STATIC_ROOT = '/static'


EMAIL_BACKEND = os.getenv('EMAIL_BACKEND', 'django.core.mail.backends.console.EmailBackend')


EMAIL_HOST = os.getenv('EMAIL_HOST', 'localhost')
EMAIL_PORT = int(os.getenv('EMAIL_PORT', '555'))
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER', 'test')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD', 'test')
EMAIL_USE_TLS = os.getenv('EMAIL_USE_TLS', 'False').lower() in ('1', 'true')


ANYMAIL = {
    "MAILGUN_API_KEY": os.getenv('EMAIL_HOST_PASSWORD', ''),
    "MAILGUN_API_URL": "https://api.eu.mailgun.net/v3",
}

SITE_URL = os.getenv('SITE_URL', 'http://localhost:8000')


CELERY_BROKER_URL = 'redis://redis:6379/0'

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.redis.RedisCache',
        'LOCATION': 'redis://redis:6379',
    }
}
