from fastapi import Depends
from typing_extensions import Annotated
from app.dao import TaskDaoDep


class DockerService:
    def __init__(self):
        pass

    def create_container(self):
        print('DockerService->create_container')


class TaskService:
    def __init__(
            self, 
            docker_service: Annotated[DockerService, Depends(DockerService)],
            task_dao: TaskDaoDep
        ):
        self.docker_service = docker_service
        self.task_dao = task_dao

    def create_task(self):
        print('TaskService->create_task')
        self.docker_service.create_container()
        self.task_dao.create()
