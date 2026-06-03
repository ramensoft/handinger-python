# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from handinger import Handinger, AsyncHandinger
from tests.utils import assert_matches_type
from handinger.types import (
    Worker,
    WorkerTemplate,
    DeleteWorkerResponse,
    WorkerRetrieveEmailResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestWorkers:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Handinger) -> None:
        worker = client.workers.create()
        assert_matches_type(WorkerTemplate, worker, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Handinger) -> None:
        worker = client.workers.create(
            instructions="You are a brand voice analyzer. Read the input text and report whether it matches Acme's playful, plain-spoken house style. Quote specific phrases.",
            output_schema={
                "type": "bar",
                "required": "bar",
                "properties": "bar",
            },
            prompt="A worker that fact-checks short claims and returns a verdict with citations.",
            summary="Audits copy against the Acme brand voice guide.",
            title="Brand voice analyzer",
            visibility="public",
        )
        assert_matches_type(WorkerTemplate, worker, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Handinger) -> None:
        response = client.workers.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        worker = response.parse()
        assert_matches_type(WorkerTemplate, worker, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Handinger) -> None:
        with client.workers.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            worker = response.parse()
            assert_matches_type(WorkerTemplate, worker, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Handinger) -> None:
        worker = client.workers.retrieve(
            worker_id="t_org_123_w_01HZY2ZJQ8G7K42W2D7WF6V4GM",
        )
        assert_matches_type(Worker, worker, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_with_all_params(self, client: Handinger) -> None:
        worker = client.workers.retrieve(
            worker_id="t_org_123_w_01HZY2ZJQ8G7K42W2D7WF6V4GM",
            task_id="x",
        )
        assert_matches_type(Worker, worker, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Handinger) -> None:
        response = client.workers.with_raw_response.retrieve(
            worker_id="t_org_123_w_01HZY2ZJQ8G7K42W2D7WF6V4GM",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        worker = response.parse()
        assert_matches_type(Worker, worker, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Handinger) -> None:
        with client.workers.with_streaming_response.retrieve(
            worker_id="t_org_123_w_01HZY2ZJQ8G7K42W2D7WF6V4GM",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            worker = response.parse()
            assert_matches_type(Worker, worker, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Handinger) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `worker_id` but received ''"):
            client.workers.with_raw_response.retrieve(
                worker_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: Handinger) -> None:
        worker = client.workers.update(
            worker_id="t_org_123_w_01HZY2ZJQ8G7K42W2D7WF6V4GM",
        )
        assert_matches_type(WorkerTemplate, worker, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Handinger) -> None:
        worker = client.workers.update(
            worker_id="t_org_123_w_01HZY2ZJQ8G7K42W2D7WF6V4GM",
            instructions="You are a brand voice analyzer. Read the input text and report whether it matches Acme's playful, plain-spoken house style. Quote specific phrases.",
            output_schema={
                "type": "bar",
                "required": "bar",
                "properties": "bar",
            },
            summary="Audits copy against the Acme brand voice guide.",
            title="Claim verdict v2",
            visibility="private",
        )
        assert_matches_type(WorkerTemplate, worker, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Handinger) -> None:
        response = client.workers.with_raw_response.update(
            worker_id="t_org_123_w_01HZY2ZJQ8G7K42W2D7WF6V4GM",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        worker = response.parse()
        assert_matches_type(WorkerTemplate, worker, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Handinger) -> None:
        with client.workers.with_streaming_response.update(
            worker_id="t_org_123_w_01HZY2ZJQ8G7K42W2D7WF6V4GM",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            worker = response.parse()
            assert_matches_type(WorkerTemplate, worker, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Handinger) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `worker_id` but received ''"):
            client.workers.with_raw_response.update(
                worker_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Handinger) -> None:
        worker = client.workers.delete(
            "t_org_123_w_01HZY2ZJQ8G7K42W2D7WF6V4GM",
        )
        assert_matches_type(DeleteWorkerResponse, worker, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Handinger) -> None:
        response = client.workers.with_raw_response.delete(
            "t_org_123_w_01HZY2ZJQ8G7K42W2D7WF6V4GM",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        worker = response.parse()
        assert_matches_type(DeleteWorkerResponse, worker, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Handinger) -> None:
        with client.workers.with_streaming_response.delete(
            "t_org_123_w_01HZY2ZJQ8G7K42W2D7WF6V4GM",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            worker = response.parse()
            assert_matches_type(DeleteWorkerResponse, worker, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Handinger) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `worker_id` but received ''"):
            client.workers.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_email(self, client: Handinger) -> None:
        worker = client.workers.retrieve_email(
            "t_org_123_w_01HZY2ZJQ8G7K42W2D7WF6V4GM",
        )
        assert_matches_type(WorkerRetrieveEmailResponse, worker, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_email(self, client: Handinger) -> None:
        response = client.workers.with_raw_response.retrieve_email(
            "t_org_123_w_01HZY2ZJQ8G7K42W2D7WF6V4GM",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        worker = response.parse()
        assert_matches_type(WorkerRetrieveEmailResponse, worker, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_email(self, client: Handinger) -> None:
        with client.workers.with_streaming_response.retrieve_email(
            "t_org_123_w_01HZY2ZJQ8G7K42W2D7WF6V4GM",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            worker = response.parse()
            assert_matches_type(WorkerRetrieveEmailResponse, worker, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve_email(self, client: Handinger) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `worker_id` but received ''"):
            client.workers.with_raw_response.retrieve_email(
                "",
            )


class TestAsyncWorkers:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncHandinger) -> None:
        worker = await async_client.workers.create()
        assert_matches_type(WorkerTemplate, worker, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncHandinger) -> None:
        worker = await async_client.workers.create(
            instructions="You are a brand voice analyzer. Read the input text and report whether it matches Acme's playful, plain-spoken house style. Quote specific phrases.",
            output_schema={
                "type": "bar",
                "required": "bar",
                "properties": "bar",
            },
            prompt="A worker that fact-checks short claims and returns a verdict with citations.",
            summary="Audits copy against the Acme brand voice guide.",
            title="Brand voice analyzer",
            visibility="public",
        )
        assert_matches_type(WorkerTemplate, worker, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncHandinger) -> None:
        response = await async_client.workers.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        worker = await response.parse()
        assert_matches_type(WorkerTemplate, worker, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncHandinger) -> None:
        async with async_client.workers.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            worker = await response.parse()
            assert_matches_type(WorkerTemplate, worker, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncHandinger) -> None:
        worker = await async_client.workers.retrieve(
            worker_id="t_org_123_w_01HZY2ZJQ8G7K42W2D7WF6V4GM",
        )
        assert_matches_type(Worker, worker, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncHandinger) -> None:
        worker = await async_client.workers.retrieve(
            worker_id="t_org_123_w_01HZY2ZJQ8G7K42W2D7WF6V4GM",
            task_id="x",
        )
        assert_matches_type(Worker, worker, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncHandinger) -> None:
        response = await async_client.workers.with_raw_response.retrieve(
            worker_id="t_org_123_w_01HZY2ZJQ8G7K42W2D7WF6V4GM",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        worker = await response.parse()
        assert_matches_type(Worker, worker, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncHandinger) -> None:
        async with async_client.workers.with_streaming_response.retrieve(
            worker_id="t_org_123_w_01HZY2ZJQ8G7K42W2D7WF6V4GM",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            worker = await response.parse()
            assert_matches_type(Worker, worker, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncHandinger) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `worker_id` but received ''"):
            await async_client.workers.with_raw_response.retrieve(
                worker_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncHandinger) -> None:
        worker = await async_client.workers.update(
            worker_id="t_org_123_w_01HZY2ZJQ8G7K42W2D7WF6V4GM",
        )
        assert_matches_type(WorkerTemplate, worker, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncHandinger) -> None:
        worker = await async_client.workers.update(
            worker_id="t_org_123_w_01HZY2ZJQ8G7K42W2D7WF6V4GM",
            instructions="You are a brand voice analyzer. Read the input text and report whether it matches Acme's playful, plain-spoken house style. Quote specific phrases.",
            output_schema={
                "type": "bar",
                "required": "bar",
                "properties": "bar",
            },
            summary="Audits copy against the Acme brand voice guide.",
            title="Claim verdict v2",
            visibility="private",
        )
        assert_matches_type(WorkerTemplate, worker, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncHandinger) -> None:
        response = await async_client.workers.with_raw_response.update(
            worker_id="t_org_123_w_01HZY2ZJQ8G7K42W2D7WF6V4GM",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        worker = await response.parse()
        assert_matches_type(WorkerTemplate, worker, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncHandinger) -> None:
        async with async_client.workers.with_streaming_response.update(
            worker_id="t_org_123_w_01HZY2ZJQ8G7K42W2D7WF6V4GM",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            worker = await response.parse()
            assert_matches_type(WorkerTemplate, worker, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncHandinger) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `worker_id` but received ''"):
            await async_client.workers.with_raw_response.update(
                worker_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncHandinger) -> None:
        worker = await async_client.workers.delete(
            "t_org_123_w_01HZY2ZJQ8G7K42W2D7WF6V4GM",
        )
        assert_matches_type(DeleteWorkerResponse, worker, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncHandinger) -> None:
        response = await async_client.workers.with_raw_response.delete(
            "t_org_123_w_01HZY2ZJQ8G7K42W2D7WF6V4GM",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        worker = await response.parse()
        assert_matches_type(DeleteWorkerResponse, worker, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncHandinger) -> None:
        async with async_client.workers.with_streaming_response.delete(
            "t_org_123_w_01HZY2ZJQ8G7K42W2D7WF6V4GM",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            worker = await response.parse()
            assert_matches_type(DeleteWorkerResponse, worker, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncHandinger) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `worker_id` but received ''"):
            await async_client.workers.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_email(self, async_client: AsyncHandinger) -> None:
        worker = await async_client.workers.retrieve_email(
            "t_org_123_w_01HZY2ZJQ8G7K42W2D7WF6V4GM",
        )
        assert_matches_type(WorkerRetrieveEmailResponse, worker, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_email(self, async_client: AsyncHandinger) -> None:
        response = await async_client.workers.with_raw_response.retrieve_email(
            "t_org_123_w_01HZY2ZJQ8G7K42W2D7WF6V4GM",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        worker = await response.parse()
        assert_matches_type(WorkerRetrieveEmailResponse, worker, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_email(self, async_client: AsyncHandinger) -> None:
        async with async_client.workers.with_streaming_response.retrieve_email(
            "t_org_123_w_01HZY2ZJQ8G7K42W2D7WF6V4GM",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            worker = await response.parse()
            assert_matches_type(WorkerRetrieveEmailResponse, worker, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve_email(self, async_client: AsyncHandinger) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `worker_id` but received ''"):
            await async_client.workers.with_raw_response.retrieve_email(
                "",
            )
