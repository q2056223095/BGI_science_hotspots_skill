# BGI Science Hotspots Skill

> 把科学新闻、论文成果和科研发现，转化为准确、克制、有材料推进感、适合小红书传播的中文科普内容。

当前版本：`0.5.0`

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

## 0.5.0 新增了什么

本版本引入科学科普活人感编辑层，方法参考 `human-writing` 的材料、推进和中文修订思路，并针对科学传播和小红书短内容做了适配。

主要变化：

- 写正文前先建立材料卡
- 短稿至少需要 3 条独立材料
- 每段必须增加新事实、新解释、新限制或新后果
- 作者声音来自信息来路和判断边界
- 禁止虚构读者反应、普通人故事、亲历和采访
- 从“限制某个句式次数”升级为检查翻案腔的写作动作
- 不再强制所有稿件使用同一套六段结构
- 科学边界放在影响判断的位置
- 新增小红书文风检查脚本

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
→ 正文、轮播图与提示词
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

## 视觉

默认规划 5 张独立 3:4 轮播图，每张只承担一个主要信息任务。生成提示词前参考：

- `assets/ASSET_INDEX.md`
- `docs/visual_style_guide.md`
- `templates/image_generation_template.md`

不要直接搬运论文图、机构图或新闻图。

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
