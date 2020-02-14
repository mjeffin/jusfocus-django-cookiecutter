from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'qhdrjromr-=fdsdfdsfhg!&ow%48&prt7c#seiiea4g^k154r'

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ['*'] 

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

TEST_RUNNER = "django.test.runner.DiscoverRunner"


try:
    from .local import *
except ImportError:
    pass

INTERNAL_IPS = [
    # ...
    '127.0.0.1',
    # ...
]
