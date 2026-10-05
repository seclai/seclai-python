# Changelog

## [1.7.1] - 2026-10-05

### Changed

- Raise `SeclaiError` from every version-gated list method when a 200 response is not a list: an error-shaped object, text, `null` or an empty body. Most of these methods returned such a body unchanged, and `list_evaluation_criteria()` and `list_run_evaluation_results()` returned `[]` for an empty one
- Read `{"data": null}` as an empty list in every version-gated list method: a list method returns `[]` and a dict method holds `[]` under its documented key. Most of them returned `{"data": None}` unchanged
- Return `{key: [...]}`, under the method's documented key, from a dict-returning version-gated list method that is answered with a bare array. It returned the array, except from `list_evaluation_criteria_page()` and `list_run_evaluation_results_page()`, which already wrapped it
- Change when `paginate()` stops. It now also stops after a page that reports `pagination.has_next` as false or that reaches the `total` the body reports, so a walk whose last page is full can make one request fewer, and after a page holding more than `limit` items unless the body says more exist. A page identical to the one before it is not yielded: the walk raises `SeclaiError` if that page reports more items, and ends if it reports no paging information. Two consecutive pages that are legitimately identical are treated the same way
- Raise `ValueError` from `paginate()` when `limit` is not a positive integer, before any request

### Fixed

- Return the list from `get_agent_callers()`, `list_inbound_email_rejections()`, `list_solution_conversations()`, `list_governance_ai_conversations()`, `list_models()`, `list_memory_bank_templates()` and `get_agents_using_memory_bank()` when `api_version` is `2026-07-27` or later. They returned the `{data, pagination}` object, four of them from a method annotated `list`
- Keep the items under the documented key when `api_version` is `2026-07-27` or later, in `list_knowledge_bases()`, `list_memory_banks()`, `list_agent_email_optouts()`, `list_blocked_email_senders()`, `set_auto_block_mode()`, `list_organization_alert_preferences()`, `list_email_domains()`, `list_alert_configs()`, `list_model_alerts()`, `list_experiments()`, `get_generation_tiers()`, `list_embedding_models()` and `list_reranker_models()`. The items were only under `data`, so `result["knowledge_bases"]` raised `KeyError`. `data` and `pagination` are still present
- Fill the flat `total`, `page` and `limit` a method documents from `pagination` when `api_version` is `2026-07-27` or later. They were absent from the four evaluation listings, the knowledge-base and memory-bank listings and every listing with a `total`
- Declare `attrs` as a runtime dependency. The generated client imports it, so `import seclai` failed with `ModuleNotFoundError` unless another installed package happened to provide `attrs`
- End `paginate()` on an endpoint that ignores `page` and `limit`. `client.paginate("GET", "/alerts/configs", items_key="configs")` never ended on the default API version once an account had 50 alert configs
- Raise `SeclaiError` from `paginate()` when an endpoint that pages by `offset` is walked with the default `param_style="page"` on the default API version. Every request returned the first page, so the walk never ended
- Send one `authorization` and one `x-account-id` on the first typed-method call, such as `list_sources()` or `run_agent()`, when the client uses a bearer-token provider or an SSO profile and `default_headers` spells either header in another case. Both values were sent on that call; later calls sent only the resolved credential, which is now the one sent every time
- Apply the unknown-version guard to a `Seclai-Version` in the default headers of a supplied `http_client`, at construction and on each request. This is a new rejection: a value this release was not built against was sent unchecked and now raises `SeclaiConfigurationError`, as the same value in `default_headers` does. `allow_unknown_api_version=True` permits any value
- Correct the documentation of `list_alert_configs()`: on the default API version it ignores `page` and `limit` and returns every configuration. The README said it paged

## [1.7.0] - 2026-10-05

_Documentation-only release: the `content_version_ids` guidance of `list_source_contents()` now says to keep a request to about 100 ids, since they travel in the query string._

## [1.6.0] - 2026-10-04

### Changed

- Sync the bundled OpenAPI spec, adding 10 paths and 18 schemas. The typed models gain the new response fields, including `attachments` on a run and on each step
- Move `LATEST_API_VERSION` to `2026-10-03`

### Added

- Add `list_cloud_drives()`, `get_cloud_drive()`, `update_cloud_drive()`, `disconnect_cloud_drive()`, `delete_cloud_drive()`, `list_cloud_drive_providers()`, `get_agents_using_cloud_drive()` and `list_cloud_drive_rejections()` for cloud-drive connections. The list methods return the items on either response shape
- Add `list_source_contents()` and `get_source_content_status()` to read the indexing status of a source's content, keyed by the `content_version_id` the upload methods return
- Add `list_embedding_models()` and `list_reranker_models()`, with the pricing and defaults that sit beside each list
- Add `ApiVersion` members for `2026-08-03`, `2026-08-21`, `2026-09-28`, `2026-09-30` and `2026-10-03`, so each can be selected without `allow_unknown_api_version`
- Add a `param_style` argument to `paginate()` for endpoints that page by `offset` rather than `page`

### Fixed

- Read the body of an error response in the streaming methods. A 422 from `run_streaming_agent_and_wait()` escaped as `httpx.ResponseNotRead`, a 422 from `run_streaming_agent()` lost its field-level detail, and every streaming error had an empty `response_text`
- Raise `SeclaiAPIStatusError` on a 422 whose `detail` is a plain string, from every method including the typed ones and the uploads. Decoding it as field-level validation raised `ValueError` from inside the generated models
- Apply the unknown-version guard to a `Seclai-Version` passed in a per-request `headers` argument, on `request()` and the streaming methods. Any value was sent
- Replace a header case-insensitively when a per-request `headers` argument or the auth layer supplies one the client already set. Both spellings were sent
- Yield the items from `paginate()` when the endpoint answers with a bare array, or under `data` while a per-resource `items_key` was given. It yielded nothing in both cases, and now raises `SeclaiError` on a shape it cannot read
- Copy `default_headers` at construction. Mutating the mapping afterwards put an unvalidated `Seclai-Version` on the wire
- Reject an empty `Seclai-Version` in `default_headers`. It was read as absent, sent anyway, and suppressed `api_version`

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

- Validate the `Seclai-Version` that survives the header merge, and drop every differently-cased duplicate. Two spellings in `default_headers` previously bypassed the guard and put two values on the wire
- Validate a `Seclai-Version` supplied through `default_headers`, not just the `api_version` argument. `default_headers` is applied last so it wins, which left the unknown-version guard one header away from being bypassed
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

[1.7.1]: https://github.com/seclai/seclai-python/releases/tag/1.7.1
[1.7.0]: https://github.com/seclai/seclai-python/releases/tag/1.7.0
[1.6.0]: https://github.com/seclai/seclai-python/releases/tag/1.6.0
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
