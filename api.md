# Workers

Types:

```python
from handinger.types import (
    CreateWorker,
    DeleteWorkerResponse,
    UpdateWorker,
    Worker,
    WorkerTemplate,
    WorkerRetrieveEmailResponse,
)
```

Methods:

- <code title="post /api/workers">client.workers.<a href="./src/handinger/resources/workers/workers.py">create</a>(\*\*<a href="src/handinger/types/worker_create_params.py">params</a>) -> <a href="./src/handinger/types/worker_template.py">WorkerTemplate</a></code>
- <code title="get /api/workers/{workerId}">client.workers.<a href="./src/handinger/resources/workers/workers.py">retrieve</a>(worker_id, \*\*<a href="src/handinger/types/worker_retrieve_params.py">params</a>) -> <a href="./src/handinger/types/worker.py">Worker</a></code>
- <code title="patch /api/workers/{workerId}">client.workers.<a href="./src/handinger/resources/workers/workers.py">update</a>(worker_id, \*\*<a href="src/handinger/types/worker_update_params.py">params</a>) -> <a href="./src/handinger/types/worker_template.py">WorkerTemplate</a></code>
- <code title="delete /api/workers/{workerId}">client.workers.<a href="./src/handinger/resources/workers/workers.py">delete</a>(worker_id) -> <a href="./src/handinger/types/delete_worker_response.py">DeleteWorkerResponse</a></code>
- <code title="get /api/workers/{workerId}/email">client.workers.<a href="./src/handinger/resources/workers/workers.py">retrieve_email</a>(worker_id) -> <a href="./src/handinger/types/worker_retrieve_email_response.py">WorkerRetrieveEmailResponse</a></code>

## Schedules

Types:

```python
from handinger.types.workers import WorkerSchedule, ScheduleListResponse, ScheduleCancelResponse
```

Methods:

- <code title="post /api/workers/{workerId}/schedules">client.workers.schedules.<a href="./src/handinger/resources/workers/schedules.py">create</a>(worker_id, \*\*<a href="src/handinger/types/workers/schedule_create_params.py">params</a>) -> <a href="./src/handinger/types/workers/worker_schedule.py">WorkerSchedule</a></code>
- <code title="get /api/workers/{workerId}/schedules">client.workers.schedules.<a href="./src/handinger/resources/workers/schedules.py">list</a>(worker_id) -> <a href="./src/handinger/types/workers/schedule_list_response.py">ScheduleListResponse</a></code>
- <code title="delete /api/workers/{workerId}/schedules/{scheduleId}">client.workers.schedules.<a href="./src/handinger/resources/workers/schedules.py">cancel</a>(schedule_id, \*, worker_id) -> <a href="./src/handinger/types/workers/schedule_cancel_response.py">ScheduleCancelResponse</a></code>

## Webhooks

Types:

```python
from handinger.types.workers import UpdateWebhook, Webhook, WebhookExecution, WebhookExecutionList
```

Methods:

- <code title="get /api/workers/{workerId}/webhook">client.workers.webhooks.<a href="./src/handinger/resources/workers/webhooks.py">retrieve</a>(worker_id) -> <a href="./src/handinger/types/workers/webhook.py">Webhook</a></code>
- <code title="put /api/workers/{workerId}/webhook">client.workers.webhooks.<a href="./src/handinger/resources/workers/webhooks.py">update</a>(worker_id, \*\*<a href="src/handinger/types/workers/webhook_update_params.py">params</a>) -> <a href="./src/handinger/types/workers/webhook.py">Webhook</a></code>
- <code title="delete /api/workers/{workerId}/webhook">client.workers.webhooks.<a href="./src/handinger/resources/workers/webhooks.py">delete</a>(worker_id) -> <a href="./src/handinger/types/workers/webhook.py">Webhook</a></code>
- <code title="get /api/workers/{workerId}/webhook/executions">client.workers.webhooks.<a href="./src/handinger/resources/workers/webhooks.py">list_executions</a>(worker_id, \*\*<a href="src/handinger/types/workers/webhook_list_executions_params.py">params</a>) -> <a href="./src/handinger/types/workers/webhook_execution_list.py">WebhookExecutionList</a></code>
- <code title="post /api/workers/{workerId}/webhook/regenerate-token">client.workers.webhooks.<a href="./src/handinger/resources/workers/webhooks.py">regenerate_token</a>(worker_id) -> <a href="./src/handinger/types/workers/webhook.py">Webhook</a></code>

# Tasks

Types:

```python
from handinger.types import (
    CreateTask,
    DeleteTaskResponse,
    Task,
    TaskTurnList,
    Turn,
    TaskRetrieveResponse,
)
```

Methods:

- <code title="post /api/tasks">client.tasks.<a href="./src/handinger/resources/tasks.py">create</a>(\*\*<a href="src/handinger/types/task_create_params.py">params</a>) -> <a href="./src/handinger/types/worker.py">Worker</a></code>
- <code title="get /api/tasks/{taskId}">client.tasks.<a href="./src/handinger/resources/tasks.py">retrieve</a>(task_id) -> <a href="./src/handinger/types/task_retrieve_response.py">TaskRetrieveResponse</a></code>
- <code title="delete /api/tasks/{taskId}">client.tasks.<a href="./src/handinger/resources/tasks.py">delete</a>(task_id) -> <a href="./src/handinger/types/delete_task_response.py">DeleteTaskResponse</a></code>
- <code title="get /api/tasks/{taskId}/turns">client.tasks.<a href="./src/handinger/resources/tasks.py">list_turns</a>(task_id) -> <a href="./src/handinger/types/task_turn_list.py">TaskTurnList</a></code>
