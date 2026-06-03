# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from handinger import Handinger, AsyncHandinger
from tests.utils import assert_matches_type
from handinger.types import Worker, TaskWithTurns, DeleteTaskResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTasks:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Handinger) -> None:
        task = client.tasks.create(
            input="What's the weather today in Barcelona?",
        )
        assert_matches_type(Worker, task, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Handinger) -> None:
        task = client.tasks.create(
            input="What's the weather today in Barcelona?",
            budget="standard",
            task_id="tsk_2Z-YWz3hFq6VlW",
            worker_id="wrk_vk81XUHKHG-qr4",
        )
        assert_matches_type(Worker, task, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Handinger) -> None:
        response = client.tasks.with_raw_response.create(
            input="What's the weather today in Barcelona?",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        task = response.parse()
        assert_matches_type(Worker, task, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Handinger) -> None:
        with client.tasks.with_streaming_response.create(
            input="What's the weather today in Barcelona?",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            task = response.parse()
            assert_matches_type(Worker, task, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Handinger) -> None:
        task = client.tasks.retrieve(
            "tsk_01HZY31W2SZJ8MJ2FQTR3M1K9D",
        )
        assert_matches_type(TaskWithTurns, task, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Handinger) -> None:
        response = client.tasks.with_raw_response.retrieve(
            "tsk_01HZY31W2SZJ8MJ2FQTR3M1K9D",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        task = response.parse()
        assert_matches_type(TaskWithTurns, task, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Handinger) -> None:
        with client.tasks.with_streaming_response.retrieve(
            "tsk_01HZY31W2SZJ8MJ2FQTR3M1K9D",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            task = response.parse()
            assert_matches_type(TaskWithTurns, task, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Handinger) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `task_id` but received ''"):
            client.tasks.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Handinger) -> None:
        task = client.tasks.delete(
            "tsk_01HZY31W2SZJ8MJ2FQTR3M1K9D",
        )
        assert_matches_type(DeleteTaskResponse, task, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Handinger) -> None:
        response = client.tasks.with_raw_response.delete(
            "tsk_01HZY31W2SZJ8MJ2FQTR3M1K9D",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        task = response.parse()
        assert_matches_type(DeleteTaskResponse, task, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Handinger) -> None:
        with client.tasks.with_streaming_response.delete(
            "tsk_01HZY31W2SZJ8MJ2FQTR3M1K9D",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            task = response.parse()
            assert_matches_type(DeleteTaskResponse, task, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Handinger) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `task_id` but received ''"):
            client.tasks.with_raw_response.delete(
                "",
            )


class TestAsyncTasks:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncHandinger) -> None:
        task = await async_client.tasks.create(
            input="What's the weather today in Barcelona?",
        )
        assert_matches_type(Worker, task, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncHandinger) -> None:
        task = await async_client.tasks.create(
            input="What's the weather today in Barcelona?",
            budget="standard",
            task_id="tsk_2Z-YWz3hFq6VlW",
            worker_id="wrk_vk81XUHKHG-qr4",
        )
        assert_matches_type(Worker, task, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncHandinger) -> None:
        response = await async_client.tasks.with_raw_response.create(
            input="What's the weather today in Barcelona?",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        task = await response.parse()
        assert_matches_type(Worker, task, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncHandinger) -> None:
        async with async_client.tasks.with_streaming_response.create(
            input="What's the weather today in Barcelona?",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            task = await response.parse()
            assert_matches_type(Worker, task, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncHandinger) -> None:
        task = await async_client.tasks.retrieve(
            "tsk_01HZY31W2SZJ8MJ2FQTR3M1K9D",
        )
        assert_matches_type(TaskWithTurns, task, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncHandinger) -> None:
        response = await async_client.tasks.with_raw_response.retrieve(
            "tsk_01HZY31W2SZJ8MJ2FQTR3M1K9D",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        task = await response.parse()
        assert_matches_type(TaskWithTurns, task, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncHandinger) -> None:
        async with async_client.tasks.with_streaming_response.retrieve(
            "tsk_01HZY31W2SZJ8MJ2FQTR3M1K9D",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            task = await response.parse()
            assert_matches_type(TaskWithTurns, task, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncHandinger) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `task_id` but received ''"):
            await async_client.tasks.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncHandinger) -> None:
        task = await async_client.tasks.delete(
            "tsk_01HZY31W2SZJ8MJ2FQTR3M1K9D",
        )
        assert_matches_type(DeleteTaskResponse, task, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncHandinger) -> None:
        response = await async_client.tasks.with_raw_response.delete(
            "tsk_01HZY31W2SZJ8MJ2FQTR3M1K9D",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        task = await response.parse()
        assert_matches_type(DeleteTaskResponse, task, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncHandinger) -> None:
        async with async_client.tasks.with_streaming_response.delete(
            "tsk_01HZY31W2SZJ8MJ2FQTR3M1K9D",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            task = await response.parse()
            assert_matches_type(DeleteTaskResponse, task, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncHandinger) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `task_id` but received ''"):
            await async_client.tasks.with_raw_response.delete(
                "",
            )
