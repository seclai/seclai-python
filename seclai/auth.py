"""SSO credential resolution: config file, token caching, and automatic refresh.

This module implements the credential provider chain used by :class:`Seclai`
and :class:`AsyncSeclai`.

Internal — not part of the public API surface.
"""

from __future__ import annotations

import asyncio
import configparser
import hashlib
import json
import os
import tempfile
import threading
from collections.abc import Awaitable, Callable
from dataclasses import dataclass, field
from datetime import UTC, datetime, timedelta
from pathlib import Path
from typing import Any

import httpx

_DEFAULT_CONFIG_DIR = ".seclai"
_SSO_CACHE_DIR = "sso/cache"
_CONFIG_FILE = "config"
_EXPIRY_BUFFER_SECONDS = 30

_SSO_EXPIRED_MSG = "SSO token expired. Run `seclai auth login` to re-authenticate."


# ── Types ─────────────────────────────────────────────────────────────────────


@dataclass(frozen=True, slots=True)
class SsoProfile:
    """Resolved SSO profile settings from the config file.

    Attributes:
        sso_account_id: AWS Cognito account ID.
        sso_region: AWS region for the Cognito user pool.
        sso_client_id: Cognito app client ID.
        sso_domain: Cognito domain (e.g. ``"auth.example.com"``).
    """

    sso_account_id: str
    sso_region: str
    sso_client_id: str
    sso_domain: str


@dataclass(frozen=True, slots=True)
class SsoCacheEntry:
    """Contents of a single SSO cache file.

    Attributes:
        access_token: JWT access token.
        refresh_token: Refresh token for obtaining new access tokens.
        id_token: OIDC ID token (optional).
        expires_at: ISO-8601 expiry timestamp for the access token.
        client_id: Cognito app client ID.
        region: AWS region.
        cognito_domain: Cognito domain.
    """

    access_token: str
    refresh_token: str | None
    id_token: str | None
    expires_at: str  # ISO-8601
    client_id: str
    region: str
    cognito_domain: str

    def to_dict(self) -> dict[str, Any]:
        """Serialize to a JSON-compatible dict with camelCase keys."""
        d: dict[str, Any] = {
            "accessToken": self.access_token,
            "expiresAt": self.expires_at,
            "clientId": self.client_id,
            "region": self.region,
            "cognitoDomain": self.cognito_domain,
        }
        if self.refresh_token is not None:
            d["refreshToken"] = self.refresh_token
        if self.id_token is not None:
            d["idToken"] = self.id_token
        return d

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> SsoCacheEntry:
        """Deserialize from a JSON dict with camelCase keys."""
        return cls(
            access_token=data["accessToken"],
            refresh_token=data.get("refreshToken"),
            id_token=data.get("idToken"),
            expires_at=data["expiresAt"],
            client_id=data["clientId"],
            region=data["region"],
            cognito_domain=data["cognitoDomain"],
        )


@dataclass(slots=True)
class AuthState:
    """Resolved authentication state used throughout the client lifecycle.

    Attributes:
        mode: Auth mode — one of ``"api_key"``, ``"bearer_static"``,
            ``"bearer_provider"``, or ``"sso"``.
        api_key: API key value (for ``api_key`` mode).
        api_key_header: Header name for API key auth.
        access_token: Static bearer token (for ``bearer_static`` mode).
        access_token_provider: Callable returning a token string or awaitable
            (for ``bearer_provider`` mode).
        account_id: Account ID sent as ``X-Account-Id`` header.
        sso_profile: Resolved SSO profile (for ``sso`` mode).
        config_dir: Config directory path (for SSO cache lookup).
        auto_refresh: Whether to auto-refresh expired SSO tokens.
    """

    mode: str  # "api_key" | "bearer_static" | "bearer_provider" | "sso"
    api_key: str | None = None
    api_key_header: str = "x-api-key"
    access_token: str | None = None
    access_token_provider: Callable[[], str | Awaitable[str]] | None = None
    account_id: str | None = None
    sso_profile: SsoProfile | None = None
    config_dir: str | None = None
    auto_refresh: bool = True
    _sync_refresh_lock: threading.Lock = field(default_factory=threading.Lock, repr=False)
    _async_refresh_lock: asyncio.Lock = field(default_factory=asyncio.Lock, repr=False)


# ── Helpers ───────────────────────────────────────────────────────────────────


def cache_file_name(domain: str, client_id: str) -> str:
    """Compute SHA-1 hex digest of ``domain|client_id`` for cache filename."""
    return hashlib.sha1(f"{domain}|{client_id}".encode()).hexdigest()


