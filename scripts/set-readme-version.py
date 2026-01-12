from __future__ import annotations

import os
import shutil
import sys
from pathlib import Path


DOCS_LATEST = "https://seclai.github.io/seclai-python/latest/"


def main() -> int:
    if len(sys.argv) != 2 or sys.argv[1] not in {"apply", "restore"}:
        print("Usage: python scripts/set-readme-version.py <apply|restore>", file=sys.stderr)
        return 2

    mode = sys.argv[1]

    repo_root = Path(__file__).resolve().parent.parent
    readme_path = repo_root / "README.md"
    backup_path = repo_root / ".README.md.bak"

    if mode == "apply":
        version = os.environ.get("VERSION")
        if not version:
            print("Missing VERSION env var.", file=sys.stderr)
            return 2

        if not backup_path.exists():
            shutil.copyfile(readme_path, backup_path)

        original = readme_path.read_text(encoding="utf-8")
        versioned = f"https://seclai.github.io/seclai-python/{version}/"

        # Replace only the canonical docs link. Keep other "latest" mentions untouched.
        updated = original.replace(DOCS_LATEST, versioned)

        readme_path.write_text(updated, encoding="utf-8")
        return 0

    # restore
    if backup_path.exists():
        shutil.copyfile(backup_path, readme_path)
        backup_path.unlink()

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
