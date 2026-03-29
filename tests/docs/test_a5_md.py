"""Sanity checks for ``docs/a5/*.md`` link targets."""

from __future__ import annotations

import re
from pathlib import Path

_REPO_ROOT = Path(__file__).resolve().parents[2]
DOCS = _REPO_ROOT / "docs"
A5 = DOCS / "a5"


def test_a5_docs_exist() -> None:
    assert (A5 / "README.md").is_file()
    for name in (
        "telemetry.md",
        "engineering.md",
        "roadmap.md",
        "feedback.md",
        "A5_CHECKLIST.md",
    ):
        assert (A5 / name).is_file(), f"missing {name}"


def test_a5_md_links_resolve() -> None:
    for md_path in sorted(A5.glob("*.md")):
        text = md_path.read_text(encoding="utf-8")
        base = md_path.parent
        for raw in re.findall(r"\]\(([^)]+\.md)\)", text):
            target = (base / raw.split("#", 1)[0]).resolve()
            assert target.is_file(), f"broken {raw!r} in {md_path.name} → {target}"
