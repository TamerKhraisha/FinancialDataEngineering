"""
This file contains a Simple Worker that can be used in any workflow.
For detailed information https://github.com/conductor-sdk/conductor-python/blob/main/README.md#step-2-write-worker
"""
from conductor.client.worker.worker_task import worker_task
from stock_and_inventory_service.service import update_inventory as ui

@worker_task(task_definition_name='update_inventory')
def update_inventory(order_id: str) -> dict:
    result = ui(order_id=order_id)
    return result
