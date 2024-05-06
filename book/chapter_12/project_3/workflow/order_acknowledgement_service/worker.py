"""
This file contains a Simple Worker that can be used in any workflow.
For detailed information https://github.com/conductor-sdk/conductor-python/blob/main/README.md#step-2-write-worker
"""
from conductor.client.worker.worker_task import worker_task
from order_acknowledgement_service.service import acknowledge_order as ao

@worker_task(task_definition_name='acknowledge_order')
def acknowledge_order(customer_id: int, products: dict, payment_amount: float, delivery_address: str) -> dict:
    result = ao(customer_id=customer_id, products=products, payment_amount=payment_amount, delivery_address=delivery_address)
    return result
