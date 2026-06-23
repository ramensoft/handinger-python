# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional

from pydantic import Field as FieldInfo

from .task import Task
from .._models import BaseModel

__all__ = ["TaskWithTurns", "Turn", "TurnFile"]


class TurnFile(BaseModel):
    filename: Optional[str] = None

    media_type: str = FieldInfo(alias="mediaType")

    url: str

    size: Optional[int] = None


class Turn(BaseModel):
    id: str

    completed_at: Optional[str] = FieldInfo(alias="completedAt", default=None)

    credits: int

    duration_ms: int = FieldInfo(alias="durationMs")

    files: List[TurnFile]
    """Files published by this turn."""

    input: str

    input_tokens: int = FieldInfo(alias="inputTokens")

    output_text: str = FieldInfo(alias="outputText")

    output_tokens: int = FieldInfo(alias="outputTokens")

    role: str

    seq: int

    started_at: str = FieldInfo(alias="startedAt")

    status: str

    structured_output: Optional[Dict[str, object]] = FieldInfo(alias="structuredOutput", default=None)
    """Structured JSON payload when the worker is configured with an output schema.

    `null` otherwise.
    """

    task_id: str = FieldInfo(alias="taskId")


class TaskWithTurns(BaseModel):
    task: Task

    turns: List[Turn]
