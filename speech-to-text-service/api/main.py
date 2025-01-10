from fastapi import FastAPI
from pydantic import BaseModel
from celery import Celery, uuid
from celery.result import AsyncResult


app = FastAPI()

celery_app = Celery(
    broker="redis://localhost:6379/0",
    backend="redis://localhost:6379/0",
)


class TranscriptionRequest(BaseModel):
    url: str
    language: str


@app.post("/transcribe/")
async def post_transcribe(request: TranscriptionRequest):
    task_id = uuid()

    async_task = celery_app.send_task(
        "tasks.transcribe",
        args=[request.url, request.language],
        task_id=task_id,
    )

    return {
        "task_id": async_task.id,
        "status": async_task.status,
    }


@app.get("/transcribe/{task_id}/status")
async def get_transcribe_status(task_id: str):
    async_result = AsyncResult(task_id, app=celery_app)
    return {
        "status": async_result.status,
        "result": async_result.result,
        "task_id": async_result.id,
    }
