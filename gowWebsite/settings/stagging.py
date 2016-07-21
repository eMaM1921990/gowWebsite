__author__ = 'emam'

from base import *


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases
#Database Info
DB_USER='eMaM1921990'
DB_PASSWORD='0122308791'
DB_NAME='eMaM1921990$default'
DB_HOST='eMaM1921990.mysql.pythonanywhere-services.com'
DB_PORT=3306

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



MEDIA_BASE='/home/eMaM1921990/'
MEDIA_ROOT = os.path.join(MEDIA_BASE, 'media')
MEDIA_URL = '/media/'
ADV_URL='adv/'
