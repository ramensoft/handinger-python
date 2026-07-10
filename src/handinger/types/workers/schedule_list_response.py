# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .worker_schedule import WorkerSchedule

__all__ = ["ScheduleListResponse"]


class ScheduleListResponse(BaseModel):
    schedules: List[WorkerSchedule]

    timezone: str

    worker_id: str = FieldInfo(alias="workerId")
