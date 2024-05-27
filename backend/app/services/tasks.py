import time
from fastapi import Depends
from typing_extensions import Annotated

from app.dao import TaskDaoDep
from app.models import TaskCreate, Task
from app.services.docker import DockerService


class TaskService:
    def __init__(
            self, 
            docker_service: Annotated[DockerService, Depends(DockerService)],
            task_dao: TaskDaoDep
        ):
        self.docker_service = docker_service
        self.task_dao = task_dao

    def create_task(self, task_in: TaskCreate) -> Task:
        task: Task = self.task_dao.create(task_in)
        return task
        
    def get_task(self, task_id: int) -> Task:
        return self.task_dao.get_by_id(task_id)
    
    def run_task(self, task_id: int) -> Task:
        """Run task inside docker. 
        
        Create docker container for given task and run code.
        Store elapsed time, output, and status.
        """
        task: Task = self.task_dao.get_by_id(task_id)
        start_time = time.time()
        response = self.docker_service.create_task_container(task)
        response['elapsed_time'] = time.time() - start_time
        return self.task_dao.update(task, response)
