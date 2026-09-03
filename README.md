# BGI Science Hotspots Skill

> 把科学新闻、论文成果和科研发现，转化为准确、克制、有证据身份与材料推进感、适合小红书传播的中文科普内容。

当前版本：`0.5.2`

---

## 一句话定位

```text
Evidence-first Science-to-XHS
```

核心目标：

```text
准确事实 + Evidence Identity + Claim Ceiling + 清楚解释 + 材料推进 + 有限判断 + 科学边界 + 小红书传播感
```

核心原则：

```text
先做科普，不做教育转化。
事实决定有没有，证据身份决定能说多远，材料决定能写多长，平台只决定怎样呈现。
```

最重要的硬规则：

```text
最终结论 <= 证据允许的 Claim Ceiling
```

除非用户明确要求，不把科学热点强行转向孩子成长、家长教育、课程价值、活动报名或机构品牌。

---

## 0.5.2 更新了什么

0.5.2 来自 Regression Round 2 的三个高风险 Case：

- BAIBA：小鼠干预 + 人源肌管 + 人群相关性会不会被拼成“人体运动平替 / 糖尿病治疗”
- ALS：新闻标题会不会把原论文的 `mouse model` 范围洗掉
- RM-718：`company-reported + ongoing open-label + n=7 + cross-trial` 会不会被包装成“新药已证明有效”

Round 2 说明，单纯有“来源优先级”和“科学边界提醒”还不够。Skill 需要在写作前先判断：

> **这条证据是什么身份，它最多允许支持到什么结论？**

### Evidence Identity 六字段

关键证据必须判断：

```text
source_identity
+ evidence_subject
+ study_design
+ evidence_stage
+ claim_type
+ claim_ceiling
```

并记录：

```text
Allowed Claim
Forbidden Upgrade
```

### Claim Ceiling Gate

事实初稿后，标题与正文关键 Claim 必须回映射：

```text
Claim
→ Evidence ID
→ Claim Type
→ Claim Ceiling
→ 是否越级？
```

找不到 Evidence ID 的重要结论，要么补来源，要么删除或降级。

### 五类 Evidence Laundering

0.5.2 正式识别：

- `Subject Laundering`：`mouse model → human disease`
- `Source-Scope Laundering`：传播标题覆盖原论文更窄范围
- `Evidence Laundering`：动物 / 体外 / 人群观察拼成更强人体结论
- `Comparison Laundering`：cross-trial 写成头对头优效 / 等效
- `Stage Laundering`：prediction / backtest / preliminary / prototype 写成 validated / deployed / proven

详细规则：

- `docs/evidence_identity_layer.md`
- `templates/evidence_identity_card.md`

机器可读回归 contract：

- `tests/regression/evidence_identity_contract.json`

---

## 0.5.1 图片协议继续完整保留

0.5.2 没有回退 0.5.1 的实际出图状态机。

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

禁止：

- 四宫格
- 双页
- 上下 / 左右分屏
- contact sheet
- 长图串联多页
- 一个画布出现多个页码

一个原则：

```text
一次调用 = 一个画布 = 一页 = 一个页码 = 一个核心问题
```

---

## 0.5.0 的活人感编辑能力继续保留

包括：

- 写正文前先建立材料卡
- 短稿至少需要 3 条独立材料
- 每段必须增加新事实、新解释、新限制或新后果
- 作者声音来自信息来路和判断边界
- 禁止虚构读者反应、普通人故事、亲历和采访
- 检查翻案腔、洞察路标、同构排比和空泛大词
- 不再强制固定六段结构
- 科学边界放在影响判断的位置
- 小红书文风静态检查脚本

---

## 0.5.2 工作流

```text
热点 / 材料
→ 原始来源核验
→ Evidence Identity Table
→ Claim Ceiling
→ 材料卡
→ Laundering 检查
→ 唯一主要任务
→ 事实初稿
→ Claim Ceiling Gate
→ 活人感编辑
→ 科学边界复核
→ 文风检查
→ 正文 / 轮播图规划 / 提示词
→ 如需实际出图：P1确认 → P2 → P3 → P4 → P5
```

---

## 快速开始

### 使用主 Skill

将 `SKILL.md` 作为主规则。

### 使用总提示词

复制：

```text
prompts/master_prompt.md
```

再附上新的科学热点或原始材料。

### Evidence Identity

高风险科研 / 医学 / 技术内容优先读取：

```text
docs/evidence_identity_layer.md
templates/evidence_identity_card.md
docs/source_and_compliance.md
```

### 活人感改稿

初稿并通过 Claim Ceiling Gate 后读取：

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

**任何情况下都不要把多页拼成一张图。**

---

## 验证体系

仓库冻结了两个比较基线：

```text
baseline/v0.4.0
baseline/v0.5.1
```

Regression 资产：

```text
tests/VALIDATION.md
tests/regression/manifest.json
tests/regression/round2_cases.json
tests/regression/evidence_identity_contract.json
tests/regression/results/
```

结构检查：

```bash
python scripts/check_regression_suite.py
```

Round 2 的 R006–R008 是 Evidence Identity Layer 的核心防回归 Cases。

注意：现有 Round 1 / Round 2 分数属于 manual same-model controlled replay，不是 seed-controlled 或统计学 benchmark。

---

## 文风检查

```bash
python scripts/check_copy_style.py draft.md
```

脚本只报警，不自动改文。科学事实、专业术语和必要的纠偏表达仍需结合证据判断。

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
├── examples/
├── scripts/
│   ├── check_repo.py
│   ├── check_regression_suite.py
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

## 合规

- 健康和医学内容不做诊断、治疗承诺和焦虑营销
- 动物、体外、机制和小样本研究不直接外推到人群
- 人群观察不自动升级成因果
- 公司初步披露保留来源身份和阶段
- cross-trial 不自动产生优效 / 等效结论
- 技术内容区分 prediction、validation、prototype、pilot 和 deployment
- 科研发现不把局部修正写成彻底推翻
- 不强行加入教育、课程、品牌和销售转化

---

## 致谢与许可

本仓库的活人感编辑方法参考了开源项目 `KKKKhazix/human-writing`。具体说明见 `THIRD_PARTY_NOTICES.md`。

本仓库自身许可见 `LICENSE`。