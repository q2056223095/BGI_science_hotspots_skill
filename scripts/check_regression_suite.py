#!/usr/bin/env python3
"""Validate the structure of tests/regression/manifest.json.

This script checks test assets only. It does not call an LLM, verify scientific
claims on the web, or score generated copy.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "tests" / "regression" / "manifest.json"

REQUIRED_CASE_KEYS = {
    "id",
    "type",
    "title",
    "user_task",
    "sources",
    "source_facts",
    "expected_behaviors",
    "failure_traps",
}

REAL_TYPES = {"mechanism", "discovery", "technology", "controversy"}


def fail(message: str) -> int:
    print(f"Regression suite check failed: {message}", file=sys.stderr)
    return 1


def main() -> int:
    if not MANIFEST.exists():
        return fail(f"missing {MANIFEST.relative_to(ROOT)}")

    try:
        data = json.loads(MANIFEST.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        return fail(f"invalid JSON: {exc}")

    baselines = data.get("frozen_baselines")
    if not isinstance(baselines, dict):
        return fail("frozen_baselines must be an object")

    for version in ("0.4.0", "0.5.1"):
        sha = baselines.get(version)
        if not isinstance(sha, str) or len(sha) != 40:
            return fail(f"baseline {version} must contain a 40-char commit SHA")

    cases = data.get("cases")
    if not isinstance(cases, list) or not cases:
        return fail("cases must be a non-empty list")

    ids: set[str] = set()
    seen_types: set[str] = set()

    for index, case in enumerate(cases, start=1):
        if not isinstance(case, dict):
            return fail(f"case #{index} must be an object")

        missing = REQUIRED_CASE_KEYS - case.keys()
        if missing:
            return fail(f"case #{index} missing keys: {sorted(missing)}")

        case_id = case["id"]
        if not isinstance(case_id, str) or not case_id.startswith("R"):
            return fail(f"case #{index} has invalid id: {case_id!r}")
        if case_id in ids:
            return fail(f"duplicate case id: {case_id}")
        ids.add(case_id)

        case_type = case["type"]
        if isinstance(case_type, str):
            seen_types.add(case_type)

        for key in ("sources", "source_facts", "expected_behaviors", "failure_traps"):
            value = case[key]
            if not isinstance(value, list) or not value:
                return fail(f"{case_id}.{key} must be a non-empty list")
            if not all(isinstance(item, str) and item.strip() for item in value):
                return fail(f"{case_id}.{key} contains an invalid item")

        if case_type != "image_protocol":
            external_sources = [
                item for item in case["sources"] if item.startswith(("https://", "http://"))
            ]
            if not external_sources:
                return fail(f"{case_id} must include at least one external source URL")

        if len(case["source_facts"]) < 3 and case_type != "image_protocol":
            return fail(f"{case_id} should contain at least 3 independent source facts")

        if len(case["expected_behaviors"]) < 3:
            return fail(f"{case_id} should contain at least 3 expected behaviors")

        if len(case["failure_traps"]) < 3:
            return fail(f"{case_id} should contain at least 3 failure traps")

    missing_types = REAL_TYPES - seen_types
    if missing_types:
        return fail(f"missing real science case types: {sorted(missing_types)}")

    print("Regression suite structure passed.")
    print(f"Cases: {len(cases)}")
    print(f"Frozen baselines: {', '.join(sorted(baselines))}")
    print(f"Covered real-science types: {', '.join(sorted(REAL_TYPES))}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
