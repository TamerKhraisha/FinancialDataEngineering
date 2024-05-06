from conductor.client.automator.task_handler import TaskHandler
from conductor.client.configuration.configuration import Configuration
from conductor.client.workflow.conductor_workflow import ConductorWorkflow
from conductor.client.workflow.executor.workflow_executor import WorkflowExecutor
from order_workflow import order_workflow


def register_workflow(workflow_executor: WorkflowExecutor) -> ConductorWorkflow:
    workflow = order_workflow(workflow_executor=workflow_executor)
    workflow.register(True)
    return workflow


def main():
    # The app is connected to http://localhost:8080/api by default
    try:
        api_config = Configuration()
    
        workflow_executor = WorkflowExecutor(configuration=api_config)
    
        # Registering the workflow (Required only when the app is executed the first time)
        workflow = register_workflow(workflow_executor)
    
        print(f'Successfully registered workflow {workflow.name} - version {workflow.version}')
    except Exception as e:
        print(e)

if __name__ == '__main__':
    main()