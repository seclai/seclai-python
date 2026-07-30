# Changelog

## [1.5.0] - 2026-07-27

### Changed

- Document the version-gated top-level key on `list_alert_configs()`, `list_model_alerts()`, `list_experiments()` and `get_generation_tiers()`. All four flip from a per-resource key to the canonical `{data, pagination}` envelope once `api_version` is `2026-07-27` or later
- Note on `get_non_manual_evaluation_summary()` that `agent_id` scoping is part of the `2026-07-27` changeset. On the legacy baseline the API ignores it and returns the account-wide rollup, which is indistinguishable from a scoped result in the payload
- Accept either wire shape from `list_run_evaluation_results()`, and return the results rather than an envelope. It was annotated `dict` while the default API returns a bare array
- Stop sending `severity` from `list_alerts()`. `GET /alerts` declares no such filter, so it never filtered, and it becomes a 422 once `api_version` is `2026-07-27` or later. The argument is still accepted and ignored
- Accept either wire shape from `list_evaluation_criteria()`. The endpoint answers with a bare list by default and the canonical `{data, pagination}` envelope once opted in, so the client reads both and keeps returning a list
- Sync the bundled OpenAPI spec with the API fixes found while updating the SDKs: `agent_id` is now declared on the non-manual evaluation summary, and `page`/`limit` on the evaluation and alert-config listings

### Added

- Add the `ApiVersion` string enum plus `DEFAULT_API_VERSION` and `LATEST_API_VERSION`. An `api_version` this release was not built against raises `SeclaiConfigurationError`, since a newer version can reshape responses this client would mis-decode; pass `allow_unknown_api_version=True` to override
- Add `list_evaluation_criteria_page()` and `list_run_evaluation_results_page()` for the canonical `{data, pagination}` envelope, which those endpoints emit once `api_version` is `2026-07-27` or later
- Add an `api_version` client option, sent as the `Seclai-Version` header, opting into dated API changes released on or before that date. Omitted by default, so upgrading the SDK alone never changes response shapes
- Add `get_api_version()` and `update_api_version()` to read the version a request resolves to and to pin or clear the account's version. `update_api_version()` applies the same unknown-version guard as the client option, since the pin is account-wide and affects every header-less caller
- Add `unwrap_items()`, which reads a version-gated list response in either shape so a call site does not have to branch on the API version

### Fixed

- Raise `SeclaiAPIValidationError` rather than a bare `SeclaiAPIStatusError` on a 422 from any method built on `request()` — most of the SDK. Only the generated-client path distinguished the two, so field-level validation detail was being discarded everywhere else
- Send `step_type` from `get_agent_ai_conversation_history()`, along with `step_id`, `limit` and `offset`. The API marks `step_type` required and the method had no way to supply it, so every call answered 422. Omitting it now raises `ValueError` naming the argument instead of deferring to a 422 naming the wire parameter
- Raise from `unwrap_items()` on a list response in a shape the client cannot read, rather than returning `[]`. Reporting "no results" for an unrecognised envelope is indistinguishable from a genuinely empty page
- Floor the `list_model_alerts()` page translation at zero. `offset` is declared `minimum: 0`, so `page=0` turned a previously-ignored parameter into a hard 422
- Paginate `list_model_alerts()` with the `offset` the endpoint declares instead of `page`, which it does not accept — every page after the first returned page 1
- Request `GET /sources` rather than `GET /sources/`. The trailing-slash form is no longer declared by the API
- Send `q` rather than `query` from `search()`. The API requires `q`, so every search call had been failing validation since 1.1.0
- Cancel a run with `DELETE /agents/runs/{run_id}`. `cancel_agent_run()` posted to `/agents/runs/{run_id}/cancel`, a path the API has never exposed, so cancelling always failed

## [1.4.0] - 2026-07-25

### Changed

- Sync the bundled OpenAPI spec, adding 22 paths and 22 schemas

### Added

- Add `get_me()` returning the authenticated user's account id and organization memberships
- Add `disable_agent()`, `enable_agent()`, and `get_agent_callers()` to pause and resume an agent across every trigger path
- Add `set_email_trigger_config()` to set the alias, sender allowlist, and inbound-handling flags on an `EMAIL_RECEIVED` trigger
- Add agent-email opt-out methods `list_agent_email_optouts()` and `remove_agent_email_optout()`
- Add inbound sender blocklist methods `list_blocked_email_senders()`, `block_email_sender()`, `unblock_email_sender()`, and `set_auto_block_mode()`
- Add inbound-email observability methods `list_inbound_email_rejections()`, `get_inbound_email_status()`, `cancel_queued_email_runs()`, and `resume_inbound_email()`
- Add email domain management: `list_email_domains()`, `add_email_domain()`, `remove_email_domain()`, `verify_email_domain()`, `set_primary_email_domain()`, `use_shared_email_domain()`, `send_email_domain_test_email()`, and `get_dmarc_summary()`
- Add `get_generation_tiers()` mapping each media-generation modality and tier to its model and cost
- Add `search_docs()` for keyword or semantic search over the Seclai documentation

## [1.3.0] - 2026-06-05

### Added

