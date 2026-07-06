#!/usr/bin/env python3
"""Basic repository structure checker for BGI science hotspot skill."""
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = [
    'README.md',
    'SKILL.md',
    'LICENSE',
    'VERSION',
    'CHANGELOG.md',
    'CONTRIBUTING.md',
    'prompts/master_prompt.md',
    'templates/xiaohongshu_copy_template.md',
    'templates/image_generation_template.md',
    'templates/workflow_checklist.md',
    'docs/content_strategy.md',
    'docs/source_and_compliance.md',
    'docs/visual_style_guide.md',
    'examples/01_whale_fall.md',
    'examples/02_muscle_loss.md',
    'examples/03_juno.md',
    'assets/ASSET_INDEX.md',
    '.github/PULL_REQUEST_TEMPLATE.md',
    '.github/ISSUE_TEMPLATE/new_hotspot.md',
    '.github/ISSUE_TEMPLATE/visual_refinement.md',
    'docs/anti_ai_editorial_layer.md',
    'templates/anti_ai_self_check.md',
]

def main() -> int:
    missing = [p for p in REQUIRED if not (ROOT / p).exists()]
    asset_count = len(list((ROOT / 'assets').glob('*.png')))
    print(f'Repository root: {ROOT}')
    print(f'PNG assets: {asset_count}')
    if missing:
        print('Missing required files:')
        for p in missing:
            print(f'  - {p}')
        return 1
    print('Structure check passed.')
    return 0

if __name__ == '__main__':
    sys.exit(main())
