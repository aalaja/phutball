# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '8u!4&6@8ojhp-pfoc%o%nw6f4&=!g^+e7n=8rxc^r8-4nuxmr!'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['api'] # Should match service name in nginx config

CORS_ORIGIN_ALLOW_ALL = False

CORS_ORIGIN_WHITELIST = (
       'http://localhost:80',
)
