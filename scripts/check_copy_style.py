#!/usr/bin/env python3
"""检查科学科普中文稿中的高风险模型化形状。只报警，不自动改文。"""

from __future__ import annotations

import argparse
import re
import statistics
import sys
from dataclasses import dataclass
from pathlib import Path


HARD_JARGON = (
    "赋能",
    "抓手",
    "商业闭环",
    "价值闭环",
    "能力沉淀",
    "底层逻辑",
    "顶层设计",
    "认知跃迁",
    "价值释放",
    "降本增效",
    "内容矩阵",
    "全链路",
    "组合拳",
    "打开想象空间",
)

ROAD_SIGNS = (
    "值得注意的是",
    "需要指出的是",
    "更微妙的是",
    "还有一层",
    "从某种意义上说",
    "一句话总结",
    "先说结论",
    "说到底",
    "真正重要的是",
    "真正值得关注的是",
)

FAKE_READER = (
    "很多人第一反应",
    "大家都以为",
    "相信不少人",
    "普通人肯定会",
    "看到这里你可能会",
    "你一定会问",
)

FAKE_HUMAN = (
    "说实话",
    "我真的被震撼",
    "看完我沉默了",
    "细思极恐",
    "太不可思议了",
    "建议所有人都看看",
)

CONJUNCTIONS = (
    "因为",
    "所以",
    "但是",
    "然而",
    "同时",
    "此外",
    "并且",
    "因此",
    "不仅",
    "而且",
)

PIVOT_PATTERNS = (
    re.compile(r"(?:并)?不是[^。！？\n]{0,90}而是"),
    re.compile(r"并非[^。！？\n]{0,90}而是"),
    re.compile(r"不在于[^。！？\n]{0,90}而在于"),
    re.compile(r"与其说[^。！？\n]{0,90}(?:不如|毋宁|倒不如)"),
    re.compile(r"你以为[^。！？\n]{0,90}(?:其实|实际|却)"),
    re.compile(r"看似[^。！？\n]{0,90}(?:其实|实际|实则)"),
    re.compile(r"[^，。！？\n]{1,18}不重要，(?:重要|要紧)的是"),
)

NOMINALIZATION_PATTERNS = (
    re.compile(r"进行(?:了|一次|一场|着)?[^。，！？\n]{0,12}(?:分析|测量|验证|研究|讨论|优化|调整|比较|评估)"),
    re.compile(r"实现了?[^。，！？\n]{0,16}(?:提升|增长|突破|转变|落地)"),
    re.compile(r"完成了?对[^。，！？\n]{0,18}的"),
    re.compile(r"具有[^。，！？\n]{0,12}(?:意义|价值)"),
    re.compile(r"起到了?[^。，！？\n]{0,12}作用"),
)

TRICOLON_PATTERNS = (
    re.compile(r"(?:不仅|不只)[^。！？\n]{0,60}(?:还|也)[^。！？\n]{0,60}(?:还|也)"),
    re.compile(r"既[^。！？\n]{0,45}又[^。！？\n]{0,45}(?:还|也)"),
)


@dataclass
class WarningItem:
    line: int
    category: str
    excerpt: str


def mask_non_prose(text: str) -> str:
    """屏蔽代码块、网址、Markdown 链接目标和 YAML 元数据，保留位置。"""

    def mask(match: re.Match[str]) -> str:
        return "".join("\n" if char == "\n" else " " for char in match.group())

    patterns = (
        re.compile(r"\A---\s*\n.*?\n---\s*(?:\n|\Z)", re.DOTALL),
        re.compile(r"```.*?```", re.DOTALL),
        re.compile(r"`[^`\n]*`"),
        re.compile(r"\]\([^\n)]*\)"),
        re.compile(r"https?://[^\s)>]+"),
    )
    masked = text
    for pattern in patterns:
        masked = pattern.sub(mask, masked)
    return masked


def line_number(text: str, position: int) -> int:
    return text.count("\n", 0, position) + 1


def excerpt(value: str, width: int = 72) -> str:
    value = re.sub(r"\s+", " ", value).strip()
    return value if len(value) <= width else value[: width - 1] + "…"


def sentence_lengths(text: str) -> list[int]:
    sentences = [
        re.sub(r"\s+", "", item)
        for item in re.split(r"[。！？!?]+", text)
        if re.search(r"[\u4e00-\u9fff]", item)
    ]
    return [len(re.findall(r"[\u4e00-\u9fff]", item)) for item in sentences]


