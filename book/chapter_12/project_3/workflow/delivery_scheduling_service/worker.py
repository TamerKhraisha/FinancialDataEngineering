"""
This file contains a Simple Worker that can be used in any workflow.
For detailed information https://github.com/conductor-sdk/conductor-python/blob/main/README.md#step-2-write-worker
"""
from conductor.client.worker.worker_task import worker_task
from delivery_scheduling_service.service import schedule_delivery as sd
import uuid

@worker_task(task_definition_name='schedule_delivery')
def schedule_delivery(order_id: int) -> dict:
    result = sd(order_id=order_id)
    return result
