# Copilot Instructions — seclai-python

## Build & Lint Pipeline

Run the full CI check before committing:

```sh
make lint   # ruff check + black + mypy
make test   # pytest
```

Individual commands:

- **Formatter**: `poetry run black .` — CI enforces formatting; always run before committing
- **Linter**: `poetry run ruff check --fix .`
- **Type checker**: `poetry run mypy .` — strict mode with `warn_unused_ignores`
- **Tests**: `poetry run pytest tests/ -q`

## Key Rules

- Always run `poetry run black .` after making changes — CI will fail if formatting differs.
- When fixing a type issue, remove the corresponding `# type: ignore` comment or mypy will error on the unused suppression.
- Do NOT edit files under `seclai/_generated/` — they are auto-generated from the OpenAPI spec.
- The OpenAPI spec at `openapi/seclai.openapi.json` is shared identically with `seclai-go`. Changes must be synced to both repos.
- Use the existing virtualenv (`poetry run ...`); do not create or reconfigure Python environments.

## Architecture Notes

- Auth modes: `api_key`, `bearer_static`, `bearer_provider`, `sso`.
- `_build_default_headers()` only sets static auth; dynamic modes (`bearer_provider`, `sso`) are resolved per-request in `_merge_request_headers` / `_merge_request_headers_async`.
- Typed wrapper methods use `_sync_generated_client()` / `_async_generated_client()` which return a `GeneratedClient` with its own internal `httpx.Client` (separate from the SDK's `self._client`).
- In tests, to mock typed methods you must wire the mock transport into the generated client via `gc.set_httpx_client(httpx.Client(transport=transport, base_url=..., headers=dict(gc._headers)))`.
