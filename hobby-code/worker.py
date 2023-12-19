import os
import time
from typing import List

from celery import Celery
from celery.result import AsyncResult

from data_types import Army


app = Celery(__name__)
app.conf.broker_url = os.environ.get("REDIS_URL", "redis://localhost:6379")
app.conf.result_backend = app.conf.broker_url


@app.task(name="create_task")
def create_task(armies: List[Army]) -> str:
    """Find out which army is the best"""
    # deserialise
    armies = [Army.model_validate(x) for x in armies]
    # handle edge cases
    if len(armies) == 0:
        return "It's peaceful here. No armies in sight..."
    if len(armies) == 1:
        return f"No one dared to challenge {armies[0].leader}'s army. He's the best. {armies[0].leader.chant()}"
    if all(len(army.members)==0 for army in armies):
        return "No men willing to fight here?"

    victor = max(armies)
    # Estimate the time of battle
    sleep_time = sum(x.life for x in victor.members)
    # Ride! Ride to ruin and the world's ending!
    time.sleep(sleep_time)
    return f"{victor.leader}'s army has won. {victor.leader.chant()}"


def task_status(task_id: str) -> AsyncResult:
    """Return task results by task id"""
    status = app.AsyncResult(task_id)
    return status
