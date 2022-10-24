import os
import time

import structlog
from celery import Celery, shared_task

logger = structlog.get_logger(module="worker")

celery = Celery(__name__)
celery.conf.broker_url = os.environ.get("CELERY_BROKER_URL", "redis://localhost:6379")
celery.conf.result_backend = os.environ.get("CELERY_RESULT_BACKEND", "redis://localhost:6379")


@shared_task(name="create_task")
def create_task():
    logger.debug("create")
    return True
