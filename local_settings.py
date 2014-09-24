from settings import PROJECT_ROOT, SITE_ROOT
import os

DEBUG = True
TEMPLATE_DEBUG = True

DATABASES = {
    "default": {
        "ENGINE": 'django.contrib.gis.db.backends.postgis',
        "NAME": "kimathi_hostels",
        "USER": "postgres",
        "PASSWORD": "postgres",
        "HOST": "localhost",
        "PORT": "5432",
    }
}

#Procfile setting |choose one|
#web: gunicorn kimathi_hostels.wsgi --log-file -
#web: python manage.py runserver 0.0.0.0:$PORT --noreload