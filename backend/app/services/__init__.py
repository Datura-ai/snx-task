from typing_extensions import Annotated
from fastapi import Depends
from app.services.tasks import TaskService


TaskServiceDep = Annotated[TaskService, Depends(TaskService)]