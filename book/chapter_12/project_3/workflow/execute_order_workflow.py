from conductor.client.automator.task_handler import TaskHandler
from conductor.client.configuration.configuration import Configuration
from conductor.client.workflow.conductor_workflow import ConductorWorkflow
from conductor.client.workflow.executor.workflow_executor import WorkflowExecutor
from order_workflow import order_workflow


def main():
    # The app is connected to http://localhost:8080/api by default
    api_config = Configuration()

    workflow_executor = WorkflowExecutor(configuration=api_config)

    # Starting the worker polling mechanism
    task_handler = TaskHandler(configuration=api_config)
    task_handler.start_processes()

    workflow_run = workflow_executor.execute(name='Order Workflow',
                                             version=2,
                                             workflow_input={
                                                 'customer_id': 1,
                                                 'products': {1: 1, 2: 3},
                                                 'payment_amount': 2000,
                                                 'delivery_address': '456 Broadway, New York, NY 10013, United States'},
                                             )

    task_handler.stop_processes()


if __name__ == '__main__':
    main()