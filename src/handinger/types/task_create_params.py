# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["TaskCreateParams"]


class TaskCreateParams(TypedDict, total=False):
    input: Required[str]

    budget: Literal["low", "standard", "high", "unlimited"]
    """Compute budget the worker is allowed to spend on the task.

    Defaults to `standard`.
    """

    task_id: Annotated[str, PropertyInfo(alias="taskId")]
    """Optional client-provided task id.

    Reuse this id to add turns to an existing task.
    """

    worker_id: Annotated[str, PropertyInfo(alias="workerId")]
    """Worker id the task belongs to.

    If omitted, a new worker is created on-the-fly using the input as instructions.
    """
