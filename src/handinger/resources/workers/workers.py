# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Literal

import httpx

from ...types import worker_create_params, worker_update_params, worker_retrieve_params
from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from .webhooks import (
    WebhooksResource,
    AsyncWebhooksResource,
    WebhooksResourceWithRawResponse,
    AsyncWebhooksResourceWithRawResponse,
    WebhooksResourceWithStreamingResponse,
    AsyncWebhooksResourceWithStreamingResponse,
)
from ..._compat import cached_property
from .schedules import (
    SchedulesResource,
    AsyncSchedulesResource,
    SchedulesResourceWithRawResponse,
    AsyncSchedulesResourceWithRawResponse,
    SchedulesResourceWithStreamingResponse,
    AsyncSchedulesResourceWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.worker import Worker
from ...types.worker_template import WorkerTemplate
from ...types.delete_worker_response import DeleteWorkerResponse
from ...types.worker_retrieve_email_response import WorkerRetrieveEmailResponse

__all__ = ["WorkersResource", "AsyncWorkersResource"]


class WorkersResource(SyncAPIResource):
    """Create, retrieve, and manage agent worker templates."""

    @cached_property
    def schedules(self) -> SchedulesResource:
        """Manage future and recurring worker tasks."""
        return SchedulesResource(self._client)

    @cached_property
    def webhooks(self) -> WebhooksResource:
        """Configure outbound webhooks delivered when a worker's tasks complete."""
        return WebhooksResource(self._client)

    @cached_property
    def with_raw_response(self) -> WorkersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/ramensoft/handinger-python#accessing-raw-response-data-eg-headers
        """
        return WorkersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> WorkersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/ramensoft/handinger-python#with_streaming_response
        """
        return WorkersResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        instructions: str | Omit = omit,
        output_schema: Dict[str, object] | Omit = omit,
        prompt: str | Omit = omit,
        summary: str | Omit = omit,
        title: str | Omit = omit,
        visibility: Literal["public", "private"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WorkerTemplate:
        """Create a new worker.

        The worker is a reusable agent template; tasks are runs
        against this template. Use `POST /tasks` to actually run the agent.

        Args:
          instructions: Persistent system prompt the worker uses for every task it runs.

          output_schema: Optional JSON Schema (Draft-07) describing the structured object the worker must
              produce. When set, every task response is validated against the schema and
              exposed as `structuredOutput`.

          prompt: Natural-language description of the worker to use for AI-generated instructions
              when `instructions` is omitted.

          summary: Short one-line description of the worker's purpose. Auto-generated when omitted
              and a `prompt` is provided.

          title: Optional display name. When omitted, Handinger assigns a random dog-themed name.

          visibility: `public` (default) is visible to all org members. `private` is only visible to
              invited members.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/workers",
            body=maybe_transform(
                {
                    "instructions": instructions,
                    "output_schema": output_schema,
                    "prompt": prompt,
                    "summary": summary,
                    "title": title,
                    "visibility": visibility,
                },
                worker_create_params.WorkerCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WorkerTemplate,
        )

    def retrieve(
        self,
        worker_id: str,
        *,
        task_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Worker:
        """
        Retrieve the current worker state and messages from its most recent task (or a
        specific task via `taskId`).

        Args:
          task_id: Return the worker state and messages for a specific task instead of the most
              recent one.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not worker_id:
            raise ValueError(f"Expected a non-empty value for `worker_id` but received {worker_id!r}")
        return self._get(
            path_template("/api/workers/{worker_id}", worker_id=worker_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"task_id": task_id}, worker_retrieve_params.WorkerRetrieveParams),
            ),
            cast_to=Worker,
        )

    def update(
        self,
        worker_id: str,
        *,
        instructions: str | Omit = omit,
        output_schema: Optional[Dict[str, object]] | Omit = omit,
        summary: str | Omit = omit,
        title: str | Omit = omit,
        visibility: Literal["public", "private"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WorkerTemplate:
        """
        Update a worker's instructions, title, summary, visibility, or output schema.
        Only the fields you send are changed; omitted fields keep their current values.
        Only the worker creator can update a worker.

        Args:
          instructions: Replaces the persistent system prompt. Subsequent tasks pick up the new
              instructions immediately; in-flight tasks keep using the previous version.

          output_schema: Replace the worker's structured output schema. Pass `null` to clear it and
              return to free-form text responses.

          summary: Replaces the worker's short one-line summary.

          title: New display name for the worker.

          visibility: Change visibility between `public` (any org member can run tasks) and `private`
              (only invited members).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not worker_id:
            raise ValueError(f"Expected a non-empty value for `worker_id` but received {worker_id!r}")
        return self._patch(
            path_template("/api/workers/{worker_id}", worker_id=worker_id),
            body=maybe_transform(
                {
                    "instructions": instructions,
                    "output_schema": output_schema,
                    "summary": summary,
                    "title": title,
                    "visibility": visibility,
                },
                worker_update_params.WorkerUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WorkerTemplate,
        )

    def delete(
        self,
        worker_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DeleteWorkerResponse:
        """
        Soft-delete a worker template so it no longer appears in list or retrieve
        endpoints. Tasks, turns, files, schedules, and integrations remain in the
        database for analytics. Only the worker creator can delete a worker.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not worker_id:
            raise ValueError(f"Expected a non-empty value for `worker_id` but received {worker_id!r}")
        return self._delete(
            path_template("/api/workers/{worker_id}", worker_id=worker_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DeleteWorkerResponse,
        )

    def retrieve_email(
        self,
        worker_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WorkerRetrieveEmailResponse:
        """
        Retrieve the inbound email address for a worker.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not worker_id:
            raise ValueError(f"Expected a non-empty value for `worker_id` but received {worker_id!r}")
        return self._get(
            path_template("/api/workers/{worker_id}/email", worker_id=worker_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WorkerRetrieveEmailResponse,
        )


class AsyncWorkersResource(AsyncAPIResource):
    """Create, retrieve, and manage agent worker templates."""

    @cached_property
    def schedules(self) -> AsyncSchedulesResource:
        """Manage future and recurring worker tasks."""
        return AsyncSchedulesResource(self._client)

    @cached_property
    def webhooks(self) -> AsyncWebhooksResource:
        """Configure outbound webhooks delivered when a worker's tasks complete."""
        return AsyncWebhooksResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncWorkersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/ramensoft/handinger-python#accessing-raw-response-data-eg-headers
        """
        return AsyncWorkersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncWorkersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/ramensoft/handinger-python#with_streaming_response
        """
        return AsyncWorkersResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        instructions: str | Omit = omit,
        output_schema: Dict[str, object] | Omit = omit,
        prompt: str | Omit = omit,
        summary: str | Omit = omit,
        title: str | Omit = omit,
        visibility: Literal["public", "private"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WorkerTemplate:
        """Create a new worker.

        The worker is a reusable agent template; tasks are runs
        against this template. Use `POST /tasks` to actually run the agent.

        Args:
          instructions: Persistent system prompt the worker uses for every task it runs.

          output_schema: Optional JSON Schema (Draft-07) describing the structured object the worker must
              produce. When set, every task response is validated against the schema and
              exposed as `structuredOutput`.

          prompt: Natural-language description of the worker to use for AI-generated instructions
              when `instructions` is omitted.

          summary: Short one-line description of the worker's purpose. Auto-generated when omitted
              and a `prompt` is provided.

          title: Optional display name. When omitted, Handinger assigns a random dog-themed name.

          visibility: `public` (default) is visible to all org members. `private` is only visible to
              invited members.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/workers",
            body=await async_maybe_transform(
                {
                    "instructions": instructions,
                    "output_schema": output_schema,
                    "prompt": prompt,
                    "summary": summary,
                    "title": title,
                    "visibility": visibility,
                },
                worker_create_params.WorkerCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WorkerTemplate,
        )

    async def retrieve(
        self,
        worker_id: str,
        *,
        task_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Worker:
        """
        Retrieve the current worker state and messages from its most recent task (or a
        specific task via `taskId`).

        Args:
          task_id: Return the worker state and messages for a specific task instead of the most
              recent one.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not worker_id:
            raise ValueError(f"Expected a non-empty value for `worker_id` but received {worker_id!r}")
        return await self._get(
            path_template("/api/workers/{worker_id}", worker_id=worker_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"task_id": task_id}, worker_retrieve_params.WorkerRetrieveParams),
            ),
            cast_to=Worker,
        )

    async def update(
        self,
        worker_id: str,
        *,
        instructions: str | Omit = omit,
        output_schema: Optional[Dict[str, object]] | Omit = omit,
        summary: str | Omit = omit,
        title: str | Omit = omit,
        visibility: Literal["public", "private"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WorkerTemplate:
        """
        Update a worker's instructions, title, summary, visibility, or output schema.
        Only the fields you send are changed; omitted fields keep their current values.
        Only the worker creator can update a worker.

        Args:
          instructions: Replaces the persistent system prompt. Subsequent tasks pick up the new
              instructions immediately; in-flight tasks keep using the previous version.

          output_schema: Replace the worker's structured output schema. Pass `null` to clear it and
              return to free-form text responses.

          summary: Replaces the worker's short one-line summary.

          title: New display name for the worker.

          visibility: Change visibility between `public` (any org member can run tasks) and `private`
              (only invited members).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not worker_id:
            raise ValueError(f"Expected a non-empty value for `worker_id` but received {worker_id!r}")
        return await self._patch(
            path_template("/api/workers/{worker_id}", worker_id=worker_id),
            body=await async_maybe_transform(
                {
                    "instructions": instructions,
                    "output_schema": output_schema,
                    "summary": summary,
                    "title": title,
                    "visibility": visibility,
                },
                worker_update_params.WorkerUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WorkerTemplate,
        )

    async def delete(
        self,
        worker_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DeleteWorkerResponse:
        """
        Soft-delete a worker template so it no longer appears in list or retrieve
        endpoints. Tasks, turns, files, schedules, and integrations remain in the
        database for analytics. Only the worker creator can delete a worker.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not worker_id:
            raise ValueError(f"Expected a non-empty value for `worker_id` but received {worker_id!r}")
        return await self._delete(
            path_template("/api/workers/{worker_id}", worker_id=worker_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DeleteWorkerResponse,
        )

    async def retrieve_email(
        self,
        worker_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WorkerRetrieveEmailResponse:
        """
        Retrieve the inbound email address for a worker.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not worker_id:
            raise ValueError(f"Expected a non-empty value for `worker_id` but received {worker_id!r}")
        return await self._get(
            path_template("/api/workers/{worker_id}/email", worker_id=worker_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WorkerRetrieveEmailResponse,
        )


class WorkersResourceWithRawResponse:
    def __init__(self, workers: WorkersResource) -> None:
        self._workers = workers

        self.create = to_raw_response_wrapper(
            workers.create,
        )
        self.retrieve = to_raw_response_wrapper(
            workers.retrieve,
        )
        self.update = to_raw_response_wrapper(
            workers.update,
        )
        self.delete = to_raw_response_wrapper(
            workers.delete,
        )
        self.retrieve_email = to_raw_response_wrapper(
            workers.retrieve_email,
        )

    @cached_property
    def schedules(self) -> SchedulesResourceWithRawResponse:
        """Manage future and recurring worker tasks."""
        return SchedulesResourceWithRawResponse(self._workers.schedules)

    @cached_property
    def webhooks(self) -> WebhooksResourceWithRawResponse:
        """Configure outbound webhooks delivered when a worker's tasks complete."""
        return WebhooksResourceWithRawResponse(self._workers.webhooks)


class AsyncWorkersResourceWithRawResponse:
    def __init__(self, workers: AsyncWorkersResource) -> None:
        self._workers = workers

        self.create = async_to_raw_response_wrapper(
            workers.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            workers.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            workers.update,
        )
        self.delete = async_to_raw_response_wrapper(
            workers.delete,
        )
        self.retrieve_email = async_to_raw_response_wrapper(
            workers.retrieve_email,
        )

    @cached_property
    def schedules(self) -> AsyncSchedulesResourceWithRawResponse:
        """Manage future and recurring worker tasks."""
        return AsyncSchedulesResourceWithRawResponse(self._workers.schedules)

    @cached_property
    def webhooks(self) -> AsyncWebhooksResourceWithRawResponse:
        """Configure outbound webhooks delivered when a worker's tasks complete."""
        return AsyncWebhooksResourceWithRawResponse(self._workers.webhooks)


class WorkersResourceWithStreamingResponse:
    def __init__(self, workers: WorkersResource) -> None:
        self._workers = workers

        self.create = to_streamed_response_wrapper(
            workers.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            workers.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            workers.update,
        )
        self.delete = to_streamed_response_wrapper(
            workers.delete,
        )
        self.retrieve_email = to_streamed_response_wrapper(
            workers.retrieve_email,
        )

    @cached_property
    def schedules(self) -> SchedulesResourceWithStreamingResponse:
        """Manage future and recurring worker tasks."""
        return SchedulesResourceWithStreamingResponse(self._workers.schedules)

    @cached_property
    def webhooks(self) -> WebhooksResourceWithStreamingResponse:
        """Configure outbound webhooks delivered when a worker's tasks complete."""
        return WebhooksResourceWithStreamingResponse(self._workers.webhooks)


class AsyncWorkersResourceWithStreamingResponse:
    def __init__(self, workers: AsyncWorkersResource) -> None:
        self._workers = workers

        self.create = async_to_streamed_response_wrapper(
            workers.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            workers.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            workers.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            workers.delete,
        )
        self.retrieve_email = async_to_streamed_response_wrapper(
            workers.retrieve_email,
        )

    @cached_property
    def schedules(self) -> AsyncSchedulesResourceWithStreamingResponse:
        """Manage future and recurring worker tasks."""
        return AsyncSchedulesResourceWithStreamingResponse(self._workers.schedules)

    @cached_property
    def webhooks(self) -> AsyncWebhooksResourceWithStreamingResponse:
        """Configure outbound webhooks delivered when a worker's tasks complete."""
        return AsyncWebhooksResourceWithStreamingResponse(self._workers.webhooks)
