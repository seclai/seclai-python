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
| `api_key` | `SECLAI_API_KEY` | — |
| `access_token` | — | — |
| `profile` | `SECLAI_PROFILE` | `"default"` |
| `config_dir` | `SECLAI_CONFIG_DIR` | `~/.seclai` |
| `auto_refresh` | — | `True` |
| `account_id` | — | — |
| `timeout` | — | `30.0` (seconds) |
| `api_key_header` | — | `x-api-key` |
| `default_headers` | — | `None` |
| `http_client` | — | `None` (auto-created `httpx.Client`) |

Ten methods wait without limit unless you pass `timeout` yourself: `run_agent()`,
`list_agent_runs()`, `get_agent_run()`, `delete_agent_run()`, `list_sources()`,
`get_content_detail()`, `delete_content()`, `list_content_embeddings()`,
`upload_file_to_source()` and `upload_file_to_content()`. The 30-second default
does not apply to them, and neither does the timeout of an `http_client` you
supply. Requests from every other method use a supplied client's own timeout.

Set `SECLAI_API_URL` to point at a different API host (e.g., staging):

```bash
export SECLAI_API_URL="https://staging-api.seclai.com"
```

### Authentication

Credentials are resolved via a chain (first match wins):

1. Explicit `api_key` option
2. Explicit `access_token` option (string or callable)
3. `SECLAI_API_KEY` environment variable
4. SSO — cached tokens from `~/.seclai/sso/cache/` (always available as fallback)

```python
# API key
client = Seclai(api_key="sk-...")
```

```python
# Static bearer token
client = Seclai(access_token="eyJhbGciOi...")
```

```python
# Dynamic bearer token provider (sync callable, called per request)
client = Seclai(access_token=lambda: get_token_from_vault())
```

```python
# Async provider — use AsyncSeclai for async callables
client = AsyncSeclai(access_token=get_token_async)
```

```python
# SSO profile (uses cached tokens, auto-refreshes)
client = Seclai(profile="my-profile")
```

```python
# Environment variable (no options needed)
# export SECLAI_API_KEY="sk-..."
client = Seclai()
```

#### SSO authentication

SSO is the default fallback when no explicit credentials are provided. The SDK
includes built-in production SSO defaults, so no configuration is needed:

```bash
npx @seclai/cli auth login    # authenticate via browser — works immediately
```

To customize SSO settings (e.g. for a staging environment), use `seclai configure sso`
or set environment variables:

| Variable | Description | Default |
|---|---|---|
| `SECLAI_SSO_DOMAIN` | Cognito domain | `auth.seclai.com` |
| `SECLAI_SSO_CLIENT_ID` | Cognito app client ID | `4bgf8v9qmc5puivbaqon9n5lmr` |
| `SECLAI_SSO_REGION` | AWS region | `us-west-2` |

## API documentation

Online API documentation (latest):

https://seclai.github.io/seclai-python/latest/

## API versioning

The API dates its backward-incompatible changes. Nothing changes for you until
you opt in, either per client or by pinning the account:

```python
from seclai import ApiVersion

client = Seclai(api_key="...", api_version=ApiVersion.V2026_07_27)  # Seclai-Version header

state = client.get_api_version()          # what this request resolved to
client.update_api_version(ApiVersion.V2026_07_27)  # pin the whole account
```

Leave `api_version` unset and the header is omitted, so the account's pinned
baseline applies and responses keep their current shapes. Upgrading this package
alone never changes the wire contract.

Known versions are on the `ApiVersion` string enum, alongside
`DEFAULT_API_VERSION` and `LATEST_API_VERSION`. A version this release was
**not** built against raises `SeclaiConfigurationError`: a newer version can
reshape responses, and this client would decode them incorrectly rather than
reject them. Upgrade the package to adopt a new version, or pass
`allow_unknown_api_version=True` if you have to move first and accept that risk.

The guard covers the header however it reaches the wire: `api_version`,
`default_headers`, a per-request `headers` argument, or the default headers of
an `http_client` you supply, which are checked at construction and again on
each request, exactly as a value in `default_headers` is. It covers nothing
else. An account pinned server-side can still be
newer than this release — `get_api_version()` reports the `effective_version` the
request resolved to, and comparing it against `LATEST_API_VERSION` is how you
detect the gap.

