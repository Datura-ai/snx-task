from typing import Any
from fastapi import APIRouter

from app.services import TaskServiceDep

router = APIRouter()


@router.post("/")
def create_task(task_service: TaskServiceDep) -> Any:
    """Create new task."""
    task_service.create_task()
