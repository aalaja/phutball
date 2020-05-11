from .secrets import SECRET_KEY

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['api'] # Should match service name in nginx config

CORS_ORIGIN_ALLOW_ALL = False

CORS_ORIGIN_WHITELIST = (
       'http://www.philophers.football',
)

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': 'db',
        'PORT': '5432',
    }
}
