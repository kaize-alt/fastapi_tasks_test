from sqlalchemy import select

from database import new_session, TasksOrm
from schema import STaskAdd, STask


class TaskRepository():
    @classmethod
    async def add_task(cls, data: STaskAdd):
        async with new_session() as session:
            task_dict = data.model_dump()

            task = TasksOrm(**task_dict)
            session.add(task)
            await session.commit()
            return task.id


    @classmethod
    async def get_all_tasks(cls) -> list[STask]:
        async with new_session() as session:
            query = select(TasksOrm)
            result = await session.execute(query)
            task_models = result.scalars().all()
            task_schemas = [STask.model_validate(task_model) for task_model in task_models ]
            return task_models
