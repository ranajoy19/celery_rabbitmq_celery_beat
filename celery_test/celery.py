from __future__ import absolute_import, unicode_literals
import os
from django.apps import apps


from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'celery_test.settings')

app = Celery('celery_test')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()
