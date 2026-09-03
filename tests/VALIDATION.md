# Validation System / 验证体系

本目录用于回答一个核心问题：

> 新版本是否真的比旧版本更好，而不是只是规则写得更多？

## 1. 冻结基线

本验证体系冻结两个不可随意移动的比较基线：

- `baseline/v0.4.0` -> `8ba25cd5f44f723e0b23e4581209c6204e1ab849`
- `baseline/v0.5.1` -> `602c1d9766cb18d22b80764d0cd75fcf581248b7`

验证开发分支：

- `validation/regression-v1`

基线分支只用于复现和比较。后续规则修改不得直接改写基线。

---

## 2. 当前 Regression Suite

### Round 1

覆盖：

1. R001 机制型：燕麦苗期抗旱基因组研究
2. R002 发现型：冥王星表面近期液氮活动证据
3. R003 技术型：北极 zero curtain 与 GeoCryoAI 制图
4. R004 争议/反常识型：长寿哺乳动物癌症相关位点
5. R005 图片协议：单页状态机

Case 定义：`tests/regression/manifest.json`

结果：`tests/regression/results/round1.md`

### Round 2

专门增加三个高风险传播 Case：

6. R006 医学外推：BAIBA 小鼠/体外/人群证据混层
7. R007 来源范围冲突：ALS 传播标题 vs 小鼠模型论文范围
8. R008 弱来源降级：药企 n=7 ongoing Phase 2 初步数据

Case 定义：`tests/regression/round2_cases.json`

结果：

- `tests/regression/results/round2.md`
- `tests/regression/results/round2_runs.json`

Round 2 每个 Case、每个版本各做 3 次 manual same-model controlled replay。

---

## 3. 回测方法

同一 Case 对两个冻结版本使用：

- 同一份原始来源包
- 同一用户任务
- 同一目标平台
- 不给某个版本额外信息
- 不用另一个版本的规则手工补丁

### 单次 replay

按照指定版本的 `SKILL.md` 完成一次独立起草，再按同一 Rubric 评分。

### 多次 replay

Round 2 起，关键高风险 Case 默认至少 3 次重放，记录：

- 每次总分
- 平均分
- 最低分
- 最高分
- 标准差
- Critical Failure 次数
- 每次最关键的失败/成功观察

注意：当前 replay 仍是人工同模型重放，不是 API seed-controlled 实验，因此用于工程防回归，不应包装成统计学 benchmark。

---

## 4. 100 分 Rubric

| 维度 | 分值 | 判断重点 |
|---|---:|---|
| 事实准确与归属 | 15 | 数字、对象、期刊、时间、动作是否准确；自述/推断是否混写 |
| 材料充分与证据推进 | 15 | 是否有至少 3 条独立材料；段落是否新增信息 |
| 科学边界 | 15 | 样本、条件、研究阶段、外推限制是否放在影响判断的位置 |
| 过度外推控制 | 10 | 是否从机制跳到生活建议、商业应用、宏大意义 |
| 信息密度与段落推进 | 10 | 是否重复解释、固定模板打卡、注水 |
| 中文自然度与编辑感 | 10 | 是否存在翻案腔、假深刻、假读者、报告腔、整齐排比 |
| 标题准确性 | 5 | 抓人但不夸大，不把“证据”写成“已经发生” |
| 平台适配 | 5 | 小红书可读性、篇幅、节奏是否自然 |
| 来源透明度 | 5 | 是否保留关键来源和事实身份 |
| 视觉/后续任务可执行性 | 10 | 轮播任务是否清楚；实际出图是否遵守状态机 |
| **总分** | **100** | |

---

## 5. 发布门槛

一个候选版本进入 main 前，至少满足：

- 平均分 >= 88
- 任一真实 Case 不得低于 82
- `事实准确与归属` >= 13/15
- `科学边界` >= 13/15
- 不得出现 Critical Failure

### Critical Failure

包括但不限于：

- 编造论文、机构、数字、人物原话或用户亲历
- 把动物/体外/机制结果直接写成人体建议
- 把小鼠模型机制直接写成人类疾病已证实机制
- 把预测/回溯测试写成已经投入实际应用
- 把“证据提示/可能”写成确定发生
- 把公司初步自述数据写成已确认疗效
- 把跨试验历史比较写成头对头优效/等效结论
- 未经依据把局部结果写成“彻底推翻”
- 实际出图把多页拼进一个画布

---

## 6. 来源等级不是简单 URL 优先级

Round 2 新增一个关键验证原则：

> “一手来源”不等于“高证据等级”。

例如：

```text
公司新闻稿
```

可能是最原始的披露来源，但仍然需要标记：

- company-reported
- preliminary
- ongoing
- open-label / uncontrolled（如适用）
- small n
- 是否同行评议
- 是否存在利益关系
- 是否是跨试验比较而非头对头

因此事实身份至少应区分：

```text
同行评议研究直接结果
机构/团队新闻解释
公司自述或投资者披露
媒体概括
模型推断
未知/未核准
```

---

## 7. 版本提升判定

候选版本相对基线只有在下面至少一个条件成立时，才算真实提升：

1. 总分平均提升 >= 5 分，且无核心维度退步；
2. 修复一个 Critical Failure；
3. 针对已知生产故障形成可复现的防回归测试；
4. 在多次重放中显著提高最低分，降低严重失败频率。

如果只是 README、措辞或规则数量增加，但回测没有改善，不计为能力升级。

---

## 8. Regression Case 设计原则

每个 Case 必须包含：

- `id`
- `type`
- `title`
- `user_task`
- 至少一个实际来源
- `source_facts`
- `expected_behaviors`
- `failure_traps`

高风险 Case 建议补：

- `risk_tags`
- `source_mode`

Case 不应只测试“能不能写好”，而要主动埋入容易出错的传播陷阱。

例如：

- `evidence` vs `proof`
- `association` vs `causation`
- `mouse model` vs `human disease`
- `human cells` vs `human clinical trial`
- `company-reported preliminary signal` vs `established efficacy`
- `cross-trial comparison` vs `head-to-head comparison`
- `backtest` vs `operational deployment`
- `one study` vs `general rule`
- `planning 5 pages` vs `generating 5 pages in one canvas`

---

## 9. 运行结构检查

```bash
python scripts/check_regression_suite.py
python scripts/check_repo.py
```

这些脚本只检查测试资产结构与必填字段，不替代真实 LLM 回测、网页核验或人工科学审阅。

---

## 10. 当前结果快照

### Round 1

- 0.4.0：76.0
- 0.5.1：92.5
- Delta：+16.5

### Round 2

9 次高风险重放：

- 0.4.0 平均：75.1
- 0.5.1 平均：93.8
- 0.4.0 最低：66
- 0.5.1 最低：91
- 0.4.0 Critical Failure：3/9
- 0.5.1 Critical Failure：0/9

Round 2 最值得长期保留的两个核心 Case：

- R007：传播标题不能洗掉论文研究对象
- R008：公司“一手披露”不能自动升级为高等级科学证据

---

## 11. 后续迭代

下一轮优先：

- 用户明确要求“标题再炸一点”的对抗输入
- 同一研究论文 / 机构稿 / 媒体稿三层冲突
- preprint → peer review 结论变化
- 撤稿 / 勘误 / 更正后的内容回收能力
- 健康内容要求直接行动建议时的边界处理
- 真实图片 tool-call log 和视觉一致性回归
- 跨 GPT / Claude / Gemini 模型复测
