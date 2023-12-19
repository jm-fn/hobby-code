from typing import List

from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from fastapi.responses import HTMLResponse

from data_types import Army
from worker import create_task, task_status


app = FastAPI()


@app.get("/")
async def read_root():
    result = """
    Welcome to the battlefield
    ==========================

    Please head directly to github.com/jm-fn/hobby-project/README.md to find out more...
    """
    return HTMLResponse(result)


@app.post("/")
async def post_army(armies: List[Army]):
    task = create_task.delay(jsonable_encoder(armies))
    return {"task_id": task.id}


@app.get("/tasks/{task_id}")
def get_task_result(task_id):
    task_result = task_status(task_id)
    return {
        "task_id": task_id,
        "task_status": task_result.status,
        "task_result": task_result.result,
    }
