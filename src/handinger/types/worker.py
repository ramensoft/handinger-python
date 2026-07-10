# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import builtins
from typing import Dict, List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["Worker", "File", "Output", "OutputContent", "Source", "Usage"]


class File(BaseModel):
    filename: Optional[str] = None

    media_type: str = FieldInfo(alias="mediaType")

    url: str

    size: Optional[int] = None


class OutputContent(BaseModel):
    text: str

    type: Literal["output_text"]


class Output(BaseModel):
    id: str

    content: List[OutputContent]

    role: Literal["assistant"]

    status: Literal["completed"]

    type: Literal["message"]


class Source(BaseModel):
    id: str

    title: Optional[str] = None

    type: Literal["url"]

    url: str


class Usage(BaseModel):
    duration_ms: Optional[int] = FieldInfo(alias="durationMs", default=None)


class Worker(BaseModel):
    id: str

    created_at: Optional[int] = None

    error: None = None

    files: List[File]

    incomplete_details: None = None

    messages: List[object]

    metadata: Dict[str, object]

    object: Literal["worker"]

    output: List[Output]

    output_text: str

    running: bool

    sources: List[Source]

    status: Literal["running", "completed", "pending"]

    structured_output: Optional[Dict[str, builtins.object]] = None

    url: str
    """Web URL of the worker in the Handinger dashboard."""

    usage: Optional[Usage] = None
