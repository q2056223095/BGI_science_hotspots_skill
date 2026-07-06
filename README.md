# BGI Science Hotspots Skill

> 华大教育中心科学热点转译技能包：把科学新闻转化为小红书科普文案、轮播图方案和可复用内容方法。

本仓库用于沉淀一套可持续复用的内容生产方法，帮助华大教育中心将每周科学热点转化为：

- 小红书科普文案
- 科学热点背后的教育洞察
- 青少年科学教育 / 精准健康 / AI 时代人才相关内容
- 5 张独立小红书轮播图规划
- 统一视觉风格参考图
- 去 AI 味人工编辑后的真实发布稿
- AI 味自查自纠评分与发布前质检

---

## 一句话定位

这不是“追热点”的工具，而是一个把热点转化为：

```text
品牌认知 + 教育洞察 + 用户信任 + 后续转化入口
```

的内容生产 Skill。
它的核心目标不是快速生成一篇“看起来完整”的科普文，而是形成一套：

科学热点识别
- 事实核验
- 内容转译
- 去 AI 味人工编辑
- 自查自纠
- 小红书发布
- 轮播图视觉规划

的稳定工作流。

---

## 适用对象

- 华大教育中心内容团队
- 小红书 / 公众号运营同事
- 课程产品与直播策划同事
- 青少年创新班、科研实践、精准健康课程相关项目组
- 需要把科学热点转化为传播内容的项目负责人
- 需要保持内容风格统一的 AI 内容协作人员

---

## 仓库结构

```text
BGI_science_hotspots_skill/
├── README.md
├── SKILL.md
├── LICENSE
├── VERSION
├── CHANGELOG.md
├── CONTRIBUTING.md
├── REPOSITORY_STRUCTURE.md
├── prompts/
│   └── master_prompt.md
├── templates/
│   ├── xiaohongshu_copy_template.md
│   ├── image_generation_template.md
│   ├── workflow_checklist.md
│   └── anti_ai_self_check.md
├── examples/
│   ├── 01_whale_fall.md
│   ├── 02_muscle_loss.md
│   └── 03_juno.md
├── docs/
│   ├── content_strategy.md
│   ├── source_and_compliance.md
│   ├── visual_style_guide.md
│   └── anti_ai_editorial_layer.md
├── assets/
│   ├── ASSET_INDEX.md
│   └── *.png
├── scripts/
│   └── check_repo.py
└── .github/
    ├── ISSUE_TEMPLATE/
    └── PULL_REQUEST_TEMPLATE.md
```

---

## 快速开始
### 方法 1：直接使用主技能文件
复制 `SKILL.md` 的内容，作为模型的长期规则。
适合场景：
- 想让模型稳定按照华大教育中心风格输出
- 要同时产出文案 + 图片规划
- 要保持同一套栏目感
- 要降低文案的 AI 味、模板感和机构宣传感

### 方法 2：使用总提示词
复制：
```text
prompts/master_prompt.md
```
然后把新的科学热点贴进去即可。

### 方法 3：按已有案例改写
参考：
- `examples/01_whale_fall.md`
- `examples/02_muscle_loss.md`
- `examples/03_juno.md`

建议后续新增案例时，也保留：
- 原始热点事实
- 小红书发布文案
- 轮播图结构
- 图片提示词
- AI 味自查评分
- 修改前后差异说明
---

## 内容生产流程

建议每条热点按以下流程处理：

```text
热点筛选
→ 选题判断：品牌 / 健康 / 教育观点
→ 核心事实核准
→ 初稿生成
→ 去 AI 味人工编辑
→ AI 味自查评分
→ 不达标重写
→ 标题与正文定稿
→ 5 张轮播图规划
→ 图片生成提示词
→ 合规检查
→ 发布
```

对应文件：

SKILL.md                              主技能规则
docs/content_strategy.md              内容策略
docs/source_and_compliance.md         来源与合规
docs/visual_style_guide.md            视觉规范
docs/anti_ai_editorial_layer.md       去 AI 味人工编辑层
templates/workflow_checklist.md       工作流检查清单
templates/anti_ai_self_check.md       AI 味自查自纠评分表


