"""
This file contains a Simple Worker that can be used in any workflow.
For detailed information https://github.com/conductor-sdk/conductor-python/blob/main/README.md#step-2-write-worker
"""
from conductor.client.worker.worker_task import worker_task
from payment_processing_service.service import process_payment as pp

@worker_task(task_definition_name='process_payment')
def process_payment(order_id: int) -> dict:
    result = pp(order_id=order_id)
    return result