**What `2026-07-27` changes.** Undeclared query parameters become a 422 instead
of being ignored, and every list endpoint that answered with a bare array or
under a per-resource key moves to the canonical
`{"data": [...], "pagination": {...}}` envelope. The methods for those endpoints
return what they document on either shape, so code written against the default
still reads the result after you opt in:

| Declared return | Methods | From 2026-07-27 |
| --- | --- | --- |
| A list | `list_evaluation_criteria()`, `list_run_evaluation_results()`, `get_agent_callers()`, `list_inbound_email_rejections()`, `list_governance_ai_conversations()`, `list_solution_conversations()`, `list_models()`, `list_memory_bank_templates()`, `get_agents_using_memory_bank()`, `list_cloud_drive_providers()`, `list_cloud_drives()`, `get_agents_using_cloud_drive()`, `list_cloud_drive_rejections()` | Unchanged |
| `data`, from a bare array by default | `list_evaluation_criteria_page()`, `list_run_evaluation_results_page()` | `data`, plus `pagination` |
| `data` with flat `total`/`page`/`limit` | `list_evaluation_results()`, `list_agent_evaluation_results()`, `list_evaluation_runs()`, `list_compatible_runs()` | Unchanged, plus `pagination` |
| A per-resource key | `list_agent_email_optouts()` and `list_blocked_email_senders()` / `set_auto_block_mode()` (`items`), `list_alert_configs()` (`configs`), `list_organization_alert_preferences()` (`preferences`), `list_email_domains()` (`domains`), `list_knowledge_bases()` (`knowledge_bases`), `list_memory_banks()` (`memory_banks`), `list_model_alerts()` (`alerts`), `list_experiments()` (`experiments`), `get_generation_tiers()` (`tiers`), `list_embedding_models()` and `list_reranker_models()` (`models`) | The same key, plus `data` and `pagination` |

Where a method documents flat `total`, `page` or `limit`, the client fills them
from `pagination` after you opt in. Fields that sit beside a list, such as
`auto_block_mode`, the embedding defaults or the email-domain plan capabilities,
are present on both shapes. `pagination` is present only once you opt in, so
read it with `.get("pagination")`.

A 200 response that is not a list at all — an error-shaped object, text, or an
empty body — raises `SeclaiError` from every one of these methods.
`unwrap_items()` still reads either shape of any of these results.

Opting in also turns paging on for endpoints that returned everything by
default, so the same call can return fewer rows:

- `list_evaluation_criteria()` and `list_run_evaluation_results()` return every
  item by default and ignore `page`/`limit`. After you opt in they return one
  page: 50 items unless you pass `limit`, since this client sends `limit=50`.
  The list carries no sign of that; use `list_evaluation_criteria_page()` or
  `list_run_evaluation_results_page()` to see `pagination`.
- `list_alert_configs()` ignores `page` and `limit` by default and returns every
  config; after you opt in it returns one page of 50.
- `set_auto_block_mode()` returns the first 50 blocked senders on either shape.
  Its `total` is the account's full count by default, and the number of rows it
  returned after you opt in.

**Later versions.** Each is cumulative, and none changes a response shape this
client decodes:

| Version | What it changes |
| --- | --- |
| `2026-08-03` | `create_memory_bank()` and `update_memory_bank()` reject a non-zero `max_age_days` with a 400, and an omitted `retention_days` on create resolves per bank type |
| `2026-08-21` | `create_source()` rejects an embedding dimension its embedder does not support with a 400 — `list_embedding_models()` reports the supported ones |
| `2026-09-28` | Agent-definition writes use the current file-list grammar: an omitted `attachments` keeps the stored list and `[]` means no files |
| `2026-09-30` | A run's and a step's `output`, and a step's `input`, are the text rather than a JSON manifest; files are in `attachments` on every version |
| `2026-10-03` | A new LLM step written without `attachments` takes its parent's files, and a new retrieval step's matched media are its files |

## Resources

### Identity

```python
me = client.get_me()
print(me["account_id"])
for org in me["organizations"]:
    print(org["name"], org["account_id"])

# Act as an organization: Seclai(account_id=org["account_id"])
```

### Agents

