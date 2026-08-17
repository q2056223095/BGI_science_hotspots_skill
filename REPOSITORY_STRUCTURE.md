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
│   ├── xiaohongshu_copy_template.md
│   ├── image_generation_template.md
│   ├── workflow_checklist.md
│   └── anti_ai_self_check.md
├── docs/
│   ├── content_strategy.md
│   ├── source_and_compliance.md
│   ├── visual_style_guide.md
│   ├── human_editorial_layer.md
│   └── anti_ai_editorial_layer.md
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

主技能规则。定义事实核验、材料卡、说话位置、段落推进、科学边界、小红书呈现、轮播图、实际图片生成协议和合规要求。

只复制一个文件时，优先使用它。

### `docs/human_editorial_layer.md`

初稿后的活人感编辑层。重点检查材料是否足以支撑篇幅、作者凭什么知道、每段新增了什么、是否虚构现场和读者反应、是否使用翻案腔和洞察路标，以及科学边界是否放在正确位置。

### `docs/anti_ai_editorial_layer.md`

旧文件名的兼容入口。0.5.0 起转向 `docs/human_editorial_layer.md`。

### `templates/xiaohongshu_copy_template.md`

动笔前工作卡。包含任务、来源身份、材料卡、说话位置、主路径、段落推进和科学边界。

### `templates/anti_ai_self_check.md`

发布前内部评分。包含材料充分度、段落推进、说话位置和模型化修辞控制。

### `templates/image_generation_template.md`

轮播图规划与实际出图模板。0.5.1 起明确区分“规划 5 张”和“实际逐页生成”，并强制：

```text
P1 独立 3:4 → 等确认 → P2 → P3 → P4 → P5
```

禁止四宫格、双页、分屏、长图、contact sheet 和任何多页合成。

### `docs/visual_style_guide.md`

定义同组图片的配色、字体、标题层级、信息卡片、图标、留白和科技感强度。P1 确认后，P2–P5 必须继承这一视觉系统。

### `scripts/check_copy_style.py`

中文文风静态检查脚本。检查高风险翻案腔、洞察路标、假读者、伪人味、名词化、连词密度和句长整齐度。

脚本只报警，不自动改文。

---

## 推荐使用顺序

### 文案阶段

```text
1. SKILL.md
2. docs/source_and_compliance.md
3. templates/xiaohongshu_copy_template.md
4. 生成事实初稿
5. docs/human_editorial_layer.md
6. templates/anti_ai_self_check.md
7. scripts/check_copy_style.py
```

### 图片阶段

```text
1. SKILL.md 第十六、十七节
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
3. 材料卡
4. 说话位置
5. 不建议写法及问题定位
6. 推荐写法方向或完整成稿
7. 科学边界
8. 轮播图规划

不再要求公开内部评分。示例应展示修改动作，而不是让模型记住一组固定句式。

---

## 版本

当前结构对应：

```text
0.5.1
```

0.5.0 核心升级：

- 从“去 AI 味句式控制”升级为“材料、推进和中文动作”
- 不再强制固定六段式
- 禁止虚构读者反应和伪现场
- 新增文风检查脚本

0.5.1 核心升级：

- 实际出图一次只生成一页
- 第一张必须先生成并确认 P1 封面
- P2–P5 逐页继续
- 每页必须独立 3:4
- 禁止所有形式的多页合成
- P1 确认后锁定整组视觉系统
- 错误图片必须重生成当前页，不能继续下一页
