# Changelog

## [0.3.0] - 2026-07-06

### Added

- 新增 `docs/anti_ai_editorial_layer.md`：去 AI 味人工编辑层，用于降低模板感、口号感、机械排比感、机构宣传感和空泛表达。
- 新增 `templates/anti_ai_self_check.md`：AI 味自查自纠评分模块，用于对小红书发布稿进行评分、判断和自动修正。
- 新增“初稿生成 → 去 AI 味编辑 → AI 味评分 → 不达标重写 → 最终发布稿”的强制工作流。
- 新增 AI 味评分维度：真实感、具体性、句式自然度、科学可信度、平台适配度、转化克制度、情绪克制度、人工编辑完成度。
- 新增最低发布标准：总分不得低于 30 分，句式自然度、科学可信度、转化克制度不得低于 4 分。
- 新增小红书发布稿去 AI 味规则：具体事实、真实观察场景、克制个人判断、科学边界提醒。

### Changed

- 更新 `SKILL.md`，将去 AI 味人工编辑层和 AI 味自查评分模块纳入主流程。
- 更新 `README.md`，补充 v0.3.0 的核心升级说明、文件结构和使用流程。
- 更新 `REPOSITORY_STRUCTURE.md`，加入新增的 `anti_ai_editorial_layer.md` 与 `anti_ai_self_check.md` 文件说明。
- 优化内容生产流程，从“热点转译生成器”升级为“热点转译 + 人工编辑风格 + 发布前自查”的完整工作流。
- 强化健康类、教育类、科学类内容的边界表达，避免夸大科研结论、健康效果或教育效果。
- 强化品牌转化克制度，要求品牌表达自然靠后，避免正文过早出现机构宣传感。

### Notes

- 本版本不改变原有三类内容主线：品牌主线科普文、健康转化科普文、教育观点文。
- 本版本不替代原有视觉规范，而是在文案生成层增加人工编辑感和发布前质检。
- 后续新增案例建议补充 AI 味自查评分和去 AI 味修改说明，便于形成可复用案例库。

---

## [0.2.0] - 2026-07-01

### Added

- Standard GitHub repository structure.
- `LICENSE` using an all-rights-reserved default for protected brand/content assets.
- `.gitignore` for common system, editor, archive, and working files.
- `VERSION` file.
- `CONTRIBUTING.md` for content, image, and factual review workflow.
- `.github/ISSUE_TEMPLATE/` for new hotspot and visual refinement requests.
- `.github/PULL_REQUEST_TEMPLATE.md` for review consistency.
- `prompts/master_prompt.md` for direct reuse in future conversations.
- `docs/visual_style_guide.md` for image generation continuity.
- `docs/content_strategy.md` for first-principles content positioning.
- `docs/source_and_compliance.md` for fact-checking and health/education compliance.
- `assets/ASSET_INDEX.md` to document the current visual reference set.

---

## [0.1.0] - 2026-07-01

### Added

- Initial skill package for BGI science hotspot translation.
- `SKILL.md` main instruction file.
- Templates for Xiaohongshu copywriting, image planning, and workflow QA.
- Three worked examples: whale fall, muscle loss, and JUNO.
- Fifteen visual reference images.
