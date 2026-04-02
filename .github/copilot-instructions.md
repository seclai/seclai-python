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

## Quality gates (must pass to report completion)

- **ALL tests must pass with ZERO failures. No exceptions.** CI/CD runs the full test suite on every PR. A test failure blocks the build.
- **ALL lint checks (including mypy) must pass with ZERO errors.** Run `make lint` — all files, not just ones you modified.
- **Do not dismiss test or lint failures as pre-existing or unrelated.** The `main` branch CI/CD is green. Any failure on a feature branch was caused by changes on that branch.
- **CRITICAL — NEVER INVESTIGATE ERROR ORIGIN OR BLAME**: When a lint, type-check, or test error appears, **fix it immediately**. Do NOT run `git diff`, `git log`, `git show`, `git blame`, or any other command to determine whether the error is "pre-existing" or "from our changes". There is no scenario where knowing the origin of an error changes what you must do: **fix it**.
- **CRITICAL — NEVER PIPE TEST OR LINT OUTPUT**: Do not append `| tail`, `| head`, `| grep`, or any pipe to `pytest`, `make lint`, `make test`, or similar commands. Piping hides errors. Use pytest flags like `--tb=short -q` to reduce verbosity — never pipe.

## Key Rules

- Always run `poetry run black .` after making changes — CI will fail if formatting differs.
- When fixing a type issue, remove the corresponding `# type: ignore` comment or mypy will error on the unused suppression.
- Do NOT edit files under `seclai/_generated/` — they are auto-generated from the OpenAPI spec.
- The OpenAPI spec at `openapi/seclai.openapi.json` is shared identically with `seclai-go`. Changes must be synced to both repos.
- Use the existing virtualenv (`poetry run ...`); do not create or reconfigure Python environments.
- **CRITICAL — USE EXISTING VIRTUAL ENV**: The workspace Python virtual environment is already set up. Reuse with `poetry run ...`; do **not** create, activate, or reconfigure another environment unless the user explicitly asks.
- **CRITICAL — NEVER CALL PYTHON ENVIRONMENT TOOLS**: Do not call `configure_python_environment`, `activate_python_environment_tools`, or any similar environment-management tool unless the user explicitly asks.
- Do not run ad-hoc Python snippets; add tests instead.

## Git rules

- **NEVER use `git stash`.** Use `git diff`, `git log`, or `git show` instead.
- Do not run `git checkout` to switch branches, `git reset`, or any other destructive git operation without explicit user approval.

## Editing rules

- Do not use CLI text tools (sed/awk). Use the editor-based patch tool.

## Self-correction rules

- **NEVER promise to "do better" without updating these instruction files.** If a recurring mistake is identified, edit this file with a concrete rule that prevents the mistake. Do that FIRST, then continue work.

## Architecture Notes

- Auth modes: `api_key`, `bearer_static`, `bearer_provider`, `sso`.
- `_build_default_headers()` only sets static auth; dynamic modes (`bearer_provider`, `sso`) are resolved per-request in `_merge_request_headers` / `_merge_request_headers_async`.
- Typed wrapper methods use `_sync_generated_client()` / `_async_generated_client()` which return a `GeneratedClient` with its own internal `httpx.Client` (separate from the SDK's `self._client`).
- In tests, to mock typed methods you must wire the mock transport into the generated client via `gc.set_httpx_client(httpx.Client(transport=transport, base_url=..., headers=dict(gc._headers)))`.