def paragraph_openers(text: str) -> dict[str, list[int]]:
    found: dict[str, list[int]] = {}
    for line_no, paragraph in enumerate(re.split(r"\n\s*\n", text), start=1):
        plain = re.sub(r"^[#>*\-\d.\s]+", "", paragraph).strip()
        if not plain:
            continue
        opener = re.sub(r"[，。！？：:\s].*$", "", plain)[:8]
        if len(opener) >= 2:
            found.setdefault(opener, []).append(line_no)
    return found


def scan(text: str) -> list[WarningItem]:
    masked = mask_non_prose(text)
    warnings: list[WarningItem] = []

    for term in HARD_JARGON:
        for match in re.finditer(re.escape(term), masked):
            warnings.append(
                WarningItem(line_number(masked, match.start()), "商业或模型黑话", term)
            )

    for term in ROAD_SIGNS:
        for match in re.finditer(re.escape(term), masked):
            warnings.append(
                WarningItem(line_number(masked, match.start()), "洞察路标", term)
            )

    for term in FAKE_READER:
        for match in re.finditer(re.escape(term), masked):
            warnings.append(
                WarningItem(line_number(masked, match.start()), "无来源读者反应", term)
            )

    for term in FAKE_HUMAN:
        for match in re.finditer(re.escape(term), masked):
            warnings.append(
                WarningItem(line_number(masked, match.start()), "伪人味", term)
            )

    for pattern in PIVOT_PATTERNS:
        for match in pattern.finditer(masked):
            warnings.append(
                WarningItem(
                    line_number(masked, match.start()),
                    "翻案腔，确认是否有真实误读依据",
                    excerpt(match.group()),
                )
            )

    for pattern in NOMINALIZATION_PATTERNS:
        for match in pattern.finditer(masked):
            warnings.append(
                WarningItem(
                    line_number(masked, match.start()),
                    "名词化或报告腔",
                    excerpt(match.group()),
                )
            )

    for pattern in TRICOLON_PATTERNS:
        for match in pattern.finditer(masked):
            warnings.append(
                WarningItem(
                    line_number(masked, match.start()),
                    "三项以上同构排比",
                    excerpt(match.group()),
                )
            )

    han_count = len(re.findall(r"[\u4e00-\u9fff]", masked))
    conjunction_count = sum(masked.count(term) for term in CONJUNCTIONS)
    if han_count >= 300 and conjunction_count / han_count > 0.025:
        warnings.append(
            WarningItem(
                1,
                "连词密度偏高",
                f"{conjunction_count} 个常见连词 / {han_count} 个汉字",
            )
        )

    lengths = sentence_lengths(masked)
    if len(lengths) >= 8:
        mean = statistics.mean(lengths)
        stdev = statistics.pstdev(lengths)
        if mean > 0 and stdev / mean < 0.28:
            warnings.append(
                WarningItem(
                    1,
                    "句长过于整齐",
                    f"平均 {mean:.1f} 字，变异系数 {stdev / mean:.2f}",
                )
            )

    for opener, lines in paragraph_openers(masked).items():
        if len(lines) >= 3 and opener in {
            "这项研究",
            "这也说明",
            "更重要的",
            "不过",
            "同时",
            "此外",
            "很多人",
        }:
            warnings.append(
                WarningItem(
                    lines[0],
                    "段落开头重复",
                    f"“{opener}”出现 {len(lines)} 次",
                )
            )

    return sorted(warnings, key=lambda item: (item.line, item.category, item.excerpt))


def main() -> int:
    parser = argparse.ArgumentParser(
        description="检查科学科普中文稿中的高风险模型化形状。"
    )
    parser.add_argument("path", type=Path, help="Markdown 或纯文本稿件路径")
    args = parser.parse_args()

    if not args.path.exists():
        print(f"文件不存在：{args.path}", file=sys.stderr)
        return 2

    text = args.path.read_text(encoding="utf-8")
    warnings = scan(text)

    if not warnings:
        print("Style check passed. 未发现高风险模型化形状。")
        return 0

    print(f"发现 {len(warnings)} 项需要人工判断：")
    for item in warnings:
        print(f"- 第 {item.line} 行 [{item.category}] {item.excerpt}")

    print("\n提示：脚本只报警。科学纠偏、专业术语和正式步骤需要结合语境判断。")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
