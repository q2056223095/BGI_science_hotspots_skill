#!/usr/bin/env python3
"""Validate the structure of BGI Science Hotspots regression manifests.

This script checks test assets only. It does not call an LLM, verify scientific
claims on the web, or score generated copy.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MANIFESTS = [
    ROOT / "tests" / "regression" / "manifest.json",
    ROOT / "tests" / "regression" / "round2_cases.json",
]

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
EXPECTED_BASELINES = {
    "0.4.0": "8ba25cd5f44f723e0b23e4581209c6204e1ab849",
    "0.5.1": "602c1d9766cb18d22b80764d0cd75fcf581248b7",
}


def fail(message: str) -> int:
    print(f"Regression suite check failed: {message}", file=sys.stderr)
    return 1


def load_manifest(path: Path) -> dict:
    if not path.exists():
        raise ValueError(f"missing {path.relative_to(ROOT)}")
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise ValueError(f"invalid JSON in {path.relative_to(ROOT)}: {exc}") from exc
    if not isinstance(data, dict):
        raise ValueError(f"{path.relative_to(ROOT)} must contain a JSON object")
    return data


def validate_baselines(data: dict, path: Path) -> None:
    baselines = data.get("frozen_baselines")
    if not isinstance(baselines, dict):
        raise ValueError(f"{path.name}.frozen_baselines must be an object")
    for version, expected_sha in EXPECTED_BASELINES.items():
        sha = baselines.get(version)
        if sha != expected_sha:
            raise ValueError(
                f"{path.name} baseline {version} must remain frozen at {expected_sha}"
            )


def validate_case(case: dict, index: int, path: Path, ids: set[str], seen_types: set[str]) -> None:
    missing = REQUIRED_CASE_KEYS - case.keys()
    if missing:
        raise ValueError(
            f"{path.name} case #{index} missing keys: {sorted(missing)}"
        )

    case_id = case["id"]
    if not isinstance(case_id, str) or not case_id.startswith("R"):
        raise ValueError(f"{path.name} case #{index} has invalid id: {case_id!r}")
    if case_id in ids:
        raise ValueError(f"duplicate case id across manifests: {case_id}")
    ids.add(case_id)

    case_type = case["type"]
    if isinstance(case_type, str):
        seen_types.add(case_type)

    for key in ("sources", "source_facts", "expected_behaviors", "failure_traps"):
        value = case[key]
        if not isinstance(value, list) or not value:
            raise ValueError(f"{case_id}.{key} must be a non-empty list")
        if not all(isinstance(item, str) and item.strip() for item in value):
            raise ValueError(f"{case_id}.{key} contains an invalid item")

    if case_type != "image_protocol":
        external_sources = [
            item for item in case["sources"] if item.startswith(("https://", "http://"))
        ]
        if not external_sources:
            raise ValueError(f"{case_id} must include at least one external source URL")

    if len(case["source_facts"]) < 3 and case_type != "image_protocol":
        raise ValueError(f"{case_id} should contain at least 3 independent source facts")
    if len(case["expected_behaviors"]) < 3:
        raise ValueError(f"{case_id} should contain at least 3 expected behaviors")
    if len(case["failure_traps"]) < 3:
        raise ValueError(f"{case_id} should contain at least 3 failure traps")

    risk_tags = case.get("risk_tags")
    if risk_tags is not None:
        if not isinstance(risk_tags, list) or not risk_tags:
            raise ValueError(f"{case_id}.risk_tags must be a non-empty list when present")
        if not all(isinstance(item, str) and item.strip() for item in risk_tags):
            raise ValueError(f"{case_id}.risk_tags contains an invalid item")


def main() -> int:
    ids: set[str] = set()
    seen_types: set[str] = set()
    total_cases = 0

    try:
        for path in MANIFESTS:
            data = load_manifest(path)
            validate_baselines(data, path)
            cases = data.get("cases")
            if not isinstance(cases, list) or not cases:
                raise ValueError(f"{path.name}.cases must be a non-empty list")
            for index, case in enumerate(cases, start=1):
                if not isinstance(case, dict):
                    raise ValueError(f"{path.name} case #{index} must be an object")
                validate_case(case, index, path, ids, seen_types)
                total_cases += 1
    except ValueError as exc:
        return fail(str(exc))

    missing_types = REAL_TYPES - seen_types
    if missing_types:
        return fail(f"missing real science case types: {sorted(missing_types)}")

    print("Regression suite structure passed.")
    print(f"Manifests: {len(MANIFESTS)}")
    print(f"Cases: {total_cases}")
    print(f"Frozen baselines: {', '.join(sorted(EXPECTED_BASELINES))}")
    print(f"Covered core science types: {', '.join(sorted(REAL_TYPES))}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
