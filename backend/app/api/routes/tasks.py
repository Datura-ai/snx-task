from typing import Any
from fastapi import APIRouter

from app.services import TaskServiceDep
from app.models import TaskCreate

router = APIRouter()


@router.post("/")
def create_task(task_service: TaskServiceDep, task: TaskCreate) -> Any:
    """Create new task."""
    task_service.create_task(task)
