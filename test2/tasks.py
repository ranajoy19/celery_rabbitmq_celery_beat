from celery import shared_task

from .email import send_review_mail
from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)


@shared_task(name ="send_review_email_task")
def send_review_email_task(name,email,review):
    logger.info('send email successfully')
    return send_review_mail(name,email,review)
