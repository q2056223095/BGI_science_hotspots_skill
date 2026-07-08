# Repository Structure

```text
BGI_science_hotspots_skill/
├── README.md                         # 仓库说明与快速开始
├── SKILL.md                          # 主技能文件，最重要
├── LICENSE                           # 默认保留所有权利，可按需替换
├── VERSION                           # 当前版本
├── CHANGELOG.md                      # 版本更新记录
├── CONTRIBUTING.md                   # 贡献与新增案例规范
├── REPOSITORY_STRUCTURE.md           # 仓库结构说明
├── prompts/
│   └── master_prompt.md              # 可直接复制使用的总提示词
├── templates/
│   ├── xiaohongshu_copy_template.md  # 小红书文案模板
│   ├── image_generation_template.md  # 图片生成模板
│   ├── workflow_checklist.md         # 工作流检查清单
│   └── anti_ai_self_check.md         # AI 味自查自纠评分模块
├── examples/
│   ├── 01_whale_fall.md              # 发现型科普案例：鲸落
│   ├── 02_muscle_loss.md             # 机制型科普案例：肌肉流失
│   └── 03_juno.md                    # 技术型科普案例：JUNO
├── docs/
│   ├── content_strategy.md           # 内容策略
│   ├── source_and_compliance.md      # 来源与合规
│   ├── visual_style_guide.md         # 视觉规范
│   └── anti_ai_editorial_layer.md    # 去 AI 味人工编辑层
├── assets/
│   ├── ASSET_INDEX.md                # 图片资产索引
│   └── *.png                         # 视觉参考图
├── scripts/
│   └── check_repo.py                 # 本地结构检查脚本
└── .github/
    ├── ISSUE_TEMPLATE/
    │   ├── new_hotspot.md            # 新热点需求模板
    │   └── visual_refinement.md      # 图片修改需求模板
    └── PULL_REQUEST_TEMPLATE.md      # PR 模板
```

---

## 最重要的 5 个文件

### 1. `SKILL.md`

模型长期复用的核心规则。

这是整个仓库最重要的文件。

如果只复制一个文件给模型使用，优先复制 `SKILL.md`。

它定义：

- 科学热点小红书科普转译定位
- 四类内容方向：发现型 / 机制型 / 技术型 / 争议反常识型
- 文案结构
- 事实核验要求
- 去 AI 味编辑流程
- AI 味自查评分规则
- 轮播图生成规则
- 健康、科研、技术、图片合规要求

---

### 2. `prompts/master_prompt.md`

下次对话可直接复制粘贴的完整提示词。

适合：

- 快速启动一个新热点
- 给 DeepSeek / Kimi / Claude / GPT 等模型复用
- 让不同模型保持同一套工作流

---

### 3. `docs/anti_ai_editorial_layer.md`

去 AI 味人工编辑层。

用于解决：

- 文案太像 AI
- 句式太整齐
- 转化太硬
- 口号感太强
- 大词太多
- 缺少真实观察和具体细节

核心目标：

让内容像一个懂科学、懂传播的人看到科学热点后的真实判断，而不是标准 AI 生成文案或机构宣传稿。

---

### 4. `templates/anti_ai_self_check.md`

AI 味自查自纠评分模块。

用于每篇文案发布前评分。

评分维度包括：

- 真实感
- 具体性
- 句式自然度
- 科学可信度
- 平台适配度
- 转化克制度
- 情绪克制度
- 人工编辑完成度

总分 40 分。低于 30 分不建议发布，必须重写或局部修改。

---

### 5. `docs/visual_style_guide.md`

图片风格保持一致的依据。

用于保证：

- 小红书轮播图风格统一
- 科学信息图不跑偏
- 不出现低级海报感、电商风、过度 AI 风
- 后续批量生成图片时保持同一套视觉语言

---

## 推荐使用顺序

每次处理一个新科学热点时，建议按以下文件顺序执行：

```text
1. SKILL.md
2. docs/content_strategy.md
3. docs/source_and_compliance.md
4. docs/anti_ai_editorial_layer.md
5. templates/anti_ai_self_check.md
6. templates/workflow_checklist.md
7. docs/visual_style_guide.md
8. templates/image_generation_template.md
9. assets/ASSET_INDEX.md
```

---

## 新增案例时的建议结构

如果后续在 `examples/` 中新增案例，建议每个案例至少包含：

```text
1. 热点背景
2. 核心事实
3. 选题判断
4. 小红书标题
5. 小红书正文
6. AI 味自查评分
7. 去 AI 味修改说明
8. 5 张轮播图规划
9. 图片生成提示词
10. 合规检查
```

---

## 版本说明

当前结构对应建议版本：

```text
0.4.0
```

本版本相较 `0.3.0` 的关键变化：

- 从“教育 / 品牌转化型科学热点 skill”改为“纯科普转译型 skill”
- 删除默认教育洞察、孩子成长、课程转化和机构品牌导向
- 将内容方向改为发现型 / 机制型 / 技术型 / 争议反常识型
- 保留事实核验、去 AI 味、视觉规范、合规检查和小红书传播结构
