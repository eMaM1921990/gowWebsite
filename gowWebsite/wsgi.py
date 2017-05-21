"""
WSGI config for gowWebsite project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/howto/deployment/wsgi/
"""
#
# import os
#
# from django.core.wsgi import get_wsgi_application
#
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "gowWebsite.settings")
#
# application = get_wsgi_application()


import os
import sys

sys.path.append('/opt/bitnami/apps/django/django_projects/gowWebsite')
os.environ['PYTHON_EGG_CACHE']="/opt/bitnami/apps/django/django_projects/gowWebsite/egg_cache"
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "gowWebsite.settings.base")

from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()
