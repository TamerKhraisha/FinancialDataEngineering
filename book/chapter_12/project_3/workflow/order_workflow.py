from conductor.client.workflow.conductor_workflow import ConductorWorkflow
from conductor.client.workflow.executor.workflow_executor import WorkflowExecutor
from order_acknowledgement_service.worker import acknowledge_order
from notification_service.worker import notify_customer
from payment_processing_service.worker import process_payment
from stock_and_inventory_service.worker import update_inventory
from delivery_scheduling_service.worker import schedule_delivery

def order_workflow(workflow_executor: WorkflowExecutor) -> ConductorWorkflow:
    workflow = ConductorWorkflow(
        name='Order Workflow',
        executor=workflow_executor,
        version=2,
        description='Executes the services required to process a customer order.'
    )

    # Acknowledge Order task
    acknowledge_order_task = acknowledge_order(
        task_ref_name='acknowledge_order_ref',
        customer_id=workflow.input('customer_id'),
        products=workflow.input('products'),
        payment_amount=workflow.input('payment_amount'),
        delivery_address=workflow.input('delivery_address')
    )

    # Notify the customer of the acknowledgment task
    notify_acknowledgement_task = notify_customer(
        task_ref_name='notify_acknowledgement_ref',
        order_id=acknowledge_order_task.output('order_id'),
        notification_text=acknowledge_order_task.output('notification')
    )

    # Process payment task
    process_payment_task = process_payment(
        task_ref_name='process_payment_ref',
        order_id=acknowledge_order_task.output('order_id')
    )

    # Notify customer of payment task
    notify_payment_task = notify_customer(
        task_ref_name='notify_payment_ref',
        order_id=acknowledge_order_task.output('order_id'),
        notification_text=process_payment_task.output('notification')
    )

    # Update inventory
    update_inventory_task = update_inventory(
        task_ref_name='update_inventory_ref',
        order_id=acknowledge_order_task.output('order_id')
    )

    # Notify customer of inventory booking
    notify_inventory_task = notify_customer(
        task_ref_name='notify_inventory_ref',
        order_id=acknowledge_order_task.output('order_id'),
        notification_text=update_inventory_task.output('notification')
    )

    # Schedule delivery
    schedule_delivery_task = schedule_delivery(
        task_ref_name='schedule_delivery_ref',
        order_id=acknowledge_order_task.output('order_id'),
    )

    # Notify customer of delivery schedule
    notify_delivery_task = notify_customer(
        task_ref_name='notify_delivery_ref',
        order_id=acknowledge_order_task.output('order_id'),
        notification_text=schedule_delivery_task.output('notification')
    )

    # define the flow structure
    workflow >> acknowledge_order_task >> \
        notify_acknowledgement_task >> \
        process_payment_task >> \
        notify_payment_task >> \
        update_inventory_task >> \
        notify_inventory_task >> \
        schedule_delivery_task >> \
        notify_delivery_task

    return workflow