def resolve_config_dir(override: str | None = None) -> Path:
    """Resolve the config directory path."""
    if override:
        return Path(override)
    env_dir = os.getenv("SECLAI_CONFIG_DIR")
    if env_dir:
        return Path(env_dir)
    home = Path.home()
    return home / _DEFAULT_CONFIG_DIR


def parse_ini_config(config_path: Path) -> configparser.ConfigParser:
    """Read an INI config file with AWS-style ``[profile X]`` sections."""
    cp = configparser.ConfigParser()
    if config_path.exists():
        cp.read(str(config_path))
    return cp


def load_sso_profile(config_dir: Path, profile_name: str) -> SsoProfile | None:
    """Load and resolve an SSO profile from the config file.

    Non-default profiles inherit unset values from ``[default]``.
    """
    config_path = config_dir / _CONFIG_FILE
    if not config_path.exists():
        return None

    cp = parse_ini_config(config_path)

    default_section: dict[str, str] = {}
    if cp.has_section("default"):
        default_section = dict(cp.items("default"))

    if profile_name == "default":
        section = default_section
    else:
        section_name = f"profile {profile_name}"
        if not cp.has_section(section_name):
            return None
        section = {**default_section, **dict(cp.items(section_name))}

    sso_account_id = section.get("sso_account_id")
    sso_region = section.get("sso_region")
    sso_client_id = section.get("sso_client_id")
    sso_domain = section.get("sso_domain")

    if not all([sso_account_id, sso_region, sso_client_id, sso_domain]):
        return None

    return SsoProfile(
        sso_account_id=sso_account_id,  # type: ignore[arg-type]
        sso_region=sso_region,  # type: ignore[arg-type]
        sso_client_id=sso_client_id,  # type: ignore[arg-type]
        sso_domain=sso_domain,  # type: ignore[arg-type]
    )


# ── Cache I/O ─────────────────────────────────────────────────────────────────


def _sso_cache_path(config_dir: Path, profile: SsoProfile) -> Path:
    """Resolve the full path to a profile's SSO cache file."""
    hash_name = cache_file_name(profile.sso_domain, profile.sso_client_id)
    return config_dir / _SSO_CACHE_DIR / f"{hash_name}.json"


def read_sso_cache(config_dir: Path, profile: SsoProfile) -> SsoCacheEntry | None:
    """Read a cached SSO token from disk."""
    cache_path = _sso_cache_path(config_dir, profile)
    if not cache_path.exists():
        return None
    try:
        data = json.loads(cache_path.read_text())
        return SsoCacheEntry.from_dict(data)
    except (json.JSONDecodeError, KeyError, OSError):
        return None


def write_sso_cache(
    config_dir: Path, profile: SsoProfile, entry: SsoCacheEntry
) -> None:
    """Write a cached SSO token to disk atomically."""
    cache_dir = config_dir / _SSO_CACHE_DIR
    cache_dir.mkdir(parents=True, exist_ok=True)
    os.chmod(str(cache_dir), 0o700)

    hash_name = cache_file_name(profile.sso_domain, profile.sso_client_id)
    cache_path = cache_dir / f"{hash_name}.json"

    fd, tmp_path = tempfile.mkstemp(dir=str(cache_dir), suffix=".tmp")
    try:
        with os.fdopen(fd, "w") as f:
            json.dump(entry.to_dict(), f, indent=2)
        os.chmod(tmp_path, 0o600)
        os.replace(tmp_path, str(cache_path))
    except Exception:
        try:
            os.unlink(tmp_path)
        except OSError:
            pass
        raise


def delete_sso_cache(config_dir: Path, profile: SsoProfile) -> None:
    """Delete a cached SSO token file."""
    cache_path = _sso_cache_path(config_dir, profile)
    if cache_path.exists():
        cache_path.unlink()


# ── Token validation ──────────────────────────────────────────────────────────


def is_token_valid(entry: SsoCacheEntry) -> bool:
    """Check if a cached token is still valid (with 30s buffer)."""
    try:
        expires_at = datetime.fromisoformat(entry.expires_at.replace("Z", "+00:00"))
    except ValueError:
        return False
    now = datetime.now(UTC)
    return now + timedelta(seconds=_EXPIRY_BUFFER_SECONDS) < expires_at


# ── Token refresh helpers ───────────────────────────────────────────────────


def _build_refresh_request(
    profile: SsoProfile, refresh_token_value: str
) -> tuple[str, dict[str, str]]:
    """Build the token refresh URL and form body."""
    token_url = f"https://{profile.sso_domain}/oauth2/token"
    body = {
        "grant_type": "refresh_token",
        "client_id": profile.sso_client_id,
        "refresh_token": refresh_token_value,
    }
    return token_url, body


