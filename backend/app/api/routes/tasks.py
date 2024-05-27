from typing import Optional
from fastapi import APIRouter, BackgroundTasks, HTTPException

from app.services import TaskServiceDep
from app.models import TaskCreate, Task

router = APIRouter()


def run_task(task_id: int, task_service: TaskServiceDep):
    """Background task to create a docker container and run task. 
    
    This can be upgraded to use celery tasks for later.
    """
    task_service.run_task(task_id)



@router.post("/", response_model=Task)
def create_task(task_service: TaskServiceDep, task: TaskCreate, bgc_tasks: BackgroundTasks) -> Task:
    """Create new task."""
    task: Task = task_service.create_task(task)
    bgc_tasks.add_task(run_task, task.id, task_service)
    return task


@router.get("/{task_id}", response_model=Task)
def get_task(task_id: int, task_service: TaskServiceDep) -> Task:
    task: Optional[Task] = task_service.get_task(task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task
