# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["WorkerRetrieveParams"]


class WorkerRetrieveParams(TypedDict, total=False):
    task_id: Annotated[str, PropertyInfo(alias="taskId")]
    """
    Return the worker state and messages for a specific task instead of the most
    recent one.
    """