```python
# CRUD
agents = client.list_agents(page=1, limit=20)
agent = client.create_agent({"name": "My Agent", "description": "..."})
fetched = client.get_agent("agent_id")

# Pause / resume — a disabled agent stops firing from every trigger path
callers = client.get_agent_callers("agent_id")  # live agents calling this one
client.disable_agent("agent_id")  # 409 if any caller above is still live
client.enable_agent("agent_id")
updated = client.update_agent("agent_id", {"name": "Renamed"})
client.delete_agent("agent_id")

# Definition (step workflow)
definition = client.get_agent_definition("agent_id")
client.update_agent_definition("agent_id", {
    "change_id": definition["change_id"],
    "steps": [{"type": "llm", "config": {}}],
})

# Export / import an agent
exported = client.export_agent("agent_id")

# Validate the payload first to surface unresolved entity refs in this account
preview = client.preview_import_agent({"agent_definition": exported})
entity_remap = {
    ref["ref_id"]: ""  # pick a target uuid from ref["alternatives"]
    for ref in preview.get("unresolved_refs", [])
}

# Commit — `entity_remap` substitutes workflow refs before save
imported = client.create_agent({
    "name": "Imported",
    "agent_definition": exported,
    "entity_remap": entity_remap,
})
# `imported["import_warnings"]` lists any items that couldn't be applied.
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

# Cancel an in-flight or queued run. `delete_agent_run()` is the same
# operation on the same endpoint, returning a typed model instead of a dict.
client.cancel_agent_run("run_id")
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
# Discover which files (if any) the agent expects before staging uploads
refs = client.get_agent_attachment_references("agent_id")
# refs["requires_uploads"] -> bool; refs["agent"] lists the exact_names /
# indexes_max / patterns a run-time upload batch must satisfy.

upload = client.upload_agent_input("agent_id", file=b"data", file_name="input.pdf")
status = client.get_agent_input_upload_status("agent_id", upload["upload_id"])
```

### Agent run attachments

```python
# Download a file emitted by a step in an agent run. attachment_id is the
# URL-safe-base64 storage_key surfaced in run output manifests / webhooks.
response = client.download_agent_run_attachment("run_id", "attachment_id")  # raw httpx.Response
with response:
    for chunk in response.iter_bytes():
        ...  # write to disk
```

### Agent AI assistant

```python
steps = client.generate_agent_steps("agent_id", {"user_input": "Build a RAG pipeline"})
config = client.generate_step_config("agent_id", {"step_type": "llm", "user_input": "..."})

# Conversation history — step_type is required by the API
history = client.get_agent_ai_conversation_history("agent_id", step_type="llm")
client.mark_agent_ai_suggestion("agent_id", "conversation_id", {"accepted": True})
```

### Agent evaluations

```python
# CRUD
criteria_list = client.list_evaluation_criteria("agent_id", page=1, limit=50)
# page/limit only take effect with api_version="2026-07-27" or later; the legacy
# response is unpaginated. list_evaluation_criteria_page() returns the same items
# plus a "pagination" key when opted in.
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

Indexing status of a source's content, keyed by the `content_version_id` the
upload methods return:

```python
failed = client.list_source_contents("source_id", status="failed")
batch = client.list_source_contents(
    "source_id", content_version_ids=["cv_1", "cv_2"]
)
one = client.get_source_content_status("source_id", "cv_1")
```

### Cloud drives

```python
providers = client.list_cloud_drive_providers()
drives = client.list_cloud_drives()
drive = client.get_cloud_drive("connection_id")
client.update_cloud_drive("connection_id", {"name": "Contracts"})

# Which agents depend on it, and which files it skipped and why
agents = client.get_agents_using_cloud_drive("connection_id")
skipped = client.list_cloud_drive_rejections("connection_id", limit=20)

