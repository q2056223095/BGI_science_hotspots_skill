# BGI Science Hotspots Skill

> 华大教育中心科学热点转译技能包：把科学新闻转化为小红书科普文案、轮播图方案和可复用内容方法。

本仓库用于沉淀一套可持续复用的内容生产方法，帮助华大教育中心将每周科学热点转化为：

- 小红书科普文案
- 科学热点背后的教育洞察
- 青少年科学教育 / 精准健康 / AI时代人才相关内容
- 5张独立小红书轮播图规划
- 统一视觉风格参考图

---

## 一句话定位

这不是“追热点”的工具，而是一个把热点转化为：

```text
品牌认知 + 教育洞察 + 用户信任 + 后续转化入口
```

的内容生产 Skill。

---

## 适用对象

- 华大教育中心内容团队
- 小红书 / 公众号运营同事
- 课程产品与直播策划同事
- 青少年创新班、科研实践、精准健康课程相关项目组

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
│   └── workflow_checklist.md
├── examples/
│   ├── 01_whale_fall.md
│   ├── 02_muscle_loss.md
│   └── 03_juno.md
├── docs/
│   ├── content_strategy.md
│   ├── source_and_compliance.md
│   └── visual_style_guide.md
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

---

## 内容生产流程

建议每条热点按以下流程处理：

```text
热点筛选
→ 选题判断：品牌 / 健康 / 教育观点
→ 核心事实核准
→ 标题与正文
→ 5张轮播图规划
→ 图片生成
→ 合规检查
→ 发布
```

详细检查清单见：

```text
templates/workflow_checklist.md
```

---

## 三类内容方向

### 1. 品牌主线科普文

适合：鲸落、生物多样性、生命周期、自然教育。

作用：建立华大教育中心“生命科学教育”的品牌辨识度。

### 2. 健康转化科普文

适合：肌肉流失、营养、睡眠、运动干预、衰老机制。

作用：连接精准健康、健康管理师、运动处方师等课程方向。

### 3. 教育观点文

适合：JUNO、大科学装置、AI+科研、跨学科科学问题。

作用：服务 AI时代人才选拔逻辑、青少年创新班、科研实践和专业选择。

---

## 视觉风格

图片统一遵循：

- 小红书 3:4 竖版
- 5张独立图，不拼成长图
- 专业、可信、现代、清爽、轻科技感
- 深蓝 / 科技蓝 / 白底 / 少量亮黄
- 信息图风格，每页一个核心结论

详细规范见：

```text
docs/visual_style_guide.md
assets/ASSET_INDEX.md
```

---

## GitHub 上传步骤

### 方式 A：网页上传

1. 在 GitHub 新建仓库，例如：

```text
bgi-education-science-hotspots-skill
```

2. 解压本 zip 文件。
3. 将解压后的 `BGI_science_hotspots_skill` 文件夹内所有文件上传到仓库根目录。
4. 确认 GitHub 首页能显示 `README.md`。

### 方式 B：命令行上传

```bash
git init
git add .
git commit -m "Init BGI science hotspots skill"
git branch -M main
git remote add origin <your-repo-url>
git push -u origin main
```

---

## 本地结构检查

可运行：

```bash
python scripts/check_repo.py
```

如果显示：

```text
Structure check passed.
```

说明文件结构完整。

---

## 合规提醒

健康类内容必须避免：

- 医疗诊断
- 治疗承诺
- “运动防癌”“逆转疾病”等绝对化说法
- 把动物模型直接外推到人体结论

教育类内容必须避免：

- 空泛鸡汤
- 夸大升学承诺
- 只说“培养能力”但不拆解能力结构

更多规则见：

```text
docs/source_and_compliance.md
```

---

## 当前版本

见：`VERSION`

当前版本：`0.2.0`

---

## License

默认使用保留所有权利的内部内容许可。详见 `LICENSE`。

如果未来希望开源，请先替换为合适的开源许可证。

