"""Dated API versions known to this release.

The set is open: the API adds versions without an SDK release, and the
``api_version`` client option is typed ``str | None``, so a date newer than this
release knows about can be passed directly. Treat these as convenience constants
rather than an exhaustive list — :meth:`Seclai.get_api_version` reports what the
server actually supports.
"""

from __future__ import annotations

from enum import StrEnum


class ApiVersion(StrEnum):
    """A dated API version. Members are plain strings, so they can be passed
    anywhere ``api_version`` is accepted."""

    V2026_07_01 = "2026-07-01"
    V2026_07_27 = "2026-07-27"


#: Baseline applied to an unpinned, header-less caller.
DEFAULT_API_VERSION = ApiVersion.V2026_07_01

#: Newest version known to this SDK release. May lag the server.
LATEST_API_VERSION = ApiVersion.V2026_07_27


def validate_api_version(version: str | None, *, allow_unknown: bool) -> str | None:
    """Reject a version this release was not built against.

    A newer server version can change response shapes. Request-side mistakes
    surface as a 422, but a changed response just mis-decodes: renamed keys read
    as absent and reshaped payloads land as ``None``, silently. Opting into a
    version the SDK has never seen therefore fails closed unless asked otherwise.

    This guards the header only. An account pinned server-side can still be newer
    than this release — read :meth:`Seclai.get_api_version` and compare
    ``effective_version`` against :data:`LATEST_API_VERSION` to detect that.
    """
    if version is None or allow_unknown:
        return version
    known = [v.value for v in ApiVersion]
    if version not in known:
        raise ValueError(
            f"Unknown api_version {version!r}. This release was built against "
            f"{', '.join(known)}. A newer API version can change response shapes, "
            "which this client would decode incorrectly rather than reject. "
            "Upgrade the SDK, or pass allow_unknown_api_version=True to proceed "
            "anyway."
        )
    return version
