import enum
from typing import Optional
from sqlmodel import SQLModel, Field, Column, Enum


class TaskTypeEnum(str, enum.Enum):
    execute_code = 'execute_code'
    


class TaskStatusEnum(str, enum.Enum):
    pending = 'pending'
    completed = 'completed'
    failed = 'failed'


class Task(SQLModel, table=True):
    """Task model. 
    
    This model store details for a single task. It'll be helpful to track pending tasks, 
    failed tasks, and completed tasks. 

    In the future, we can add more functionalities to re-run etc. 
    This will also track elapsed time for task completion.
    """
    id: Optional[int] = Field(default=None, primary_key=True)
    task_type: TaskTypeEnum = Field(sa_column=Column(Enum(TaskTypeEnum)))    
    task_status: TaskStatusEnum = Field(sa_column=Column(Enum(TaskStatusEnum)))
    code: str
    cpu: int
    gpu: int
    ram: str
    storage: str
    output: str