"""Every third-party module the package imports is a declared runtime dependency.

The dev group installs more than the published wheel requires, so an import
that only a dev tool provides passes every other test and fails for users.
"""

from __future__ import annotations

import ast
import pathlib
import sys
import tomllib

ROOT = pathlib.Path(__file__).resolve().parent.parent
PACKAGE = ROOT / "seclai"

# Import name -> distribution name, where they differ.
DISTRIBUTIONS = {"dateutil": "python-dateutil"}


def _normalise(name: str) -> str:
    return name.lower().replace("_", "-")


def _imported_modules() -> dict[str, pathlib.Path]:
    """Top-level module names imported under ``seclai/``, with one file each."""
    found: dict[str, pathlib.Path] = {}
    for path in sorted(PACKAGE.rglob("*.py")):
        for node in ast.walk(ast.parse(path.read_text(), filename=str(path))):
            if isinstance(node, ast.Import):
                names = [alias.name for alias in node.names]
            elif isinstance(node, ast.ImportFrom) and node.level == 0 and node.module:
                names = [node.module]
            else:
                continue
            for name in names:
                found.setdefault(name.split(".")[0], path)
    return found


def _declared() -> set[str]:
    with (ROOT / "pyproject.toml").open("rb") as handle:
        dependencies = tomllib.load(handle)["tool"]["poetry"]["dependencies"]
    return {_normalise(name) for name in dependencies if name != "python"}


def test_package_is_walked() -> None:
    imported = _imported_modules()
    assert "httpx" in imported
    assert any("_generated" in path.parts for path in PACKAGE.rglob("*.py"))


def test_every_third_party_import_is_a_runtime_dependency() -> None:
    declared = _declared()
    undeclared = {
        module: str(path.relative_to(ROOT))
        for module, path in _imported_modules().items()
        if module not in sys.stdlib_module_names
        and module != PACKAGE.name
        and _normalise(DISTRIBUTIONS.get(module, module)) not in declared
    }
    assert (
        undeclared == {}
    ), f"imported but not in [tool.poetry.dependencies]: {undeclared}"
