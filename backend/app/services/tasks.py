import structlog
from app.worker import create_task

logger = structlog.get_logger(module="tasks")


class TaskService:
    def create(self):
        create_task.delay()
