"""
Django settings for mysite project.

Generated by 'django-admin startproject' using Django 2.0.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os
import dj_database_url
import django_heroku

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("SECRET_KEY", "INSECURE")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get('DEBUG', 'False').lower() == 'true'
HEROKU_RELEASE_VERSION = os.environ.get("HEROKU_RELEASE_VERSION", "0")
HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME", "")
HEROKU_SLUG_COMMIT = os.environ.get("HEROKU_SLUG_COMMIT", "")

# Cache version - Use HEROKU_RELEASE_VERSION (eg v123)
VERSION = int(HEROKU_RELEASE_VERSION.replace('v', ''))

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'blog.apps.BlogConfig',
    'scout.apps.ScoutConfig',
    'grappelli',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'markdownify',
    'nested_admin',
    'django_celery_beat',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'mysite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'blog.ctx.heroku_info',
                'blog.ctx.nav',
                'blog.ctx.mains',
                'django.template.context_processors.request',
            ],
        },
    },
]

WSGI_APPLICATION = 'mysite.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/New_York'

USE_I18N = True

USE_L10N = True

USE_TZ = True

ACCOUNT_LOGOUT_REDIRECT_URL = "/blog"

# Change 'default' database configuration with $DATABASE_URL.
DATABASES['default'].update(dj_database_url.config(conn_max_age=500, ssl_require=True))

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
ALLOWED_HOSTS = ['*']

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_ROOT = os.path.join(PROJECT_ROOT, 'staticfiles')
STATIC_URL = '/static/'

# Extra places for collectstatic to find static files.
STATICFILES_DIRS = [
    os.path.join(PROJECT_ROOT, 'static'),
]

# Simplified static file serving.
# https://warehouse.python.org/project/whitenoise/
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Markdownify https://django-markdownify.readthedocs.io/en/latest/settings.html
MARKDOWNIFY_BLEACH = False

MARKDOWNIFY_MARKDOWN_EXTENSIONS = ['markdown.extensions.fenced_code',
                                   'markdown.extensions.extra', ]

# Https instead of Http
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_HSTS_SECONDS = 3600
SECURE_HSTS_PRELOAD = True
CSRF_USE_SESSIONS = True

# S3 file storage
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
AWS_AUTO_CREATE_BUCKET = True
AWS_BUCKET_ACL = "private"
AWS_DEFAULT_ACL = "private"
AWS_STORAGE_BUCKET_NAME = os.environ.get('BUCKETEER_BUCKET_NAME', 'insecure')
AWS_SECRET_ACCESS_KEY = os.environ.get('BUCKETEER_AWS_SECRET_ACCESS_KEY', 'insecure')
AWS_ACCESS_KEY_ID = os.environ.get('BUCKETEER_AWS_ACCESS_KEY_ID', 'insecure')
AWS_S3_USE_SSL = True

BASE_REDIS_URL_DEFAULT = 'redis://localhost'
BASE_REDIS_URL = os.environ.get('REDIS_URL', BASE_REDIS_URL_DEFAULT)
REDIS_DJANGO_CACHE_URL = BASE_REDIS_URL + "/1"
REDIS_CELERY_TASKS_URL = BASE_REDIS_URL + "/2"
REDIS_CELERY_TOMBS_URL = BASE_REDIS_URL + "/3"

if BASE_REDIS_URL != BASE_REDIS_URL_DEFAULT:
    CACHES = {
        'default': {
            'BACKEND': 'redis_cache.RedisCache',
            'LOCATION': REDIS_DJANGO_CACHE_URL,
            'CONNECTION_POOL_CLASS': 'redis.BlockingConnectionPool',
            'CONNECTION_POOL_CLASS_KWARGS': {
                'max_connections': 50,
                'timeout': 20,
            },
        },
    }

CELERY_BROKER_URL = REDIS_CELERY_TASKS_URL
CELERY_ACCEPT_CONTENT = ['json', ]
CELERY_RESULT_BACKEND = REDIS_CELERY_TOMBS_URL
CELERY_ACKS_LATE = True
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_ENABLE_UTC = True

TBA_AUTH_KEY = os.environ.get('TBA_AUTH_KEY', None)

# Activate Django-Heroku.
django_heroku.settings(locals())
