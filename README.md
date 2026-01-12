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
sources = client.request("GET", "/api/sources/")
print(sources)
```

### Async client

```python
import asyncio

from seclai import AsyncSeclai


async def main() -> None:
	async with AsyncSeclai(api_key="...") as client:
		sources = await client.request("GET", "/api/sources/")
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

### List sources

```python
from seclai import Seclai

client = Seclai(api_key="...")

sources = client.list_sources(page=1, limit=20)
print(sources)
```

### Upload a file to a source

You can upload either a filesystem path or bytes.

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
