#!/usr/bin/env python3
"""Basic repository structure checker for BGI science hotspot skill."""

from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]

REQUIRED = [
    "README.md",
    "SKILL.md",
    "LICENSE",
    "VERSION",
    "CHANGELOG.md",
    "CONTRIBUTING.md",
    "REPOSITORY_STRUCTURE.md",
    "THIRD_PARTY_NOTICES.md",

    "prompts/master_prompt.md",

    "templates/xiaohongshu_copy_template.md",
    "templates/image_generation_template.md",
    "templates/workflow_checklist.md",
    "templates/anti_ai_self_check.md",

    "docs/content_strategy.md",
    "docs/source_and_compliance.md",
    "docs/visual_style_guide.md",
    "docs/anti_ai_editorial_layer.md",
    "docs/human_editorial_layer.md",

    "examples/01_whale_fall.md",
    "examples/02_muscle_loss.md",
    "examples/03_juno.md",
    "examples/04_human_editorial_before_after.md",

    "scripts/check_copy_style.py",
    "scripts/check_regression_suite.py",

    "tests/VALIDATION.md",
    "tests/regression/manifest.json",
    "tests/regression/round2_cases.json",
    "tests/regression/results/round1.md",
    "tests/regression/results/round2.md",
    "tests/regression/results/round2_runs.json",
    "tests/regression/results/round2_summary.json",
    "tests/regression/results/ROUND2_SOURCE_NOTES.md",

    "assets/ASSET_INDEX.md",

    ".github/PULL_REQUEST_TEMPLATE.md",
    ".github/ISSUE_TEMPLATE/new_hotspot.md",
    ".github/ISSUE_TEMPLATE/visual_refinement.md",
]


def main() -> int:
    missing = [path for path in REQUIRED if not (ROOT / path).exists()]
    asset_count = len(list((ROOT / "assets").glob("*.png")))

    print(f"Repository root: {ROOT}")
    print(f"PNG assets: {asset_count}")

    if missing:
        print("Missing required files:")
        for path in missing:
            print(f" - {path}")
        return 1

    print("Structure check passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
