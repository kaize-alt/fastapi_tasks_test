from typing import Annotated

from fastapi import APIRouter, Depends

from repository import TaskRepository
from schema import STaskAdd, STask

router = APIRouter(
    prefix="/tasks",
    tags=["Tasks"]
)

@router.post("/add_task")
async def add_task(
        task: Annotated[STaskAdd, Depends()]
):
    task_id = await TaskRepository.add_task(task)
    return {"message": "Task added successfully", "task_id": task_id}


@router.get("/get_tasks")
async def get_tasks() -> STask:
    tasks = await TaskRepository.get_all_tasks()
    return tasks
