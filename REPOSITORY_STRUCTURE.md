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
│   └── workflow_checklist.md         # 工作流检查清单
├── examples/
│   ├── 01_whale_fall.md              # 鲸落案例
│   ├── 02_muscle_loss.md             # 肌肉流失案例
│   └── 03_juno.md                    # JUNO案例
├── docs/
│   ├── content_strategy.md           # 内容策略
│   ├── source_and_compliance.md      # 来源与合规
│   └── visual_style_guide.md         # 视觉规范
├── assets/
│   ├── ASSET_INDEX.md                # 图片资产索引
│   └── *.png                         # 视觉参考图
└── .github/
    ├── ISSUE_TEMPLATE/
    │   ├── new_hotspot.md            # 新热点需求模板
    │   └── visual_refinement.md      # 图片修改需求模板
    └── PULL_REQUEST_TEMPLATE.md      # PR模板
```

## 最重要的 3 个文件

1. `SKILL.md`：模型长期复用的核心规则。
2. `prompts/master_prompt.md`：下次对话可直接复制粘贴的完整提示词。
3. `docs/visual_style_guide.md`：图片风格保持一致的依据。

