#!/usr/bin/env python3
"""Validate BGI Science Hotspots regression assets.

This script validates repository test structure and the machine-readable
Evidence Identity contract. It does not call an LLM, verify scientific claims
on the web, or score generated copy.
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
EVIDENCE_CONTRACT = ROOT / "tests" / "regression" / "evidence_identity_contract.json"

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

EXPECTED_EVIDENCE_FIELDS = {
    "source_identity",
    "evidence_subject",
    "study_design",
    "evidence_stage",
    "claim_type",
    "claim_ceiling",
}

REQUIRED_CONTRACT_CASES = {"R006", "R007", "R008"}


def fail(message: str) -> int:
    print(f"Regression suite check failed: {message}", file=sys.stderr)
    return 1


def load_json(path: Path) -> dict:
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


def validate_string_list(value: object, label: str) -> None:
    if not isinstance(value, list) or not value:
        raise ValueError(f"{label} must be a non-empty list")
    if not all(isinstance(item, str) and item.strip() for item in value):
        raise ValueError(f"{label} contains an invalid item")


def validate_case(
    case: dict,
    index: int,
    path: Path,
    ids: set[str],
    seen_types: set[str],
) -> None:
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
        validate_string_list(case[key], f"{case_id}.{key}")

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
        validate_string_list(risk_tags, f"{case_id}.risk_tags")


def validate_evidence_contract(all_case_ids: set[str]) -> tuple[int, int]:
    data = load_json(EVIDENCE_CONTRACT)

    if data.get("contract_version") != "0.5.2":
        raise ValueError("evidence_identity_contract.json contract_version must be 0.5.2")

    validate_string_list(data.get("global_invariants"), "contract.global_invariants")
    validate_string_list(data.get("critical_failures"), "contract.critical_failures")

    required_fields = data.get("required_fields")
    validate_string_list(required_fields, "contract.required_fields")
    if set(required_fields) != EXPECTED_EVIDENCE_FIELDS:
        raise ValueError(
            "contract.required_fields must exactly contain the six Evidence Identity fields"
        )

    cases = data.get("cases")
    if not isinstance(cases, list) or not cases:
        raise ValueError("contract.cases must be a non-empty list")

    contract_case_ids: set[str] = set()
    evidence_count = 0

    for index, case in enumerate(cases, start=1):
        if not isinstance(case, dict):
            raise ValueError(f"contract case #{index} must be an object")

        case_id = case.get("case_id")
        if not isinstance(case_id, str) or not case_id.startswith("R"):
            raise ValueError(f"contract case #{index} has invalid case_id: {case_id!r}")
        if case_id in contract_case_ids:
            raise ValueError(f"duplicate case_id in evidence contract: {case_id}")
        if case_id not in all_case_ids:
            raise ValueError(f"evidence contract references unknown regression case: {case_id}")
        contract_case_ids.add(case_id)

        evidence_items = case.get("evidence_identities")
        if not isinstance(evidence_items, list) or not evidence_items:
            raise ValueError(f"{case_id}.evidence_identities must be a non-empty list")

        for evidence_index, evidence in enumerate(evidence_items, start=1):
            if not isinstance(evidence, dict):
                raise ValueError(
                    f"{case_id}.evidence_identities #{evidence_index} must be an object"
                )

            missing = EXPECTED_EVIDENCE_FIELDS - evidence.keys()
            if missing:
                raise ValueError(
                    f"{case_id}.evidence #{evidence_index} missing fields: {sorted(missing)}"
                )

            for field in EXPECTED_EVIDENCE_FIELDS:
                value = evidence[field]
                if not isinstance(value, str) or not value.strip():
                    raise ValueError(
                        f"{case_id}.evidence #{evidence_index}.{field} must be non-empty"
                    )

            evidence_count += 1

        validate_string_list(case.get("forbidden_upgrades"), f"{case_id}.forbidden_upgrades")

    missing_contract_cases = REQUIRED_CONTRACT_CASES - contract_case_ids
    if missing_contract_cases:
        raise ValueError(
            f"evidence contract missing Round 2 core cases: {sorted(missing_contract_cases)}"
        )

    return len(contract_case_ids), evidence_count


def main() -> int:
    ids: set[str] = set()
    seen_types: set[str] = set()
    total_cases = 0

    try:
        for path in MANIFESTS:
            data = load_json(path)
            validate_baselines(data, path)
            cases = data.get("cases")
            if not isinstance(cases, list) or not cases:
                raise ValueError(f"{path.name}.cases must be a non-empty list")
            for index, case in enumerate(cases, start=1):
                if not isinstance(case, dict):
                    raise ValueError(f"{path.name} case #{index} must be an object")
                validate_case(case, index, path, ids, seen_types)
                total_cases += 1

        missing_types = REAL_TYPES - seen_types
        if missing_types:
            raise ValueError(f"missing real science case types: {sorted(missing_types)}")

        contract_cases, evidence_count = validate_evidence_contract(ids)

    except ValueError as exc:
        return fail(str(exc))

    print("Regression suite structure passed.")
    print(f"Manifests: {len(MANIFESTS)}")
    print(f"Cases: {total_cases}")
    print(f"Frozen baselines: {', '.join(sorted(EXPECTED_BASELINES))}")
    print(f"Covered core science types: {', '.join(sorted(REAL_TYPES))}")
    print(f"Evidence Identity contract cases: {contract_cases}")
    print(f"Evidence Identity entries: {evidence_count}")
    print("Evidence Identity fields: " + ", ".join(sorted(EXPECTED_EVIDENCE_FIELDS)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
