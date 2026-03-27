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

from .auth import (
    DEFAULT_SSO_CLIENT_ID,
    DEFAULT_SSO_DOMAIN,
    DEFAULT_SSO_REGION,
    SsoCacheEntry,
    SsoProfile,
)
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

__all__ = [
    "AgentRunStreamRequest",
    "AsyncSeclai",
    "DEFAULT_SSO_CLIENT_ID",
    "DEFAULT_SSO_DOMAIN",
    "DEFAULT_SSO_REGION",
    "JSONValue",
    "Seclai",
    "SeclaiAPIStatusError",
    "SeclaiAPIValidationError",
    "SeclaiConfigurationError",
    "SeclaiError",
    "SeclaiStreamingError",
    "SsoProfile",
    "SsoCacheEntry",
]
