import copy
import importlib.util
import json
import subprocess
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
SPEC = ROOT / "openapi" / "seclai.openapi.json"
SPECFIX = ROOT / "scripts" / "specfix.py"


def _run(src: Path, dst: Path) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(SPECFIX), str(src), str(dst)],
        capture_output=True,
        text=True,
        check=False,
    )


def test_specfix_adds_the_retained_field(tmp_path: Path) -> None:
    dst = tmp_path / "out.json"
    result = _run(SPEC, dst)
    assert result.returncode == 0, result.stderr
    out = json.loads(dst.read_text(encoding="utf-8"))
    props = out["components"]["schemas"]["SetSlackTriggerConfigApiRequest"][
        "properties"
    ]
    assert props["input"]["deprecated"] is True


def test_specfix_fails_when_the_spec_declares_a_retained_field_again(
    tmp_path: Path,
) -> None:
    spec = json.loads(SPEC.read_text(encoding="utf-8"))
    spec["components"]["schemas"]["SetSlackTriggerConfigApiRequest"]["properties"][
        "input"
    ] = {"type": "string"}
    src = tmp_path / "in.json"
    src.write_text(json.dumps(spec), encoding="utf-8")
    dst = tmp_path / "out.json"

    result = _run(src, dst)

    assert result.returncode == 1
    assert (
        "stale entry `SetSlackTriggerConfigApiRequest.input` in the retained-fields "
        "list: the spec declares it again; remove the entry"
    ) in result.stderr
    assert not dst.exists()


def test_specfix_applies_no_entry_when_one_is_stale(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    spec_loader = importlib.util.spec_from_file_location("specfix", SPECFIX)
    assert spec_loader is not None and spec_loader.loader is not None
    specfix = importlib.util.module_from_spec(spec_loader)
    spec_loader.loader.exec_module(specfix)
    monkeypatch.setattr(
        specfix,
        "RETAINED_REQUEST_FIELDS",
        [
            ("Fresh", "kept", {"type": "string"}),
            ("Stale", "back", {"type": "string"}),
        ],
    )
    spec = {
        "components": {
            "schemas": {
                "Fresh": {"properties": {}},
                "Stale": {"properties": {"back": {"type": "integer"}}},
            }
        }
    }
    before = copy.deepcopy(spec)

    errors = specfix.retain_removed_request_fields(spec)

    assert len(errors) == 1 and "stale entry `Stale.back`" in errors[0]
    assert spec == before
