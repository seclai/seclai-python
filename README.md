# Seclai Python SDK

This is the official Seclai Python SDK.

## Install

```bash
pip3 install seclai
```

## Quickstart

### Authentication

Provide your API key either:

- explicitly: `Seclai(api_key="...")`, or
- via environment variable: `SECLAI_API_KEY`

### Sync client

```python
from seclai import Seclai

client = Seclai(api_key="...")

# Low-level request (escape hatch)
sources = client.request("GET", "/sources/")
print(sources)
```

### Async client

```python
import asyncio

from seclai import AsyncSeclai


async def main() -> None:
	async with AsyncSeclai(api_key="...") as client:
		sources = await client.request("GET", "/sources/")
		print(sources)


asyncio.run(main())
```

## Common examples

### Run an agent

```python
from seclai import Seclai
from seclai._generated.models.agent_run_request import AgentRunRequest

client = Seclai(api_key="...")

run = client.run_agent(
	"11111111-1111-4111-8111-111111111111",
	body=AgentRunRequest(
		input_="Hello from the Seclai Python SDK!",
		metadata={
            "app": "My App"
        },
	),
)

print(run)
```

### Run an agent with SSE streaming (wait for final result)

This helper returns when the stream emits the final `done` event. It raises if the stream ends early or `timeout` is reached.

```python
from seclai import Seclai

client = Seclai(api_key="...")

run = client.run_streaming_agent_and_wait(
	"11111111-1111-4111-8111-111111111111",
	body={
		"input": "Hello from streaming",
		"metadata": {"app": "My App"},
	},
	timeout=60.0,
)

print(run)
```

Async:

```python
import asyncio

from seclai import AsyncSeclai


async def main() -> None:
	async with AsyncSeclai(api_key="...") as client:
		run = await client.run_streaming_agent_and_wait(
			"11111111-1111-4111-8111-111111111111",
			body={"input": "Hello from streaming"},
			timeout=60.0,
		)
		print(run)


asyncio.run(main())
```

### Get agent run details

Get details of a specific agent run, optionally including per-step outputs:

```python
from seclai import Seclai

client = Seclai(api_key="...")

# Basic details
run = client.get_agent_run(
	"11111111-1111-4111-8111-111111111111",
	"22222222-2222-4222-8222-222222222222",
)
print(run)

# Include per-step outputs with timing, durations, and credits
run = client.get_agent_run(
	"11111111-1111-4111-8111-111111111111",
	"22222222-2222-4222-8222-222222222222",
	include_step_outputs=True,
)
print(run)
```

### List sources

```python
from seclai import Seclai

client = Seclai(api_key="...")

sources = client.list_sources(page=1, limit=20)
print(sources)
```

### Upload a file to a source

You can upload either a filesystem path or bytes.

**Max file size:** 200 MiB.

**Supported MIME types:**
- `application/epub+zip`
- `application/json`
- `application/msword`
- `application/pdf`
- `application/vnd.ms-excel`
- `application/vnd.ms-outlook`
- `application/vnd.ms-powerpoint`
- `application/vnd.openxmlformats-officedocument.presentationml.presentation`
- `application/vnd.openxmlformats-officedocument.spreadsheetml.sheet`
- `application/vnd.openxmlformats-officedocument.wordprocessingml.document`
- `application/xml`
- `application/zip`
- `audio/flac`, `audio/mp4`, `audio/mpeg`, `audio/ogg`, `audio/wav`
- `image/bmp`, `image/gif`, `image/jpeg`, `image/png`, `image/tiff`, `image/webp`
- `text/csv`, `text/html`, `text/markdown`, `text/x-markdown`, `text/plain`, `text/xml`
- `video/mp4`, `video/quicktime`, `video/x-msvideo`

If the upload is sent as `application/octet-stream`, the server attempts to infer the type from the file extension.

```python
from seclai import Seclai

client = Seclai(api_key="...")

# Upload from path
resp = client.upload_file_to_source(
	"22222222-2222-4222-8222-222222222222",
	file="./document.pdf",
	title="Example document",
)
print(resp)
```

```python
from seclai import Seclai

client = Seclai(api_key="...")

# Upload from bytes
resp = client.upload_file_to_source(
	"22222222-2222-4222-8222-222222222222",
	file=b"hello world",
	file_name="hello.txt",
	mime_type="text/plain",
)
print(resp)
```

## Error handling

Typed convenience methods raise exceptions for non-success responses.

```python
from seclai import Seclai, SeclaiAPIStatusError

client = Seclai(api_key="...")

try:
	sources = client.list_sources()
except SeclaiAPIStatusError as e:
	print("Request failed:")
	print("status:", e.status_code)
	print("method:", e.method)
	print("url:", e.url)
	print("body:", e.response_text)
	raise
```

## Configuration

### Timeouts and headers

```python
from seclai import Seclai

client = Seclai(
	api_key="...",
	timeout=30.0,
	default_headers={"x-my-app": "my-service"},
)
```

## Development

### Base URL

Set `SECLAI_API_URL` to point at a different API host (e.g., staging):

```bash
export SECLAI_API_URL="https://example.invalid"
```

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

## API documentation

Online API documentation (latest):

https://seclai.github.io/seclai-python/latest/

Generate HTML docs into `build/docs/`:

```bash
make docs
```

### OpenAPI spec & regenerating the client

Copy the OpenAPI JSON file into `openapi/seclai.openapi.json`, then run:

```bash
make generate
```

## Reporting issues

If you hit a bug or have a feature request, please open an issue and include:

- what you were trying to do
- a minimal repro snippet (if possible)
- the exception / traceback
- your environment (Python version, OS)

## Contributing

Contributions are welcome.

- Keep changes focused and add/adjust tests where appropriate.
- Run `make lint` and `make test` before opening a PR.
