#!/usr/bin/env python3
"""Static health check for the notebooks in this repository (standard library only).

For every notebook it verifies:
  * the file is valid JSON with the expected nbformat keys;
  * no Colab / widget metadata is left that can stop GitHub from rendering it;
  * no secret-looking strings are present;
  * every local data file referenced in a pandas / sqlite call exists
    relative to the notebook's own folder.

It does NOT execute notebooks. Exit code is 1 if any problem is found.

Usage:  python scripts/check_notebooks.py
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SECRET = re.compile(r"((?<![A-Za-z0-9])sk-[A-Za-z0-9_\-]{20,}|hf_[A-Za-z0-9]{25,}|AKIA[0-9A-Z]{16}|ghp_[A-Za-z0-9]{30,})")
READ_CALL = re.compile(
    r"""(?:read_csv|read_excel|read_json|read_parquet|read_sql\w*|sqlite3\.connect|create_engine)"""
    r"""\(\s*(?:r?)(['"])(?P<ref>[^'"\n]+)\1"""
)
# Files that notebooks mention but that are downloaded or created at run time.
KNOWN_EXTERNAL = {"ds_salaries.csv", "glove.6B.50d.txt", "sample.txt", "class_names.dat", "books_clean.csv"}


def check(path: Path) -> list[str]:
    problems: list[str] = []
    try:
        nb = json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:  # noqa: BLE001
        return [f"invalid JSON: {exc}"]
    for key in ("cells", "metadata", "nbformat", "nbformat_minor"):
        if key not in nb:
            problems.append(f"missing key '{key}'")
    for bad in ("colab", "widgets"):
        if bad in nb.get("metadata", {}):
            problems.append(f"metadata.{bad} present")
    for i, cell in enumerate(nb.get("cells", [])):
        src = "".join(cell.get("source", []))
        if SECRET.search(src):
            problems.append(f"cell {i}: secret-looking string")
        if cell.get("cell_type") != "code":
            continue
        for m in READ_CALL.finditer(src):
            ref = m.group("ref")
            if "://" in ref and not ref.startswith("sqlite:///"):
                continue  # remote URL
            ref = ref.removeprefix("sqlite:///").replace("\\", "/")
            if ref.startswith("/") or Path(ref).name in KNOWN_EXTERNAL:
                continue
            if not (path.parent / ref).resolve().exists():
                problems.append(f"cell {i}: data file not found: {ref}")
    return problems


def main() -> int:
    notebooks = sorted(p for p in ROOT.rglob("*.ipynb") if ".ipynb_checkpoints" not in p.parts)
    failed = 0
    for nb in notebooks:
        issues = check(nb)
        if issues:
            failed += 1
            print(f"FAIL {nb.relative_to(ROOT)}")
            for issue in issues:
                print(f"     - {issue}")
    print(f"\n{len(notebooks)} notebooks checked, {failed} with problems.")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
