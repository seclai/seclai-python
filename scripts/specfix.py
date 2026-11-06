"""Prepare the bundled OpenAPI spec for openapi-python-client.

Reads ``openapi/seclai.openapi.json`` and writes a copy for ``make generate`` to
read, so the bundled spec itself stays identical to the other SDKs' copies.

The copy adds back request properties the spec removed but released models
already exposed (``RETAINED_REQUEST_FIELDS``), so the generated model keeps the
attribute and existing callers keep working. Each is described as ignored by
the API. Remove an entry at the next major version.

Exits non-zero when an entry is stale: its schema, or the schema's
``properties``, is missing, or the spec already declares the property again.
A stale entry must be removed or updated rather than silently skipped. Every
entry is checked first, so on an error none is applied and nothing is written.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

# (schema, property, definition). Mirrors `retainedRequestFields` in
# seclai-go's cmd/specfix.
RETAINED_REQUEST_FIELDS: list[tuple[str, str, dict[str, Any]]] = [
    (
        # Released in 1.9.0; the API ignores it since version 2026-11-04.
        "SetSlackTriggerConfigApiRequest",
        "input",
        {
            "anyOf": [{"type": "string"}, {"type": "null"}],
            "deprecated": True,
            "description": (
                "Deprecated: the trigger's former input template. The API "
                "ignores it; set `alias` to choose the name people type after "
                "`/seclai`."
            ),
            "title": "Input",
        },
    ),
]


def retain_removed_request_fields(spec: dict[str, Any]) -> list[str]:
    """Add each retained field to its schema; return the errors found.

    Every entry is checked before any is applied, so on an error the spec is
    left unchanged.
    """
    errors: list[str] = []
    schemas = spec.get("components", {}).get("schemas", {})
    for schema_name, prop, _ in RETAINED_REQUEST_FIELDS:
        schema = schemas.get(schema_name)
        if not isinstance(schema, dict):
            errors.append(f"schema {schema_name!r} not found")
        elif not isinstance(schema.get("properties"), dict):
            errors.append(f"schema {schema_name!r} has no properties")
        elif prop in schema["properties"]:
            errors.append(
                f"stale entry `{schema_name}.{prop}` in the retained-fields "
                "list: the spec declares it again; remove the entry"
            )
    if errors:
        return errors
    for schema_name, prop, definition in RETAINED_REQUEST_FIELDS:
        schemas[schema_name]["properties"][prop] = dict(definition)
    return errors


def main() -> int:
    if len(sys.argv) != 3:
        print("Usage: python scripts/specfix.py <in.json> <out.json>", file=sys.stderr)
        return 2
    src, dst = Path(sys.argv[1]), Path(sys.argv[2])
    spec = json.loads(src.read_text(encoding="utf-8"))
    errors = retain_removed_request_fields(spec)
    if errors:
        for err in errors:
            print(f"specfix: {err}", file=sys.stderr)
        return 1
    dst.parent.mkdir(parents=True, exist_ok=True)
    dst.write_text(json.dumps(spec, indent=2) + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    sys.exit(main())
