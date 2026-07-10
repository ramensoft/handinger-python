# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from pydantic import Field as FieldInfo

from .turn import Turn
from .._models import BaseModel

__all__ = ["TaskTurnList"]


class TaskTurnList(BaseModel):
    items: List[Turn]

    task_id: str = FieldInfo(alias="taskId")
