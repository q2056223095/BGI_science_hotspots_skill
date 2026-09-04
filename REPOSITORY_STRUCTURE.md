# Repository Structure

```text
BGI_science_hotspots_skill/
├── README.md
├── SKILL.md
├── LICENSE
├── VERSION
├── CHANGELOG.md
├── CONTRIBUTING.md
├── REPOSITORY_STRUCTURE.md
├── THIRD_PARTY_NOTICES.md
├── prompts/
│   └── master_prompt.md
├── templates/
│   ├── evidence_identity_card.md
│   ├── xiaohongshu_copy_template.md
│   ├── image_generation_template.md
│   ├── workflow_checklist.md
│   └── anti_ai_self_check.md
├── docs/
│   ├── evidence_identity_layer.md
│   ├── content_strategy.md
│   ├── source_and_compliance.md
│   ├── visual_style_guide.md
│   ├── human_editorial_layer.md
│   └── anti_ai_editorial_layer.md
├── tests/
│   ├── VALIDATION.md
│   └── regression/
│       ├── manifest.json
│       ├── round2_cases.json
│       ├── evidence_identity_contract.json
│       └── results/
│           ├── README.md
│           ├── round1.md
│           ├── round2.md
│           ├── round2_runs.json
│           ├── round2_summary.json
│           └── ROUND2_SOURCE_NOTES.md
├── examples/
│   ├── 01_whale_fall.md
│   ├── 02_muscle_loss.md
│   ├── 03_juno.md
│   └── 04_human_editorial_before_after.md
├── assets/
│   ├── ASSET_INDEX.md
│   └── *.png
├── scripts/
│   ├── check_repo.py
│   ├── check_regression_suite.py
│   └── check_copy_style.py
└── .github/
    ├── ISSUE_TEMPLATE/
    │   ├── new_hotspot.md
    │   └── visual_refinement.md
    └── PULL_REQUEST_TEMPLATE.md
```

---

## 核心文件

### `SKILL.md`

主技能规则。0.5.2 起主执行链为：

```text
原始来源核验
→ Evidence Identity Table
→ Claim Ceiling
→ 材料卡
→ Laundering 检查
→ 事实初稿
→ Claim Ceiling Gate
→ 活人感编辑
→ 科学边界复核
→ 文风检查
→ 交付
```

同时完整保留 0.5.1 的单页图片生成状态机。

只复制一个文件时，优先使用它。

### `docs/evidence_identity_layer.md`

0.5.2 新增结构层。定义：

- Source Identity
- Evidence Subject
- Study Design
- Evidence Stage
- Claim Type
- Claim Ceiling
- Subject / Source-Scope / Evidence / Comparison / Stage Laundering
- Critical Failure

它回答的不是“这条来源靠谱吗”，而是“这条证据最多允许支持到什么结论”。

### `templates/evidence_identity_card.md`

写正文前使用的 Evidence Card 和 Claim Ceiling Gate 工作表。

### `tests/regression/evidence_identity_contract.json`

机器可读 Evidence Identity contract。当前固定 Round 2 的 R006–R008：

- R006：不同研究对象证据不得洗强
- R007：传播标题不得洗掉 `mouse model` 范围
- R008：公司初步临床数据与 cross-trial 必须降级

### `docs/human_editorial_layer.md`

初稿后的活人感编辑层。重点检查材料是否足以支撑篇幅、作者凭什么知道、每段新增了什么、是否虚构现场和读者反应、是否使用翻案腔和洞察路标，以及科学边界是否放在正确位置。

0.5.2 中它发生在 Claim Ceiling Gate 之后，不负责改变证据等级。

### `docs/anti_ai_editorial_layer.md`

旧文件名的兼容入口。0.5.0 起转向 `docs/human_editorial_layer.md`。

### `templates/xiaohongshu_copy_template.md`

动笔前工作卡。0.5.2 起包含 Evidence Identity Table、材料卡、说话位置、Claim Ceiling Gate、主路径、段落推进和科学边界。

### `templates/anti_ai_self_check.md`

发布前内部评分。包含材料充分度、段落推进、说话位置和模型化修辞控制。

### `templates/image_generation_template.md`

轮播图规划与实际出图模板。0.5.1 起明确区分“规划 5 张”和“实际逐页生成”，并强制：

```text
P1 独立 3:4 → 等确认 → P2 → P3 → P4 → P5
```

禁止四宫格、双页、分屏、长图、contact sheet 和任何多页合成。

### `scripts/check_regression_suite.py`

检查：

- Round 1 / Round 2 manifests
- 冻结 baseline SHA
- 重复 Case ID
- 必填字段
- Evidence Identity contract 0.5.2
- 六个 Evidence Identity 字段
- R006–R008 contract 覆盖

脚本不调用 LLM，不替代真实回测。

### `scripts/check_repo.py`

检查仓库所需文件、0.5.2 版本一致性和 SKILL 中的 Evidence Identity 核心标记。

### `scripts/check_copy_style.py`

中文文风静态检查脚本。检查高风险翻案腔、洞察路标、假读者、伪人味、名词化、连词密度和句长整齐度。

脚本只报警，不自动改文。

---

## 推荐使用顺序

### 文案阶段

```text
1. SKILL.md
2. docs/source_and_compliance.md
3. docs/evidence_identity_layer.md
4. templates/evidence_identity_card.md
5. templates/xiaohongshu_copy_template.md
6. 生成事实初稿
7. Claim Ceiling Gate
8. docs/human_editorial_layer.md
9. templates/anti_ai_self_check.md
10. scripts/check_copy_style.py
```

### 验证阶段

```text
1. python scripts/check_repo.py
2. python scripts/check_regression_suite.py
3. 重跑 R006–R008
4. 再跑全量 R001–R008
```

### 图片阶段

```text
1. SKILL.md 图片协议
2. assets/ASSET_INDEX.md
3. docs/visual_style_guide.md
4. templates/image_generation_template.md
5. templates/workflow_checklist.md
6. 只生成 P1
7. 用户确认后逐页生成 P2–P5
```

---

## 新增案例规范

每个案例建议包含：

1. 内容类型
2. 本篇唯一主要任务
3. 关键 Evidence Cards / Claim Ceiling
4. 材料卡
5. 说话位置
6. 不建议写法及问题定位
7. 推荐写法方向或完整成稿
8. 科学边界
9. 轮播图规划

不再要求公开内部评分。示例应展示修改动作，而不是让模型记住一组固定句式。

---

## 版本

当前结构对应：

```text
0.5.2
```

0.5.0：材料推进与活人感编辑层。

0.5.1：实际图片生成单页状态机。

0.5.2：Evidence Identity & Claim Ceiling Layer，防止研究对象洗宽、证据洗强、比较洗强和研究阶段洗成熟。
