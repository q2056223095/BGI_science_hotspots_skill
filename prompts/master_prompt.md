# 科学热点小红书科普转译总提示词

请使用 `BGI Science Hotspots Skill 0.5.2` 处理我提供的科学热点或材料。

## 目标

把科学新闻、论文成果或科研发现转化为：

```text
准确事实 + Evidence Identity + Claim Ceiling + 清楚解释 + 材料推进 + 有限判断 + 科学边界 + 小红书传播感
```

核心原则：

```text
先做科普，不做教育转化。
事实决定有没有，证据身份决定能说多远，材料决定能写多长，平台只决定怎样呈现。
最终结论 <= 证据允许的 Claim Ceiling。
```

除非我明确要求，不加入孩子、家长、课程、活动、机构品牌和报名信息。

## 执行顺序

1. 确认我要的交付。
2. 查找论文、期刊、机构等原始来源，并核准时间、对象、样本、方法、数字、结果和局限。
3. 对关键证据建立 Evidence Identity：`source_identity / evidence_subject / study_design / evidence_stage / claim_type / claim_ceiling`。
4. 为每条关键证据写 `Allowed Claim` 和 `Forbidden Upgrade`。
5. 建立材料卡。短稿至少 3 条独立材料，超过 1000 字至少 5 条；重要材料标记 Evidence ID。
6. 检查 Subject / Source-Scope / Evidence / Comparison / Stage Laundering。
7. 判断属于发现型、机制型、技术型或争议反常识型。
8. 确定本篇唯一主要任务和作者说话位置。
9. 生成事实初稿。
10. 执行 Claim Ceiling Gate：把标题和正文关键 Claim 回映射到 Evidence ID，越级则降级、删除或补来源。
11. 按 `docs/human_editorial_layer.md` 改稿。
12. 重新核对科学边界。
13. 按 `templates/anti_ai_self_check.md` 自查，必要时运行 `scripts/check_copy_style.py`。
14. 输出我指定的正文、标题、轮播图规划和图片提示词。
15. 如果我要“开始做图”，进入逐页实际生成流程。

## Evidence Identity｜必须执行

关键证据至少判断：

```text
Source Identity：论文 / 预印本 / 机构 / 作者 / 公司 / 媒体？
Evidence Subject：体外 / 动物 / 人群观察 / 人体干预 / 系统？
Study Design：观察 / 干预 / open-label / RCT / backtest / pilot？
Evidence Stage：preliminary / ongoing / peer-reviewed / validated / deployed？
Claim Type：观察 / 相关 / 机制 / 因果 / 疗效 / 比较 / 预测 / 应用？
Claim Ceiling：最多允许说到哪一步？
```

必须避免：

```text
mouse model → human disease
in vitro → human effect
association → causation
company-reported → independently proven
cross-trial → head-to-head comparison
preliminary / ongoing → proven
prediction / backtest → deployment
prototype / pilot → scaled application
```

多条不同身份的弱证据不能拼成一个任何单条证据都不支持的更强结论。

详细规则：

- `docs/evidence_identity_layer.md`
- `templates/evidence_identity_card.md`

## 写作要求

- 第一段尽快碰到对象、动作、结果、数字或问题。
- 每段必须增加新事实、新解释、新限制或新后果。
- 背景在读者需要时再出现。
- 材料不足就继续研究、缩小问题或缩短篇幅。
- 不虚构亲历、采访、读者反应、普通人故事和无来源精确细节。
- 作者声音来自材料取舍、信息来路和有限判断，不来自口头禅。
- 主语与动作尽早出现，减少名词化和连词堆叠。
- 不用表演性翻案腔、洞察路标、三项以上同构排比和空泛大词抬价。
- 科学纠偏必须对应真实存在的媒体说法、流行说法或旧结论。
- 边界放在会影响判断的位置，不在文末统一免责。
- 写到事情讲完就停，不重新摘要，不强行升华。

## 小红书正文

默认约 500 至 800 字。材料少时可以更短，材料足够时可以更长。

不要机械套固定六段式。根据材料选择一条主路径：

```text
事件推进
发生了什么 → 为什么 → 怎样确认 → 还有什么没确认

证据推进
结果或数字 → Evidence Identity → 改变哪处理解 → Claim Ceiling

核验推进
传播说法 → 原始研究 → 范围是否一致 → 成立部分 → 被放大部分

技术推进
原来卡点 → 新方法改哪一步 → 当前证据阶段 → 离应用还有多远
```

## 标题

标题最后取，并单独过 Claim Ceiling Gate。标题不能因为短而省略会改变结论的研究对象、证据阶段或来源身份。

避免震惊体、恐吓体、绝对承诺，以及没有真实误读依据的“你以为其实”。

## 轮播图规划

默认规划 5 张独立 3:4 轮播图：

1. P1 封面
2. P2 关键事实、背景或时间线
3. P3 证据、实验、装置或关键数据
4. P4 机制、比较或过程
5. P5 边界、待解问题或结论

每页只承担一个主要信息任务。轮播图中的标题、数字和比较同样受 Claim Ceiling 约束。

生成提示词前参考 `assets/ASSET_INDEX.md`、`docs/visual_style_guide.md` 和 `templates/image_generation_template.md`。

## 实际图片生成协议｜必须执行

轮播图规划和实际出图是两件事。

可以一次规划 P1–P5，但真正调用图片生成工具时，默认：

```text
一次只生成一张图。
一个画布只放一页。
每页都是独立 3:4 竖版。
```

首次说“开始做图”时：

```text
只生成 P1 封面
→ 停止
→ 等我确认
```

我确认封面后：

```text
继续 → 只生成 P2
继续 → 只生成 P3
继续 → 只生成 P4
继续 → 只生成 P5
```

即使我说“继续生成图2-图5”或“继续生成图4-图5”，默认也必须先只生成当前下一页，交付后停止。

除非我明确说“这次允许一次生成多张独立图片”，否则不要一次生成多张。

无论如何都禁止：

- 把 P2–P5 拼成一张图
- P4 + P5 双页合成
- 2×2 四宫格
- 上下双页
- 左右分屏模拟两页
- contact sheet
- 长图串联多页
- 一个画布出现多个页码

每次实际生成提示词开头必须写：

```text
只生成一张独立的 3:4 竖版小红书轮播图。
当前只生成 P{页码}。
一个画布只允许这一页，不得出现其他页码或其他页面内容。
禁止拼图、四宫格、双页、上下分屏、左右分屏、长图、多页总览和 contact sheet。
```

P1 一旦确认，P2–P5 必须继承封面的主色、背景、字体气质、标题层级、页码样式、卡片样式、图标风格、重点色和留白比例。

当前页生成完成后必须停止，把控制权交回给我。

如果返回结果不是独立 3:4、出现多页合成、多个页码、混入下一页内容或与封面视觉明显不一致，视为生成失败，应重新生成当前页，不要继续下一页。

## 默认交付

没有其他说明时，输出：

1. 事实核准摘要
2. 标题候选
3. 最终小红书正文
4. 5 张轮播图规划
5. 图片生成提示词
6. 必要边界与关键来源

Evidence Identity Table 和 Claim Ceiling Gate 默认内部执行，不把完整工作表展示给我；但 `company-reported / preliminary / mouse model` 等会影响判断的身份必须在正文对应位置体现。

我只要文案时，只交标题、正文和必要来源，不展示内部评分、Evidence Card、提纲和改稿过程。

我说“开始做图”时，不需要重复整套规划，直接按上述实际图片生成协议，从 P1 单页开始。