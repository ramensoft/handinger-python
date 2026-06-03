# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Mapping, cast
from typing_extensions import Literal

import httpx

from ..types import task_create_params
from .._files import deepcopy_with_paths
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import extract_files, path_template, maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.worker import Worker
from ..types.task_with_turns import TaskWithTurns
from ..types.delete_task_response import DeleteTaskResponse

__all__ = ["TasksResource", "AsyncTasksResource"]


class TasksResource(SyncAPIResource):
    """Run and inspect tasks against a worker."""

    @cached_property
    def with_raw_response(self) -> TasksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/ramensoft/handinger-python#accessing-raw-response-data-eg-headers
        """
        return TasksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TasksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/ramensoft/handinger-python#with_streaming_response
        """
        return TasksResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        input: str,
        budget: Literal["low", "standard", "high", "unlimited"] | Omit = omit,
        task_id: str | Omit = omit,
        worker_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Worker:
        """Run a new task against an existing worker and wait for the result.

        Send a
        `taskId` of a prior task to add a follow-up turn instead of starting a fresh
        task. Send `multipart/form-data` to attach files; the bytes are bootstrapped
        into the worker's workspace before the task starts. The task runs to completion
        on the server even if the connection drops; subscribe to task webhooks for
        long-running tasks.

        Args:
          budget: Compute budget the worker is allowed to spend on the task. Defaults to
              `standard`.

          task_id: Optional client-provided task id. Reuse this id to add turns to an existing
              task.

          worker_id: Worker id the task belongs to. If omitted, a new worker is created on-the-fly
              using the input as instructions.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        body = deepcopy_with_paths(
            {
                "input": input,
                "budget": budget,
                "task_id": task_id,
                "worker_id": worker_id,
            },
            [["files"], ["files", "<array>"]],
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["files"], ["files", "<array>"]])
        if files:
            # It should be noted that the actual Content-Type header that will be
            # sent to the server will contain a `boundary` parameter, e.g.
            # multipart/form-data; boundary=---abc--
            extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return self._post(
            "/api/tasks",
            body=maybe_transform(body, task_create_params.TaskCreateParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Worker,
        )

    def retrieve(
        self,
        task_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TaskWithTurns:
        """
        Retrieve a single task and its individual turns.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not task_id:
            raise ValueError(f"Expected a non-empty value for `task_id` but received {task_id!r}")
        return self._get(
            path_template("/api/tasks/{task_id}", task_id=task_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskWithTurns,
        )

    def delete(
        self,
        task_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DeleteTaskResponse:
        """Archive a task so it stops appearing in `GET /tasks` results.

        Turns and files
        are retained for audit purposes. Only the worker creator can archive a task.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not task_id:
            raise ValueError(f"Expected a non-empty value for `task_id` but received {task_id!r}")
        return self._delete(
            path_template("/api/tasks/{task_id}", task_id=task_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DeleteTaskResponse,
        )


class AsyncTasksResource(AsyncAPIResource):
    """Run and inspect tasks against a worker."""

    @cached_property
    def with_raw_response(self) -> AsyncTasksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/ramensoft/handinger-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTasksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTasksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/ramensoft/handinger-python#with_streaming_response
        """
        return AsyncTasksResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        input: str,
        budget: Literal["low", "standard", "high", "unlimited"] | Omit = omit,
        task_id: str | Omit = omit,
        worker_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Worker:
        """Run a new task against an existing worker and wait for the result.

        Send a
        `taskId` of a prior task to add a follow-up turn instead of starting a fresh
        task. Send `multipart/form-data` to attach files; the bytes are bootstrapped
        into the worker's workspace before the task starts. The task runs to completion
        on the server even if the connection drops; subscribe to task webhooks for
        long-running tasks.

        Args:
          budget: Compute budget the worker is allowed to spend on the task. Defaults to
              `standard`.

          task_id: Optional client-provided task id. Reuse this id to add turns to an existing
              task.

          worker_id: Worker id the task belongs to. If omitted, a new worker is created on-the-fly
              using the input as instructions.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        body = deepcopy_with_paths(
            {
                "input": input,
                "budget": budget,
                "task_id": task_id,
                "worker_id": worker_id,
            },
            [["files"], ["files", "<array>"]],
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["files"], ["files", "<array>"]])
        if files:
            # It should be noted that the actual Content-Type header that will be
            # sent to the server will contain a `boundary` parameter, e.g.
            # multipart/form-data; boundary=---abc--
            extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return await self._post(
            "/api/tasks",
            body=await async_maybe_transform(body, task_create_params.TaskCreateParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Worker,
        )

    async def retrieve(
        self,
        task_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TaskWithTurns:
        """
        Retrieve a single task and its individual turns.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not task_id:
            raise ValueError(f"Expected a non-empty value for `task_id` but received {task_id!r}")
        return await self._get(
            path_template("/api/tasks/{task_id}", task_id=task_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskWithTurns,
        )

    async def delete(
        self,
        task_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DeleteTaskResponse:
        """Archive a task so it stops appearing in `GET /tasks` results.

        Turns and files
        are retained for audit purposes. Only the worker creator can archive a task.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not task_id:
            raise ValueError(f"Expected a non-empty value for `task_id` but received {task_id!r}")
        return await self._delete(
            path_template("/api/tasks/{task_id}", task_id=task_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DeleteTaskResponse,
        )


class TasksResourceWithRawResponse:
    def __init__(self, tasks: TasksResource) -> None:
        self._tasks = tasks

        self.create = to_raw_response_wrapper(
            tasks.create,
        )
        self.retrieve = to_raw_response_wrapper(
            tasks.retrieve,
        )
        self.delete = to_raw_response_wrapper(
            tasks.delete,
        )


class AsyncTasksResourceWithRawResponse:
    def __init__(self, tasks: AsyncTasksResource) -> None:
        self._tasks = tasks

        self.create = async_to_raw_response_wrapper(
            tasks.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            tasks.retrieve,
        )
        self.delete = async_to_raw_response_wrapper(
            tasks.delete,
        )


class TasksResourceWithStreamingResponse:
    def __init__(self, tasks: TasksResource) -> None:
        self._tasks = tasks

        self.create = to_streamed_response_wrapper(
            tasks.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            tasks.retrieve,
        )
        self.delete = to_streamed_response_wrapper(
            tasks.delete,
        )


class AsyncTasksResourceWithStreamingResponse:
    def __init__(self, tasks: AsyncTasksResource) -> None:
        self._tasks = tasks

        self.create = async_to_streamed_response_wrapper(
            tasks.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            tasks.retrieve,
        )
        self.delete = async_to_streamed_response_wrapper(
            tasks.delete,
        )
