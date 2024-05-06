"""Notification Worker"""

from conductor.client.worker.worker_task import worker_task
from notification_service.service import notify_customer as nc

@worker_task(task_definition_name='notify_customer')
def notify_customer(order_id: int, notification_text: str) -> dict:
    service_outcome = nc(order_id=order_id, notification_text=notification_text)
    return service_outcome