def _parse_refresh_response(
    data: dict[str, Any], profile: SsoProfile, refresh_token_value: str
) -> SsoCacheEntry:
    """Parse a Cognito token response into an SsoCacheEntry."""
    expires_at = (
        datetime.now(UTC) + timedelta(seconds=data["expires_in"])
    ).isoformat()

    return SsoCacheEntry(
        access_token=data["access_token"],
        refresh_token=data.get("refresh_token", refresh_token_value),
        id_token=data.get("id_token"),
        expires_at=expires_at,
        client_id=profile.sso_client_id,
        region=profile.sso_region,
        cognito_domain=profile.sso_domain,
    )


# ── Token refresh (sync) ─────────────────────────────────────────────────────


def refresh_token_sync(
    profile: SsoProfile,
    refresh_token_value: str,
    http_client: httpx.Client | None = None,
) -> SsoCacheEntry:
    """Refresh an access token using a Cognito ``refresh_token`` grant (sync).

    Args:
        profile: SSO profile with Cognito domain and client ID.
        refresh_token_value: The refresh token to exchange.
        http_client: Optional pre-configured HTTP client.

    Returns:
        A fresh :class:`SsoCacheEntry` with the new tokens.

    Raises:
        httpx.HTTPStatusError: If the Cognito token endpoint returns a non-2xx status.
    """
    token_url, body = _build_refresh_request(profile, refresh_token_value)

    client = http_client or httpx.Client()
    try:
        response = client.post(
            token_url,
            data=body,
            headers={"content-type": "application/x-www-form-urlencoded"},
        )
        response.raise_for_status()
    finally:
        if http_client is None:
            client.close()

    return _parse_refresh_response(response.json(), profile, refresh_token_value)


# ── Token refresh (async) ────────────────────────────────────────────────────


async def refresh_token_async(
    profile: SsoProfile,
    refresh_token_value: str,
    http_client: httpx.AsyncClient | None = None,
) -> SsoCacheEntry:
    """Refresh an access token using a Cognito ``refresh_token`` grant (async).

    Args:
        profile: SSO profile with Cognito domain and client ID.
        refresh_token_value: The refresh token to exchange.
        http_client: Optional pre-configured async HTTP client.

    Returns:
        A fresh :class:`SsoCacheEntry` with the new tokens.

    Raises:
        httpx.HTTPStatusError: If the Cognito token endpoint returns a non-2xx status.
    """
    token_url, body = _build_refresh_request(profile, refresh_token_value)

    client = http_client or httpx.AsyncClient()
    try:
        response = await client.post(
            token_url,
            data=body,
            headers={"content-type": "application/x-www-form-urlencoded"},
        )
        response.raise_for_status()
    finally:
        if http_client is None:
            await client.aclose()

    return _parse_refresh_response(response.json(), profile, refresh_token_value)


# ── Credential chain ─────────────────────────────────────────────────────────


def resolve_credential_chain(
    *,
    api_key: str | None = None,
    access_token: str | None = None,
    access_token_provider: Callable[[], str | Awaitable[str]] | None = None,
    profile: str | None = None,
    config_dir: str | None = None,
    auto_refresh: bool = True,
    account_id: str | None = None,
    api_key_header: str = "x-api-key",
) -> AuthState:
    """Resolve the credential chain (synchronous).

    Resolution order:
    1. Explicit ``api_key``
    2. Explicit ``access_token`` (static string)
    3. Explicit ``access_token_provider`` (callback)
    4. ``SECLAI_API_KEY`` environment variable
    5. SSO profile from config file + cached tokens
    6. Error

    Raises:
        RuntimeError: If no credentials are found.
    """
    # 1. Explicit API key
    if api_key:
        return AuthState(
            mode="api_key",
            api_key=api_key.strip(),
            api_key_header=api_key_header,
            account_id=account_id,
            auto_refresh=False,
        )

    # 2. Static access token
    if access_token:
        return AuthState(
            mode="bearer_static",
            access_token=access_token,
            api_key_header=api_key_header,
            account_id=account_id,
            auto_refresh=False,
        )

    # 3. Access token provider
    if access_token_provider:
        return AuthState(
            mode="bearer_provider",
            access_token_provider=access_token_provider,
            api_key_header=api_key_header,
            account_id=account_id,
            auto_refresh=False,
        )

    # 4. SECLAI_API_KEY env var
    env_key = os.getenv("SECLAI_API_KEY", "").strip()
    if env_key:
        return AuthState(
            mode="api_key",
            api_key=env_key,
            api_key_header=api_key_header,
            account_id=account_id,
            auto_refresh=False,
        )

    # 5. SSO profile
    try:
        resolved_dir = resolve_config_dir(config_dir)
        profile_name = profile or os.getenv("SECLAI_PROFILE") or "default"
        sso = load_sso_profile(resolved_dir, profile_name)
        if sso:
            return AuthState(
                mode="sso",
                api_key_header=api_key_header,
                account_id=account_id or sso.sso_account_id,
                sso_profile=sso,
                config_dir=str(resolved_dir),
                auto_refresh=auto_refresh,
            )
    except (OSError, configparser.Error):
        pass

    # 6. Nothing found
    raise RuntimeError(
        "Missing credentials. Pass api_key=..., access_token=..., "
        "set SECLAI_API_KEY, or run `seclai auth login`."
    )