client.disconnect_cloud_drive("connection_id")  # keeps the connection
client.delete_cloud_drive("connection_id")
```

### File uploads

Upload a file to a source (max 200 MiB):

```python
upload = client.upload_file_to_source(
    "source_connection_id",
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
    "source_connection_content_version",
    file="./updated.pdf",
    metadata={"revision": 2},
)
```

Replace a content version with inline text:

```python
client.replace_content_with_inline_text("source_connection_content_version", {
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
detail = client.get_content_detail("source_connection_content_version")
embeddings = client.list_content_embeddings("source_connection_content_version")
client.delete_content("source_connection_content_version")
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

### Agent email triggers

```python
# Configure an EMAIL_RECEIVED trigger; omitted fields are left unchanged
config = client.set_email_trigger_config(
    "agent_id",
    "trigger_id",
    {
        "alias": "support",
        "allowed_senders": ["example.com", "ops@partner.com"],
        "ignore_auto_generated": True,   # drop auto-replies to prevent loops
        "require_sender_auth": True,     # require SPF or DMARC
        "queue_on_quota": False,         # park over-rate mail instead of failing
    },
)
print(config["email_addresses"])
```

### Agent email governance

```python
# Recipients who opted out of this account's agent emails
opt_outs = client.list_agent_email_optouts(agent_id="agent_id", limit=50)
client.remove_agent_email_optout("optout_id")  # opt them back in

# Blocked inbound senders (owner/admin only)
blocked = client.list_blocked_email_senders(limit=50)
client.block_email_sender({"sender_email": "spam.example.com", "match_type": "domain"})
client.unblock_email_sender("blocked_id")

# Auto-block on a governance BLOCK: "disabled" | "input" | "input_and_output"
client.set_auto_block_mode({"mode": "input_and_output"})

# Inbound mail discarded before running an agent
rejections = client.list_inbound_email_rejections(agent_id="agent_id")

# Account-wide overload circuit breaker
status = client.get_inbound_email_status()  # {"paused": ..., "queued_backlog": ...}
client.cancel_queued_email_runs()  # fail all QUEUED (over-quota parked) runs
client.resume_inbound_email()      # one-shot; re-arms if still overloaded
```

### Email domains

Send and receive agent email on your own domain instead of the shared
`agent.seclai.com`. Requires a user-bound credential; mutations require an
account owner/admin.

```python
listing = client.list_email_domains()

vanity = client.add_email_domain({"kind": "vanity", "value": "acme"})
custom = client.add_email_domain(
    {"kind": "custom", "value": "agent.mycompany.com", "delegated": True}
)

# Publish custom["dns_records"], then check without waiting for the sweep
client.verify_email_domain(custom["id"])

client.set_primary_email_domain(custom["id"])
client.use_shared_email_domain()  # revert; domains stay configured & verified

client.send_email_domain_test_email(custom["id"])  # always to the account owner
dmarc = client.get_dmarc_summary(custom["id"], days=30, top_sources=10)

removed = client.remove_email_domain(custom["id"])
print(removed.get("cleanup_note"))  # set when the domain was Seclai-managed
```

### Models

```python
# Media-generation quality tiers (fast/balanced/thorough) and what each resolves to
tiers = client.get_generation_tiers()

# Embedding and reranker models, with their pricing
embedders = client.list_embedding_models()["models"]
rerankers = client.list_reranker_models()["models"]

alerts = client.list_model_alerts()
client.mark_model_alert_read("alert_id")
client.mark_all_model_alerts_read()
unread = client.get_unread_model_alert_count()
recs = client.get_model_recommendations("model_id")

# Model playground experiments
experiment = client.create_experiment({"model_ids": ["model_id"], "prompt": "..."})
experiments = client.list_experiments()
detail = client.get_experiment("experiment_id")
client.cancel_experiment("experiment_id")
client.delete_experiment("experiment_id")  # soft-delete, preserves audit history
```

### Search

```python
results = client.search(query="quarterly report")
filtered = client.search(query="my agent", entity_type="agent", limit=5)
```

### Documentation search

Results are global (not account-scoped); each carries a `doc_slug` plus an
optional `anchor` for building a `https://seclai.com/docs/<doc_slug>[#<anchor>]` link.

```python
hits = client.search_docs("email triggers")                       # fast keyword match
deep = client.search_docs("how do I stop auto-reply loops",
                          mode="semantic", limit=5)               # adds a highlight
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

List methods take the paging arguments their endpoint declares: most take `page` and `limit`, some take `limit` and `offset`, some take `limit` alone, and listings that are always returned whole take none. Each method's signature says which. For auto-pagination across all pages, use the `paginate` helper. It stops after a page that is short or empty, and when the response says there is no next page or its `total` has been reached. A page longer than `limit` also ends it, unless the response says more exist. A page identical to the one before it is not yielded: `paginate` raises `SeclaiError` if that page reports more items — usually the endpoint pages by `offset`, so pass `param_style="offset"` — and otherwise stops:

```python
# Sync — yields items one by one (generator)
for agent in client.paginate("GET", "/agents"):
    print(agent["name"])

# With a per-resource items key; `data` is read first, so this works on
# either response shape
for config in client.paginate("GET", "/alerts/configs", items_key="configs"):
    print(config["id"])

# Endpoints that declare `offset` rather than `page`
for alert in client.paginate("GET", "/models/alerts", items_key="alerts",
                             param_style="offset"):
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