- Add `get_agent_attachment_references()` to read an agent's static attachment-reference contract before staging uploads ([#9](https://github.com/seclai/seclai-python/pull/9))
- Add `download_agent_run_attachment()` for a file emitted by a run step ([#9](https://github.com/seclai/seclai-python/pull/9))
- Add `delete_experiment()` to soft-delete a model playground experiment ([#9](https://github.com/seclai/seclai-python/pull/9))

## [1.2.0] - 2026-05-22

### Added

- Add `preview_import_agent()` to dry-run an agent definition import and surface unresolved entity refs ([#8](https://github.com/seclai/seclai-python/pull/8))

## [1.1.4] - 2026-04-24

### Added

- Add `list_models()` and `get_model()` for the model catalog ([#7](https://github.com/seclai/seclai-python/pull/7))
- Add model playground methods `list_experiments()`, `create_experiment()`, `get_experiment()`, and `cancel_experiment()` ([#7](https://github.com/seclai/seclai-python/pull/7))

## [1.1.3] - 2026-04-02

### Added

- Add `export_agent()` returning a portable JSON snapshot of an agent definition ([#6](https://github.com/seclai/seclai-python/pull/6))

## [1.1.2] - 2026-03-27

### Changed

- Default the SSO domain, client id, and region so a profile only needs `sso_account_id` ([#5](https://github.com/seclai/seclai-python/pull/5))

### Added

- Add `GET /me` to the bundled OpenAPI spec; the corresponding `get_me()` client method arrived in 1.4.0 ([#5](https://github.com/seclai/seclai-python/pull/5))

## [1.1.1] - 2026-03-26

### Added

- Add OAuth SSO authentication with `~/.seclai/config` profiles, an on-disk token cache, and automatic refresh ([#4](https://github.com/seclai/seclai-python/pull/4))
- Add an `account_id` option, sent as the `X-Account-Id` header, to switch organization account context ([#4](https://github.com/seclai/seclai-python/pull/4))

## [1.1.0] - 2026-03-23

### Added

- Expand endpoint coverage to knowledge bases, memory banks, sources, source exports, embedding migrations, content, solutions, alerts, governance, evaluations, and the AI assistants ([#3](https://github.com/seclai/seclai-python/pull/3))
- Add `run_streaming_agent()`, an async generator yielding every SSE event of a run ([#3](https://github.com/seclai/seclai-python/pull/3))
- Add `run_agent_and_poll()` for environments where SSE is impractical ([#3](https://github.com/seclai/seclai-python/pull/3))
- Add `paginate()` to iterate a paginated endpoint automatically ([#3](https://github.com/seclai/seclai-python/pull/3))
- Add `search()` across all resource types in an account ([#3](https://github.com/seclai/seclai-python/pull/3))

## [1.0.6] - 2026-01-30

### Added

- Add `upload_file_to_content()` to replace existing content with a file upload ([`e0d353a`](https://github.com/seclai/seclai-python/commit/e0d353a))
- Add a `metadata` argument to the upload methods ([`e0d353a`](https://github.com/seclai/seclai-python/commit/e0d353a))

### Fixed

- Correct type annotations on the upload and content methods ([`206e020`](https://github.com/seclai/seclai-python/commit/206e020))

## [1.0.5] - 2026-01-27

### Changed

- Accept a run id alone in `get_agent_run()` and `delete_agent_run()`; the agent id is no longer required ([`51926b8`](https://github.com/seclai/seclai-python/commit/51926b8))

## [1.0.4] - 2026-01-27

### Added

- Add an `include_step_outputs` argument to `get_agent_run()` ([`d3b4501`](https://github.com/seclai/seclai-python/commit/d3b4501))

## [1.0.3] - 2026-01-27

### Added

- Add `run_streaming_agent_and_wait()` to block until a streaming run completes ([`f7850df`](https://github.com/seclai/seclai-python/commit/f7850df))

### Fixed

- Drop the `/api` prefix from request paths so they match the deployed API ([`4a33852`](https://github.com/seclai/seclai-python/commit/4a33852))
- Correct the file upload endpoint ([`ea50e25`](https://github.com/seclai/seclai-python/commit/ea50e25))

## [1.0.2] - 2026-01-12

### Removed

- Remove build artifacts that had been committed to the repository ([`d946d55`](https://github.com/seclai/seclai-python/commit/d946d55))

## [1.0.1] - 2026-01-12

### Added

- Add a documentation homepage link to the package metadata ([`cc8e28f`](https://github.com/seclai/seclai-python/commit/cc8e28f))

## [1.0.0] - 2026-01-12

_Stable release. Packaging, CI, and documentation deployment only; no API changes since 0.0.1._

## [0.0.1] - 2026-01-12

_Initial release._

[1.5.0]: https://github.com/seclai/seclai-python/releases/tag/1.5.0
[1.4.0]: https://github.com/seclai/seclai-python/releases/tag/1.4.0
[1.3.0]: https://github.com/seclai/seclai-python/releases/tag/1.3.0
[1.2.0]: https://github.com/seclai/seclai-python/releases/tag/1.2.0
[1.1.4]: https://github.com/seclai/seclai-python/releases/tag/1.1.4
[1.1.3]: https://github.com/seclai/seclai-python/releases/tag/1.1.3
[1.1.2]: https://github.com/seclai/seclai-python/releases/tag/1.1.2
[1.1.1]: https://github.com/seclai/seclai-python/releases/tag/1.1.1
[1.1.0]: https://github.com/seclai/seclai-python/releases/tag/1.1.0
[1.0.6]: https://github.com/seclai/seclai-python/releases/tag/1.0.6
[1.0.5]: https://github.com/seclai/seclai-python/releases/tag/1.0.5
[1.0.4]: https://github.com/seclai/seclai-python/releases/tag/1.0.4
[1.0.3]: https://github.com/seclai/seclai-python/releases/tag/1.0.3
[1.0.2]: https://github.com/seclai/seclai-python/releases/tag/1.0.2
[1.0.1]: https://github.com/seclai/seclai-python/releases/tag/1.0.1
[1.0.0]: https://github.com/seclai/seclai-python/releases/tag/1.0.0
[0.0.1]: https://github.com/seclai/seclai-python/releases/tag/0.0.1
