"""
Django settings for gowWebsite project.

Generated by 'django-admin startproject' using Django 1.9.1.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

import os

# Django settings for celery_test project.
from datetime import timedelta
import djcelery
djcelery.setup_loader()

## Celery config ##
BROKER_URL = 'amqp://test:test@localhost:5672//'
# BROKER_URL = 'django://'


CELERY_RESULT_BACKEND = 'djcelery.backends.database:DatabaseBackend'
CELERYBEAT_SCHEDULER = 'djcelery.schedulers.DatabaseScheduler'
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = 'UTC'



## END config ##



# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE_DIR = BASE_DIR+ '/templates'


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '%dpbmcl)m&*(fw)8trvubt3qeq(wr*j#=1sg%o3l6-sxdg=ge8'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'grappelli',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'gate_of_world_app',
    'djcelery',
    'social_widgets',
    'endless_pagination',
    # 'lockdown',
   # 'kombu.transport.django',# for development onlypython manage.py migrate
]

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
        # 'lockdown.middleware.LockdownMiddleware',

]

ROOT_URLCONF = 'gowWebsite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_DIR],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ]
        },
    },
]

WSGI_APPLICATION = 'gowWebsite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases
#Database Info
DB_USER='gate_user_'
# DB_USER='root'
DB_PASSWORD='Azsxdcfv@'
# DB_PASSWORD='admin'
DB_NAME='gate_'
# DB_NAME='gate_of_world'

DB_HOST='localhost'
DB_PORT=3306

# DB_USER='eMaM1921990'
# DB_PASSWORD='ahmednano2011'
# DB_NAME='eMaM1921990$default'
# DB_HOST='eMaM1921990.mysql.pythonanywhere-services.com'
# DB_PORT=3306


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME':DB_NAME,
        'USER': DB_USER,
        'PASSWORD': DB_PASSWORD,
        'HOST': DB_HOST,   # Or an IP Address that your DB is hosted on
        'PORT':DB_PORT,
    }
}

#
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'd54asntq94mcto',
#         'USER': 'jxwhbwszuynxoj',
#         'PASSWORD': 'tTpud2fkekGAKB42h7K9eBJwEZ',
#         'HOST': 'ec2-54-243-203-93.compute-1.amazonaws.com',
#         'PORT': '5432',
#     }
# }



# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

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

#Logging
LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'standard': {
            'format': '%(asctime)s [%(levelname)s] %(name)s: %(message)s'
        },
    },
    'handlers': {
        'default': {
            'level':'DEBUG',
            'class':'logging.handlers.RotatingFileHandler',
            'filename': 'gate_log.log',
            'maxBytes': 1024*1024*5, # 5 MB
            'backupCount': 5,
            'formatter':'standard',
        },
        'request_handler': {
            'level':'DEBUG',
            'class':'logging.handlers.RotatingFileHandler',
            'filename': 'gate_log_request.log',
            'maxBytes': 1024*1024*5, # 5 MB
            'backupCount': 5,
            'formatter':'standard',
        },
    },
    'loggers': {
        '': {
            'handlers': ['default'],
            'level': 'DEBUG',
            'propagate': True
        },
        'django.request': {
            'handlers': ['request_handler'],
            'level': 'DEBUG',
            'propagate': False
        },
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)

MEDIA_BASE='/home/emam/'
MEDIA_ROOT = os.path.join(MEDIA_BASE, 'media')
MEDIA_URL = '/media/'
ADV_URL='adv/'


#GRAPPELLI
GRAPPELLI_ADMIN_TITLE='Gate of world - Admin panel'


#Lock
# LOCKDOWN_PASSWORDS = ('password', )
# LOCKDOWN_URL_EXCEPTIONS = (r'^/admin',)
# LOCKDOWN_FORM = 'lockdown.forms.LockdownForm'

#Endless pagination
ENDLESS_PAGINATION_PREVIOUS_LABEL='Previous'
ENDLESS_PAGINATION_NEXT_LABEL='Next'