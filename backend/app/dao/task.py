from .base import BaseDao
from app.models import TaskCreate, Task


class TaskDao(BaseDao):
    """DAO class for Task Model."""

    def save(self, task: Task) -> Task:
        self.session.add(task)
        self.session.commit()
        self.session.refresh(task)
        return task
    
    def create(self, task_in: TaskCreate) -> Task:
        """Create a Task."""
        task: Task = task_in.get_task()
        db_task = Task.model_validate(task)
        return self.save(db_task)

    def get_by_id(self, task_id: int) -> Task:
        return self.session.query(Task).where(Task.id==task_id).first()

    def update(self, task: Task, payload: dict) -> Task:
        task.sqlmodel_update(payload)
        return self.save(task)
