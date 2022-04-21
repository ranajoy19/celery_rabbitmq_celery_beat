from __future__ import absolute_import, unicode_literals
from celery import shared_task
from celery.utils.log import get_task_logger

from django.core.management import call_command
import sys

logger = get_task_logger(__name__)

@shared_task
def bkup():
    sys.stdout = open('db.json', 'w')
    call_command('dumpdata', 'test3')
    logger.info('data successfully backup to db.json')