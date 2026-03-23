# Seclai Python SDK

The official Python SDK for the [Seclai](https://seclai.com) API. Provides typed wrappers for the Seclai API, file uploads, SSE streaming, polling helpers, and full async support.

Requires Python 3.11+.

## Install

```bash
pip install seclai
```

## Exports

All public symbols are available from the top-level `seclai` package:

```python
from seclai import (
    Seclai,                     # Synchronous client
    AsyncSeclai,                # Asynchronous client
    SeclaiError,                # Base exception
    SeclaiConfigurationError,   # Missing API key / invalid config
    SeclaiAPIStatusError,       # Non-2xx HTTP response
    SeclaiAPIValidationError,   # HTTP 422 validation error
    SeclaiStreamingError,       # SSE stream error event
    AgentRunStreamRequest,      # TypedDict for streaming run requests
    JSONValue,                  # Recursive JSON type alias
)
```

## Quick start

```python
from seclai import Seclai

client = Seclai(api_key="...")

# List agents
agents = client.list_agents()
print(agents)

# Run an agent and stream the result
from seclai import AgentRunStreamRequest

run = client.run_streaming_agent_and_wait(
    "agent_id",
    body=AgentRunStreamRequest(input="Summarize the latest uploads", metadata={}),
    timeout=60.0,
)
print("run:", run.run_id, "status:", run.status)
```

### Async client

```python
import asyncio
from seclai import AsyncSeclai

async def main():
    async with AsyncSeclai(api_key="...") as client:
        agents = await client.list_agents()
        print(agents)

asyncio.run(main())
```

## Configuration

| Option | Environment variable | Default |
| --- | --- | --- |
| `api_key` | `SECLAI_API_KEY` | *required* |
| `timeout` | — | `30.0` (seconds) |
| `api_key_header` | — | `x-api-key` |
| `default_headers` | — | `None` |
| `http_client` | — | `None` (auto-created `httpx.Client`) |

```python
client = Seclai(
    api_key="...",
    timeout=60.0,
    default_headers={"x-custom": "value"},
)
```

Set `SECLAI_API_URL` to point at a different API host (e.g., staging):

```bash
export SECLAI_API_URL="https://staging-api.seclai.com"
```

## API documentation

Online API documentation (latest):

https://seclai.github.io/seclai-python/latest/

## Resources

### Agents

```python
# CRUD
agents = client.list_agents(page=1, limit=20)
agent = client.create_agent({"name": "My Agent", "description": "..."})
fetched = client.get_agent("agent_id")
updated = client.update_agent("agent_id", {"name": "Renamed"})
client.delete_agent("agent_id")

# Definition (step workflow)
definition = client.get_agent_definition("agent_id")
client.update_agent_definition("agent_id", {
    "change_id": definition["change_id"],
    "steps": [{"type": "llm", "config": {}}],
})
```

### Agent runs

```python
from seclai._generated.models.agent_run_request import AgentRunRequest

# Start a run
run = client.run_agent("agent_id", AgentRunRequest(input_="Hello"))

# List & search runs
runs = client.list_agent_runs("agent_id")
search = client.search_agent_runs({"query": "test"})

# Fetch run details (optionally with step outputs)
detail = client.get_agent_run("run_id", include_step_outputs=True)

# Cancel or delete
client.cancel_agent_run("run_id")
client.delete_agent_run("run_id")
```

### Streaming

The SDK provides two streaming patterns over the SSE `/runs/stream` endpoint.

**Block until done** — returns the final `done` payload or raises on timeout:

```python
from seclai import AgentRunStreamRequest

run = client.run_streaming_agent_and_wait(
    "agent_id",
    body=AgentRunStreamRequest(input="Hello from streaming", metadata={}),
    timeout=60.0,
)
```

**Generator-based** — yields every SSE event as `(event_type, data)` tuples:

```python
for event_type, data in client.run_streaming_agent(
    "agent_id",
    body=AgentRunStreamRequest(input="Hello", metadata={}),
):
    print(event_type, data)
```

Async:

```python
async for event_type, data in client.run_streaming_agent(
    "agent_id",
    body=AgentRunStreamRequest(input="Hello", metadata={}),
):
    print(event_type, data)
```

### Polling

For environments where SSE is not practical, poll for a completed run:

```python
from seclai._generated.models.agent_run_request import AgentRunRequest

result = client.run_agent_and_poll(
    "agent_id",
    AgentRunRequest(input_="Hello"),
    poll_interval=2.0,
)
```

### Agent input uploads

```python
upload = client.upload_agent_input("agent_id", file=b"data", file_name="input.pdf")
status = client.get_agent_input_upload_status("agent_id", upload["upload_id"])
```

### Agent AI assistant

```python
steps = client.generate_agent_steps("agent_id", {"user_input": "Build a RAG pipeline"})
config = client.generate_step_config("agent_id", {"step_type": "llm", "user_input": "..."})

# Conversation history
history = client.get_agent_ai_conversation_history("agent_id")
client.mark_agent_ai_suggestion("agent_id", "conversation_id", {"accepted": True})
```

### Agent evaluations

```python
# CRUD
criteria_list = client.list_evaluation_criteria("agent_id")
criteria = client.create_evaluation_criteria("agent_id", {"name": "accuracy"})
detail = client.get_evaluation_criteria("criteria_id")
client.update_evaluation_criteria("criteria_id", {"name": "updated"})
client.delete_evaluation_criteria("criteria_id")

# Test a draft
client.test_draft_evaluation("agent_id", {"criteria": {}, "run_id": "run_id"})

# Results & summaries
results = client.list_evaluation_results("criteria_id")
summary = client.get_evaluation_criteria_summary("criteria_id")
client.create_evaluation_result("criteria_id", {"run_id": "run_id", "score": 0.9})

# Results by run
run_results = client.list_run_evaluation_results("agent_id", "run_id")
non_manual = client.get_non_manual_evaluation_summary("agent_id")
compatible = client.list_compatible_runs("criteria_id")
```

### Knowledge bases

```python
kbs = client.list_knowledge_bases()
kb = client.create_knowledge_base({"name": "My KB"})
fetched = client.get_knowledge_base("kb_id")
client.update_knowledge_base("kb_id", {"name": "Renamed"})
client.delete_knowledge_base("kb_id")
```

### Memory banks

```python
banks = client.list_memory_banks()
bank = client.create_memory_bank({"name": "Chat Memory", "type": "conversation"})
fetched = client.get_memory_bank("mb_id")
client.update_memory_bank("mb_id", {"name": "Updated"})
client.delete_memory_bank("mb_id")

# Stats & compaction
stats = client.get_memory_bank_stats("mb_id")
client.compact_memory_bank("mb_id")

# Test compaction
test = client.test_memory_bank_compaction("mb_id", {"entries": []})
standalone = client.test_compaction_prompt_standalone({"prompt": "test"})

# Templates & agents
templates = client.list_memory_bank_templates()
agents = client.get_agents_using_memory_bank("mb_id")

# AI assistant
suggestion = client.generate_memory_bank_config({"user_input": "Create a bank"})
last_conv = client.get_memory_bank_ai_last_conversation()
client.accept_memory_bank_ai_suggestion("conversation_id", {"accepted": True})

# Source management
client.delete_memory_bank_source("mb_id")
```

### Sources

```python
sources = client.list_sources(page=1, limit=20)
source = client.create_source({"name": "My Source"})
fetched = client.get_source("source_id")
client.update_source("source_id", {"name": "Updated"})
client.delete_source("source_id")
```

### File uploads

Upload a file to a source (max 200 MiB):

```python
upload = client.upload_file_to_source(
    "source_id",
    file="./document.pdf",
    title="Q4 Report",
    metadata={"department": "finance"},
)
```

Upload inline text:

```python
upload = client.upload_inline_text_to_source("source_connection_id", {
    "title": "Greeting",
    "content": "Hello, world!",
})
```

Replace a content version with a new file:

```python
upload = client.upload_file_to_content(
    "content_version_id",
    file="./updated.pdf",
    metadata={"revision": 2},
)
```

Replace a content version with inline text:

```python
client.replace_content_with_inline_text("content_version_id", {
    "title": "Updated",
    "content": "New content text",
})
```

### Source exports

```python
exports = client.list_source_exports("source_id")
export = client.create_source_export("source_id", {"format": "json"})
status = client.get_source_export("source_id", "export_id")
estimate = client.estimate_source_export("source_id", {"format": "json"})
response = client.download_source_export("source_id", "export_id")  # raw httpx.Response
client.delete_source_export("source_id", "export_id")
client.cancel_source_export("source_id", "export_id")
```

### Source embedding migrations

```python
migration = client.get_source_embedding_migration("source_id")
client.start_source_embedding_migration("source_id", {"target_model": "v2"})
client.cancel_source_embedding_migration("source_id")
```

### Content

```python
detail = client.get_content_detail("content_id")
embeddings = client.list_content_embeddings("content_id")
client.delete_content("content_id")
```

### Solutions

```python
solutions = client.list_solutions()
sol = client.create_solution({"name": "My Solution"})
fetched = client.get_solution("solution_id")
client.update_solution("solution_id", {"name": "Renamed"})
client.delete_solution("solution_id")

# Link / unlink resources
client.link_agents_to_solution("solution_id", {"agent_ids": ["a1"]})
client.unlink_agents_from_solution("solution_id", {"agent_ids": ["a1"]})
client.link_knowledge_bases_to_solution("solution_id", {"kb_ids": ["kb1"]})
client.unlink_knowledge_bases_from_solution("solution_id", {"kb_ids": ["kb1"]})
client.link_source_connections_to_solution("solution_id", {"sc_ids": ["sc1"]})
client.unlink_source_connections_from_solution("solution_id", {"sc_ids": ["sc1"]})

# AI assistant
plan = client.generate_solution_ai_plan("solution_id", {"user_input": "Build it"})
client.accept_solution_ai_plan("solution_id", "conversation_id", {})
client.decline_solution_ai_plan("solution_id", "conversation_id")

# AI-generated resources
client.generate_solution_ai_knowledge_base("solution_id", {"user_input": "..."})
client.generate_solution_ai_source("solution_id", {"user_input": "..."})

# Conversations
convs = client.list_solution_conversations("solution_id")
client.add_solution_conversation_turn("solution_id", {"user_input": "..."})
client.mark_solution_conversation_turn("solution_id", "conversation_id", {"accepted": True})
```

### Governance AI

```python
plan = client.generate_governance_ai_plan({"user_input": "Create a content policy"})
convs = client.list_governance_ai_conversations()
client.accept_governance_ai_plan("conversation_id")
client.decline_governance_ai_plan("conversation_id")
```

### Alerts

```python
alerts = client.list_alerts(status="active")
alert = client.get_alert("alert_id")
client.change_alert_status("alert_id", {"status": "resolved"})
client.add_alert_comment("alert_id", {"text": "Investigating"})

# Subscriptions
client.subscribe_to_alert("alert_id")
client.unsubscribe_from_alert("alert_id")

# Alert configs
configs = client.list_alert_configs()
client.create_alert_config({"name": "Config"})
config = client.get_alert_config("config_id")
client.update_alert_config("config_id", {"name": "Updated"})
client.delete_alert_config("config_id")

# Organization preferences
prefs = client.list_organization_alert_preferences()
client.update_organization_alert_preference("org_id", "anomaly", {"enabled": True})
```

### Models

```python
alerts = client.list_model_alerts()
client.mark_model_alert_read("alert_id")
client.mark_all_model_alerts_read()
unread = client.get_unread_model_alert_count()
recs = client.get_model_recommendations("model_id")
```

### Search

```python
results = client.search(query="quarterly report")
filtered = client.search(query="my agent", entity_type="agent", limit=5)
```

### Top-level AI assistant

```python
# Generate plans for different resource types
kb_plan = client.ai_assistant_knowledge_base({"user_input": "Create a product FAQ KB"})
source_plan = client.ai_assistant_source({"user_input": "Set up a docs source"})
solution_plan = client.ai_assistant_solution({"user_input": "Build a support bot"})
mb_plan = client.ai_assistant_memory_bank({"user_input": "Create a chat memory bank"})

# Accept or decline
client.accept_ai_assistant_plan("conversation_id", {"accepted": True})
client.decline_ai_assistant_plan("conversation_id")

# Memory bank conversation history
history = client.get_ai_assistant_memory_bank_history()
client.accept_ai_memory_bank_suggestion("conversation_id", {"accepted": True})

# Feedback
client.submit_ai_feedback({"rating": 5, "comment": "Helpful!"})
```

### Pagination

All list methods accept `page` and `limit` parameters. For auto-pagination across all pages, use the `paginate` helper:

```python
# Sync — yields items one by one (generator)
for agent in client.paginate("GET", "/agents"):
    print(agent["name"])

# With a custom items key
for alert in client.paginate("GET", "/alerts", items_key="items"):
    print(alert["id"])
```

```python
# Async — also an async generator
async for agent in client.paginate("GET", "/agents"):
    print(agent["name"])
```

## Error handling

All SDK errors inherit from `SeclaiError`. Use specific exception types for targeted handling:

```python
from seclai import (
    Seclai,
    SeclaiAPIStatusError,
    SeclaiAPIValidationError,
    SeclaiConfigurationError,
    SeclaiStreamingError,
)

client = Seclai(api_key="...")

try:
    from seclai._generated.models.agent_run_request import AgentRunRequest

    result = client.run_agent("agent_id", AgentRunRequest(input_="Hello"))
except SeclaiAPIValidationError as e:
    print("Validation error:", e.status_code, e.validation_error)
except SeclaiAPIStatusError as e:
    print("API error:", e.status_code, e.response_text)
except SeclaiStreamingError as e:
    print("Streaming error:", e.message, "run:", e.run_id)
except SeclaiConfigurationError as e:
    print("Config error:", e)
```

| Error type | When |
| --- | --- |
| `SeclaiConfigurationError` | Missing API key, invalid configuration |
| `SeclaiAPIStatusError` | Non-2xx HTTP response |
| `SeclaiAPIValidationError` | HTTP 422 (inherits `SeclaiAPIStatusError`) |
| `SeclaiStreamingError` | SSE stream error event received |

## Low-level access

Use `client.request()` for direct API requests:

```python
result = client.request("GET", "/custom/endpoint", params={"key": "value"})
```

## Development

### Testing

```bash
make test
```

To pass args through to pytest:

```bash
make test ARGS='-k auth'
```

### Formatting

```bash
make format
```

### Linting

```bash
make lint
```

### OpenAPI spec & regenerating the client

Copy the OpenAPI JSON file into `openapi/seclai.openapi.json`, then run:

```bash
make generate
```

### Generate docs

```bash
make docs
```

## Reporting issues

If you hit a bug or have a feature request, please open an issue and include:

- what you were trying to do
- a minimal repro snippet (if possible)
- the exception / traceback
- your environment (Python version, OS)

## License

MIT — see [LICENSE](LICENSE) for details.