---

v0.3.0 重要升级：去 AI 味编辑与自查
本版本新增两个关键模块：
1. 去 AI 味人工编辑层
文件：
docs/anti_ai_editorial_layer.md
用于降低：
模板感
口号感
机械排比感
机构宣传感
空泛大词堆叠
过度完整但不自然的 AI 逻辑链

核心要求：
每篇至少加入具体事实、数字或真实观察场景
“不是……而是……”最多使用 2 次
品牌转化不得过早出现
健康和科研内容必须保留科学边界
文案要像真实编辑或科学教育从业者的判断，而不是机构宣传稿

2. AI 味自查自纠评分模块
文件：
templates/anti_ai_self_check.md
每篇文案完成后，必须从 8 个维度评分：
真实感
具体性
句式自然度
科学可信度
平台适配度
转化克制度
情绪克制度
人工编辑完成度
总分 40 分。
最低发布标准：
总分不得低于 30 分
句式自然度不得低于 4 分
科学可信度不得低于 4 分
转化克制度不得低于 4 分
必须至少包含 1 个具体事实、数字或真实场景
必须完成一次去 AI 味编辑

三类内容方向
1. 品牌主线科普文
适合：
鲸落
生物多样性
生命周期
自然教育
物种关系
生态系统

作用：
建立华大教育中心“生命科学教育”的品牌辨识度
让用户看到科学教育不只是知识讲解，而是帮助孩子理解生命关系和真实世界

2. 健康转化科普文
适合：
肌肉流失
营养
睡眠
运动干预
衰老机制
慢病风险
精准健康管理
作用：
连接精准健康、健康管理师、运动处方师等课程方向
让用户理解健康管理不是泛泛建议，而是系统评估、机制理解和个体化方案

4. 教育观点文
适合：
JUNO
大科学装置
AI+科研
跨学科科学问题
科研实践
专业选择
未来人才能力

作用：
服务 AI 时代人才选拔逻辑
服务青少年创新班、科研实践和专业选择
帮助家长理解未来孩子需要的不只是刷题能力，而是提出问题、使用工具、理解数据、判断结果和协作解决复杂问题的能力
视觉风格

图片统一遵循：
小红书 3:4 竖版
5 张独立图，不拼成长图
专业、可信、现代、清爽、轻科技感
深蓝 / 科技蓝 / 白底 / 少量亮黄
信息图风格，每页一个核心结论
不做低级海报感
不做电商风
不做纯装饰图
不做过度炫光、虚假科技感

详细规范见：
docs/visual_style_guide.md
assets/ASSET_INDEX.md

合规提醒
健康类内容必须避免：
医疗诊断
治疗承诺
“运动防癌”“逆转疾病”等绝对化说法
把动物模型、体外实验、机制研究直接外推到人体结论
用科研结果制造健康焦虑

教育类内容必须避免：
空泛鸡汤
夸大升学承诺
只说“培养能力”但不拆解能力结构
把科学热点强行变成课程广告

科学类内容必须避免：
为了传播效果牺牲准确性
把“研究提示”写成“已经证明”
使用无法核准的夸张表述

更多规则见：
docs/source_and_compliance.md

本地结构检查
可运行：
python scripts/check_repo.py
如果显示：
Structure check passed.
说明文件结构完整。
如果你把 anti_ai_editorial_layer.md 和 anti_ai_self_check.md 加入了结构检查脚本，也需要同步确认这两个文件存在。

GitHub 上传步骤
方式 A：网页上传
进入仓库
打开对应文件
点击编辑按钮
复制新内容覆盖原内容
Commit message 可写：
Update skill workflow with anti-AI editing modules
提交到 main 分支
方式 B：命令行上传
git clone https://github.com/q2056223095/BGI_science_hotspots_skill.git
cd BGI_science_hotspots_skill

# 修改文件后执行
python scripts/check_repo.py
git add .
git commit -m "Add anti-AI editorial and self-check workflow"
git push

当前版本
见：
VERSION
当前建议版本：
0.3.0
