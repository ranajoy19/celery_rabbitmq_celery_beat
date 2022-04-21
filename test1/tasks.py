from __future__ import absolute_import, unicode_literals
from celery.utils.log import get_task_logger
from celery import shared_task

logger = get_task_logger(__name__)

@shared_task
def add(x,y):
    logger.info('sucessfully adding is done')
    return x+y


