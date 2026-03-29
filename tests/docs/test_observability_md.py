"""Sanity checks for ``docs/Observability.md``."""

from __future__ import annotations

import re
from pathlib import Path

_REPO_ROOT = Path(__file__).resolve().parents[2]
DOCS = _REPO_ROOT / "docs"
OBS_DOC = DOCS / "Observability.md"


def test_observability_md_exists() -> None:
    assert OBS_DOC.is_file(), f"expected {OBS_DOC}"


def test_observability_md_internal_md_links_resolve() -> None:
    text = OBS_DOC.read_text(encoding="utf-8")
    for raw in re.findall(r"\]\(([^)]+\.md)\)", text):
        path = (DOCS / raw.split("#", 1)[0]).resolve()
        assert path.is_file(), f"broken link target {raw!r} (resolved {path})"


def test_observability_md_documents_prometheus_path() -> None:
    text = OBS_DOC.read_text(encoding="utf-8")
    assert "/metrics/prometheus" in text
    assert "SENTRY_DSN" in text
