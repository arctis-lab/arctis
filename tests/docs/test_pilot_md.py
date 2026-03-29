"""Sanity checks for ``docs/pilot/*.md`` link targets."""

from __future__ import annotations

import re
from pathlib import Path

_REPO_ROOT = Path(__file__).resolve().parents[2]
DOCS = _REPO_ROOT / "docs"
PILOT = DOCS / "pilot"


def test_pilot_docs_exist() -> None:
    assert (PILOT / "README.md").is_file()
    for name in (
        "tenant_setup.md",
        "pilot_scope.md",
        "onboarding_call.md",
        "pilot_checklist.md",
        "pilot_success.md",
    ):
        assert (PILOT / name).is_file(), f"missing {name}"


def test_pilot_md_links_resolve() -> None:
    for md_path in sorted(PILOT.glob("*.md")):
        text = md_path.read_text(encoding="utf-8")
        base = md_path.parent
        for raw in re.findall(r"\]\(([^)]+\.md)\)", text):
            target = (base / raw.split("#", 1)[0]).resolve()
            assert target.is_file(), f"broken {raw!r} in {md_path.name} → {target}"
