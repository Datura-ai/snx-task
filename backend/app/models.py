import enum
from typing import Optional
from sqlmodel import SQLModel, Field, Column, Enum
from pydantic import conint, field_validator

from app.validators import validate_size_str


class TaskTypeEnum(str, enum.Enum):
    execute_code = 'execute_code'
    


class TaskStatusEnum(str, enum.Enum):
    pending = 'pending'
    completed = 'completed'
    failed = 'failed'


class Resource(SQLModel):
    cpus: conint(ge=1)  # At least 1 CPU
    memory: str = Field(regex=r'^\d+[mMgG]$') # Memory in format like '512m', '1g'
    gpus: conint(ge=0) = 0  # At least 0 GPUs, default to 0
    storage: str = Field(regex=r'^\d+[mMgG]$')  # Storage in format like '1g', '10g'
    
    @field_validator('memory', 'storage')
    @classmethod
    def check_memory_storage(cls, v: str) -> str:
        if validate_size_str(v) is False:
            raise ValueError('Invalid Size.')
        return v


class TaskBase(SQLModel):
    """Base model for Task."""
    task_type: TaskTypeEnum = Field(sa_column=Column(Enum(TaskTypeEnum)))
    code: str


class TaskCreate(TaskBase):
    """Schema to create a task."""
    resources: Resource


class Task(TaskBase, table=True):
    """Task model. 
    
    This model store details for a single task. It'll be helpful to track pending tasks, 
    failed tasks, and completed tasks. 

    In the future, we can add more functionalities to re-run etc. 
    This will also track elapsed time for task completion.
    """
    id: Optional[int] = Field(default=None, primary_key=True)
    task_status: TaskStatusEnum = Field(sa_column=Column(Enum(TaskStatusEnum)))
    cpu: int
    gpu: int
    ram: str
    storage: str
    output: str


