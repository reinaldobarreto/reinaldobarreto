from __future__ import annotations

from datetime import datetime
from typing import Dict, List, Optional
from uuid import uuid4

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field


class TaskCreate(BaseModel):
    title: str = Field(min_length=1, max_length=120)
    description: Optional[str] = Field(default=None, max_length=400)


class Task(TaskCreate):
    id: str
    done: bool
    created_at: datetime


class TaskUpdate(BaseModel):
    title: Optional[str] = Field(default=None, min_length=1, max_length=120)
    description: Optional[str] = Field(default=None, max_length=400)
    done: Optional[bool] = None


app = FastAPI(
    title="FastAPI CRUD - Tasks",
    version="1.0.0",
    description="Simple CRUD API to showcase FastAPI + Pydantic + OpenAPI.",
)

_db: Dict[str, Task] = {}


@app.get("/health")
def health() -> Dict[str, str]:
    return {"status": "ok"}


@app.post("/tasks", response_model=Task, status_code=201)
def create_task(payload: TaskCreate) -> Task:
    task = Task(
        id=str(uuid4()),
        title=payload.title,
        description=payload.description,
        done=False,
        created_at=datetime.utcnow(),
    )
    _db[task.id] = task
    return task


@app.get("/tasks", response_model=List[Task])
def list_tasks(done: Optional[bool] = None) -> List[Task]:
    tasks = list(_db.values())
    if done is None:
        return tasks
    return [t for t in tasks if t.done is done]


@app.get("/tasks/{task_id}", response_model=Task)
def get_task(task_id: str) -> Task:
    task = _db.get(task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task


@app.patch("/tasks/{task_id}", response_model=Task)
def update_task(task_id: str, payload: TaskUpdate) -> Task:
    task = _db.get(task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    data = task.model_dump()
    patch = payload.model_dump(exclude_unset=True)
    merged = {**data, **patch}
    updated = Task(**merged)
    _db[task_id] = updated
    return updated


@app.delete("/tasks/{task_id}", status_code=204)
def delete_task(task_id: str) -> None:
    if task_id not in _db:
        raise HTTPException(status_code=404, detail="Task not found")
    del _db[task_id]

