# -*- coding: utf-8 -*-
import os, sys

from django.core.wsgi import get_wsgi_application

sys.path.append('/home/muslu/django/pisayisicom/pisayisicom/')
sys.path.append('/home/muslu/django/pisayisicom/')

os.environ['DJANGO_SETTINGS_MODULE'] = 'pisayisicom.settings'
application = get_wsgi_application()
