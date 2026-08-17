# BGI Science Hotspots Skill

> 把科学新闻、论文成果和科研发现，转化为准确、克制、有材料推进感、适合小红书传播的中文科普内容。

当前版本：`0.5.1`

---

## 一句话定位

```text
准确事实 + 清楚解释 + 材料推进 + 有限判断 + 科学边界 + 小红书传播感
```

这个 Skill 不追求一篇“结构完整但像标准答案”的稿件。它先核准事实，再检查材料是否足以支撑篇幅，随后让文章沿着读者的自然问题往前走。

核心原则：

```text
先做科普，不做教育转化。
事实决定能说什么，材料决定能写多长。
```

除非用户明确要求，不把科学热点强行转向孩子成长、家长教育、课程价值、活动报名或机构品牌。

---

## 0.5.1 更新了什么

这是一个图片生成执行协议修复版本。

0.5.0 已经规定“5 张独立 3:4 轮播图”，但模型在实际调用图片工具时仍可能把“继续生成图2-图5”误解成“一次做成四宫格 / 双页 / 多页合成”。0.5.1 把这一点升级成硬规则和状态机。

新增规则：

- 规划 5 张与实际生成 5 张明确分离
- 实际出图默认一次只生成 1 张
- 第一次开始做图只生成 P1 封面
- P1 生成后必须停下来等用户确认
- 封面确认后按 P2 → P3 → P4 → P5 逐页生成
- 即使用户说“继续图4-图5”，默认仍先只生成 P4
- 禁止四宫格、双页、上下分屏、左右分屏、长图、contact sheet 和多页总览
- 每页必须是独立 3:4 竖版
- P2–P5 必须继承已确认 P1 的视觉系统
- 多页合成、比例错误、多个页码或混入下一页内容，直接判定为生成失败
- 每次实际图片提示词强制加入单页防拼图前缀

---

## 0.5.0 的核心能力仍然保留

0.5.0 引入科学科普活人感编辑层，方法参考 `human-writing` 的材料、推进和中文修订思路，并针对科学传播和小红书短内容做了适配。

包括：

- 写正文前先建立材料卡
- 短稿至少需要 3 条独立材料
- 每段必须增加新事实、新解释、新限制或新后果
- 作者声音来自信息来路和判断边界
- 禁止虚构读者反应、普通人故事、亲历和采访
- 从“限制某个句式次数”升级为检查翻案腔的写作动作
- 不再强制所有稿件使用同一套六段结构
- 科学边界放在影响判断的位置
- 小红书文风检查脚本

---

## 工作流

```text
热点筛选
→ 原始来源核验
→ 材料卡
→ 事实身份与科学边界
→ 确定唯一主要任务
→ 事实初稿
→ 活人感编辑
→ 科学边界复核
→ 文风检查
→ 正文、轮播图规划与提示词
→ 如需实际出图：P1确认 → P2 → P3 → P4 → P5
```

---

## 快速开始

### 使用主 Skill

将 `SKILL.md` 作为模型长期规则。

### 使用总提示词

复制 `prompts/master_prompt.md`，再附上新的科学热点或原始材料。

### 改稿

初稿完成后读取：

```text
docs/human_editorial_layer.md
templates/anti_ai_self_check.md
```

### 实际做图

读取：

```text
assets/ASSET_INDEX.md
docs/visual_style_guide.md
templates/image_generation_template.md
templates/workflow_checklist.md
```

实际出图默认执行：

```text
只生成 P1（独立 3:4）
→ 等确认
→ 只生成 P2
→ 等继续
→ 只生成 P3
→ 等继续
→ 只生成 P4
→ 等继续
→ 只生成 P5
```

**任何情况下都不要把多页拼成一张图。**

### 运行文风检查

```bash
python scripts/check_copy_style.py draft.md
```

脚本只报警，不自动改文。科学事实、专业术语和必要的纠偏表达需要人工判断。

---

## 仓库结构

```text
BGI_science_hotspots_skill/
├── README.md
├── SKILL.md
├── VERSION
├── CHANGELOG.md
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
├── scripts/
│   ├── check_repo.py
│   └── check_copy_style.py
└── assets/
    ├── ASSET_INDEX.md
    └── *.png
```

---

## 四类内容

- 发现型：新物种、古生物、天文、海洋、生态、地质和考古
- 机制型：大脑、睡眠、免疫、代谢、衰老、营养、运动和疾病机制
- 技术型：AI + 科研、新材料、芯片、机器人、大科学装置和生物技术
- 争议或反常识型：存在真实传播误读、修正旧认识或标题容易写过头的研究

分类用于决定解释重点，不提供固定句式。

---

## 图片生成硬规则

默认规划 5 张独立 3:4 轮播图，每张只承担一个主要信息任务。

实际图片生成：

- 一次只生成一张
- 第一次只生成 P1
- P1 必须先确认
- P2–P5 一张一张继续
- 一个画布只能有一个页码
- 禁止多页合成
- 后续页继承封面视觉系统
- 错误结果重新生成当前页，不继续下一页

详细规则见：

- `SKILL.md` 第十七节
- `templates/image_generation_template.md`
- `docs/visual_style_guide.md`
- `templates/workflow_checklist.md`

---

## 合规

- 健康和医学内容不做诊断、治疗承诺和焦虑营销
- 动物、体外、机制和小样本研究不直接外推到人群
- 技术内容区分预测、验证、原型、试点和应用
- 科研发现不把局部修正写成彻底推翻
- 自然生态内容避免过度拟人化和童话化
- 不强行加入教育、课程、品牌和销售转化

---

## 致谢与许可

本仓库的活人感编辑方法参考了开源项目 `KKKKhazix/human-writing`。具体说明见 `THIRD_PARTY_NOTICES.md`。

本仓库自身许可见 `LICENSE`。
