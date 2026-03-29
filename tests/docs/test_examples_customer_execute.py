"""Sanity checks for ``docs/examples/customer_execute_body.json``."""

from __future__ import annotations

import json
from pathlib import Path

_REPO_ROOT = Path(__file__).resolve().parents[2]
BODY = _REPO_ROOT / "docs" / "examples" / "customer_execute_body.json"


def test_customer_execute_body_exists_and_shape() -> None:
    assert BODY.is_file(), f"expected {BODY}"
    data = json.loads(BODY.read_text(encoding="utf-8"))
    assert isinstance(data.get("input"), dict)
    assert isinstance(data.get("skills"), list) and data["skills"]
    for item in data["skills"]:
        assert isinstance(item, dict) and "id" in item
