from typing_extensions import Annotated
from fastapi import Depends
from .task import TaskDao


TaskDaoDep = Annotated[TaskDao, Depends(TaskDao)]