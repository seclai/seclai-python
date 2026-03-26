"""Seclai Python SDK.

Provides synchronous and asynchronous clients for the Seclai API.

Quick start::

    from seclai import Seclai

    client = Seclai(api_key="...")
    agents = client.list_agents()

All public symbols are re-exported from this package:

- :class:`Seclai` — synchronous client
- :class:`AsyncSeclai` — asynchronous client
- :class:`SeclaiError` — base exception
- :class:`SeclaiConfigurationError` — configuration errors
- :class:`SeclaiAPIStatusError` — non-2xx HTTP responses
- :class:`SeclaiAPIValidationError` — HTTP 422 validation errors
- :class:`SeclaiStreamingError` — SSE stream errors
- :class:`AgentRunStreamRequest` — typed request body for streaming runs
- :data:`JSONValue` — recursive JSON type alias
"""

from .seclai import (
    AgentRunStreamRequest,
    AsyncSeclai,
    JSONValue,
    Seclai,
    SeclaiAPIStatusError,
    SeclaiAPIValidationError,
    SeclaiConfigurationError,
    SeclaiError,
    SeclaiStreamingError,
)

from .auth import (
    SsoProfile,
    SsoCacheEntry,
    is_token_valid,
    load_sso_profile,
    read_sso_cache,
    write_sso_cache,
    delete_sso_cache,
    cache_file_name,
    resolve_config_dir,
    refresh_token_sync,
    refresh_token_async,
)

__all__ = [
    "AgentRunStreamRequest",
    "AsyncSeclai",
    "JSONValue",
    "Seclai",
    "SeclaiAPIStatusError",
    "SeclaiAPIValidationError",
    "SeclaiConfigurationError",
    "SeclaiError",
    "SeclaiStreamingError",
    "SsoProfile",
    "SsoCacheEntry",
    "is_token_valid",
    "load_sso_profile",
    "read_sso_cache",
    "write_sso_cache",
    "delete_sso_cache",
    "cache_file_name",
    "resolve_config_dir",
    "refresh_token_sync",
    "refresh_token_async",
]
