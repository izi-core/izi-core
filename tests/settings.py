import os

import izi
from izi.defaults import *  # noqa

# Path helper
location = lambda x: os.path.join(
    os.path.dirname(os.path.realpath(__file__)), x)

ALLOWED_HOSTS = ['test', '.ecommerce.izi.asia']

DATABASES = {
    'default': {
        'ENGINE': os.environ.get('DATABASE_ENGINE',
                                 'django.db.backends.postgresql'),
        'NAME': os.environ.get('DATABASE_NAME', 'izi'),
        'USER': os.environ.get('DATABASE_USER', None),
        'PASSWORD': os.environ.get('DATABASE_USER', None),
    }
}

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.admin',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.flatpages',
    'django.contrib.staticfiles',
    'widget_tweaks',

    # contains models we need for testing
    'tests._site.model_tests_app',
    'tests._site.myauth',

    # Use a custom partner app to test overriding models.  I can't
    # find a way of doing this on a per-test basis, so I'm using a
    # global change.
] + izi.get_core_apps([
    'tests._site.apps.partner',
    'tests._site.apps.customer',
    'tests._site.apps.catalogue'
])

AUTH_USER_MODEL = 'myauth.User'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            location('_site/templates'),
            izi.IZI_MAIN_TEMPLATE_DIR,
        ],
        'OPTIONS': {
            'loaders': [
                ('django.template.loaders.cached.Loader', [
                    'django.template.loaders.filesystem.Loader',
                    'django.template.loaders.app_directories.Loader',
                ]),
            ],
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.request',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.contrib.messages.context_processors.messages',

                'izi.apps.search.context_processors.search_form',
                'izi.apps.customer.notifications.context_processors.notifications',
                'izi.apps.promotions.context_processors.promotions',
                'izi.apps.checkout.context_processors.checkout',
                'izi.core.context_processors.metadata',
            ]
        }
    }
]


MIDDLEWARE = [
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',

    'izi.apps.basket.middleware.BasketMiddleware',
]


AUTHENTICATION_BACKENDS = (
    'izi.apps.customer.auth_backends.EmailBackend',
    'django.contrib.auth.backends.ModelBackend',
)

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        'OPTIONS': {
            'min_length': 6,
        }
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

HAYSTACK_CONNECTIONS = {'default': {'ENGINE': 'haystack.backends.simple_backend.SimpleEngine'}}
PASSWORD_HASHERS = ['django.contrib.auth.hashers.MD5PasswordHasher']
ROOT_URLCONF = 'tests._site.urls'
LOGIN_REDIRECT_URL = '/accounts/'
STATIC_URL = '/static/'
DEBUG = False
SITE_ID = 1
USE_TZ = 1
APPEND_SLASH = True
DDF_DEFAULT_DATA_FIXTURE = 'tests.dynamic_fixtures.IZIDynamicDataFixtureClass'
SESSION_SERIALIZER = 'django.contrib.sessions.serializers.JSONSerializer'
LANGUAGE_CODE = 'en-gb'

IZI_INITIAL_ORDER_STATUS = 'A'
IZI_ORDER_STATUS_PIPELINE = {'A': ('B',), 'B': ()}
IZI_INITIAL_LINE_STATUS = 'a'
IZI_LINE_STATUS_PIPELINE = {'a': ('b', ), 'b': ()}

SECRET_KEY = 'notverysecret'
TEST_RUNNER = 'django.test.runner.DiscoverRunner'