# ── Per-request auth header resolution ────────────────────────────────────────


def resolve_auth_headers_sync(state: AuthState) -> dict[str, str]:
    """Resolve auth headers for a sync request.

    Args:
        state: Resolved authentication state.

    Returns:
        Header dict with the appropriate auth header(s).

    Raises:
        TypeError: If an async ``access_token_provider`` is used with a sync client.
    """
    headers: dict[str, str] = {}

    if state.mode == "api_key":
        headers[state.api_key_header] = state.api_key  # type: ignore[assignment]
    elif state.mode == "bearer_static":
        headers["authorization"] = f"Bearer {state.access_token}"
    elif state.mode == "bearer_provider":
        token = state.access_token_provider()  # type: ignore[misc]
        if hasattr(token, "__await__"):
            raise TypeError(
                "Async access_token_provider used with sync Seclai client. "
                "Use a sync provider or switch to AsyncSeclai."
            )
        headers["authorization"] = f"Bearer {token}"
    elif state.mode == "sso":
        token = _resolve_sso_token_sync(state)
        headers["authorization"] = f"Bearer {token}"

    if state.account_id:
        headers["x-account-id"] = state.account_id

    return headers


async def resolve_auth_headers_async(state: AuthState) -> dict[str, str]:
    """Resolve auth headers for an async request.

    Args:
        state: Resolved authentication state.

    Returns:
        Header dict with the appropriate auth header(s).
    """
    headers: dict[str, str] = {}

    if state.mode == "api_key":
        headers[state.api_key_header] = state.api_key  # type: ignore[assignment]
    elif state.mode == "bearer_static":
        headers["authorization"] = f"Bearer {state.access_token}"
    elif state.mode == "bearer_provider":
        token = state.access_token_provider()  # type: ignore[misc]
        if hasattr(token, "__await__"):
            token = await token  # type: ignore[misc]
        headers["authorization"] = f"Bearer {token}"
    elif state.mode == "sso":
        token = await _resolve_sso_token_async(state)
        headers["authorization"] = f"Bearer {token}"

    if state.account_id:
        headers["x-account-id"] = state.account_id

    return headers


def _resolve_sso_token_sync(state: AuthState) -> str:
    """Resolve a valid SSO token, refreshing from cache if needed (sync)."""
    profile = state.sso_profile
    assert profile is not None
    config_dir = Path(state.config_dir) if state.config_dir else resolve_config_dir()

    cached = read_sso_cache(config_dir, profile)

    if cached and is_token_valid(cached):
        return cached.access_token

    if cached and cached.refresh_token and state.auto_refresh:
        with state._sync_refresh_lock:
            # Re-check after acquiring lock — another thread may have refreshed
            cached = read_sso_cache(config_dir, profile)
            if cached and is_token_valid(cached):
                return cached.access_token
            if cached and cached.refresh_token:
                refreshed = refresh_token_sync(profile, cached.refresh_token)
                write_sso_cache(config_dir, profile, refreshed)
                return refreshed.access_token

    raise RuntimeError(_SSO_EXPIRED_MSG)


async def _resolve_sso_token_async(state: AuthState) -> str:
    """Resolve a valid SSO token, refreshing from cache if needed (async)."""
    profile = state.sso_profile
    assert profile is not None
    config_dir = Path(state.config_dir) if state.config_dir else resolve_config_dir()

    cached = read_sso_cache(config_dir, profile)

    if cached and is_token_valid(cached):
        return cached.access_token

    if cached and cached.refresh_token and state.auto_refresh:
        async with state._async_refresh_lock:
            # Re-check after acquiring lock — another task may have refreshed
            cached = read_sso_cache(config_dir, profile)
            if cached and is_token_valid(cached):
                return cached.access_token
            if cached and cached.refresh_token:
                refreshed = await refresh_token_async(profile, cached.refresh_token)
                write_sso_cache(config_dir, profile, refreshed)
                return refreshed.access_token

    raise RuntimeError(_SSO_EXPIRED_MSG)
