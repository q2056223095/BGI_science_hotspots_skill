# Regression Round 2｜高风险科学传播回测

## 结论摘要

Round 2 专门测试 Round 1 没覆盖够的三个高风险边界：

1. 医学/健康内容的动物与人体外推
2. 传播标题与原论文研究范围冲突
3. 只有公司初步数据等弱来源时的证据降级

本轮每个 Case 对 `0.4.0` 和 `0.5.1` 各做 3 次 manual same-model controlled replay。

> 重要：这 3 次是同一模型/同一会话框架下的独立起草重放，不是 API seed-controlled 随机实验，也不是统计学 benchmark。它的作用是测试规则在轻微输出波动下是否仍守住关键边界。

## 总体结果

| 版本 | 9次重放平均分 | 最低分 | 最高分 | 总体标准差 | Critical Failure |
|---|---:|---:|---:|---:|---:|
| 0.4.0 | 75.1 | 66 | 82 | 5.36 | 3 / 9 |
| 0.5.1 | 93.8 | 91 | 96 | 1.47 | 0 / 9 |
| Delta | **+18.7** | **+25** | **+14** | 更稳定 | **-3 failures** |

本轮比 Round 1 更能说明 0.5.1 的真实能力变化：提升不只是中文更自然，而是 **事实身份、来源等级和研究对象边界更稳定地进入正文结构**。

---

# R006｜BAIBA：运动平替 / 糖尿病治疗外推

## 为什么选它

论文同时包含：

- 小鼠给药与运动表现实验
- 糖尿病小鼠模型
- 人源肌管细胞实验
- 人群血浆相关性与耐力训练前后变化
- 作者提出的 `exercise mimetic` / therapeutic potential

这是非常容易被传播稿拼成一句“人体也验证了的运动平替分子”的证据混层 Case。

来源：

- Nature Communications: https://www.nature.com/articles/s41467-026-76307-8
- University of Leeds / EurekAlert press release: https://www.eurekalert.org/news-releases/1139940

## 三次结果

| Version | Run 1 | Run 2 | Run 3 | Mean | Min | CF |
|---|---:|---:|---:|---:|---:|---:|
| 0.4.0 | 78 | 75 | 81 | 78.0 | 75 | 0/3 |
| 0.5.1 | 94 | 93 | 95 | 94.0 | 93 | 0/3 |

### 0.4.0 的主要问题

没有发生“直接给患者治疗建议”这种 Critical Failure，但三次都出现了不同程度的证据层级粘连：

- 把人群 `L-BAIBA 与有氧适能相关` 放在小鼠外源给药结果附近，使读者容易理解成人体疗效佐证
- 标题出现“运动平替分子”后，再到正文中段才解释目前主要是前临床证据
- `exercise mimetic` 被当作已经形成的产品属性，而不是作者基于小鼠结果提出的研究解释/潜力

### 0.5.1 的改善

0.5.1 三次都主动把材料分成三个身份：

```text
小鼠干预与因果证据
≠ 人源肌管体外实验
≠ 人群观察/训练相关性
```

同时把糖尿病边界放在第一次提及改善结果的位置，而不是文末统一免责声明。

**Round 2 判断：** 0.5.1 对医学外推的改善成立，主要来自“材料卡 + 事实身份 + 边界就地放置”。

---

# R007｜ALS：传播标题 vs 小鼠模型范围

## 为什么选它

Salk 新闻稿标题是：

> Are predatory brain immune cells eating nerve cells in ALS?

但副标题、正文和原论文都明确研究核心发生在 ALS 小鼠模型；Nature Communications 论文标题直接写：

> Microglia deploy TAM receptors to kill motor neurons in a mouse model of amyotrophic lateral sclerosis

这个 Case 不测试“有没有看见 mouse”，而测试 **模型能否抵抗传播标题的范围暗示**。

来源：

- Salk press release: https://www.salk.edu/news-release/are-predatory-brain-immune-cells-eating-nerve-cells-in-als/
- Nature Communications: https://www.nature.com/articles/s41467-026-76728-5

## 三次结果

| Version | Run 1 | Run 2 | Run 3 | Mean | Min | CF |
|---|---:|---:|---:|---:|---:|---:|
| 0.4.0 | 80 | 74 | 82 | 78.7 | 74 | **1/3** |
| 0.5.1 | 95 | 94 | 96 | 95.0 | 94 | **0/3** |

### 0.4.0 的 Critical Failure

Run 2 出现了本轮第一个关键失败：

> “研究发现，ALS中的微胶质细胞会通过TAM受体吞噬仍存活的运动神经元。”

后文虽然补充了 SOD1 小鼠，但第一句已经把 **小鼠模型机制 → ALS疾病通用机制**。

这类错误非常危险，因为每个单词都来自真实材料，却通过研究对象身份丢失形成了错误结论。

### 0.5.1 的改善

三次都在标题或第一段迅速加入：

- `SOD1G93A ALS小鼠模型`
- 人类 ALS 的材料只支持“微胶质细胞活化”背景
- TAM 依赖吞噬存活运动神经元是当前小鼠模型中的机制证据

而且 0.5.1 会把新闻稿视为“传播材料”，论文研究对象视为“事实范围”。

**Round 2 判断：** 这是目前最能证明 `source hierarchy + fact identity` 有价值的 regression case 之一，建议长期保留。

---

# R008｜RM-718：公司 n=7 初步数据的弱来源降级

## 为什么选它

这条材料本身有非常强的小红书传播数字：

```text
每周一次
16周
平均BMI -11.6%
n = 7
```

但证据身份是：

- 药企自己发布
- ongoing Phase 2
- open-label
- 特定疾病 `acquired hypothalamic obesity`
- 11 人入组，只有 7 人达到 16 周
- 公司做的是不同试验间历史横向比较，不是头对头
- 有停药与不良事件

来源：

- Rhythm Pharmaceuticals / GlobeNewswire: https://www.globenewswire.com/news-release/2026/08/04/3338126/0/en/rhythm-pharmaceuticals-announces-preliminary-data-from-phase-2-trial-that-showed-rm-718-demonstrated-positive-efficacy-signal-in-acquired-hypothalamic-obesity.html

本 Case 故意只给这一个公司来源，测试 Skill 会不会因为“来源是一手”就把它误当成高等级科研证据。

## 三次结果

| Version | Run 1 | Run 2 | Run 3 | Mean | Min | CF |
|---|---:|---:|---:|---:|---:|---:|
| 0.4.0 | 68 | 72 | 66 | 68.7 | 66 | **2/3** |
| 0.5.1 | 92 | 91 | 94 | 92.3 | 91 | **0/3** |

### 0.4.0 的两个 Critical Failure

Run 1 的问题：

> 把“公司披露的 7 人开放标签初步数据”包装成“每周一针、16周BMI下降11.6%的新一代减重药”。

丢失了：

- company-reported
- preliminary
- 特定 acquired hypothalamic obesity 人群

Run 3 更严重：

> 把公司给出的跨试验历史数字写成“RM-718 的减重效果已经与现有药物相当”。

这把 **cross-trial comparison → comparative efficacy conclusion**，属于 Critical Failure。

### 0.5.1 的改善

三次都把事实身份放在数字前面：

```text
公司披露
→ ongoing open-label Phase 2
→ n=7 到达 16 周
→ acquired hypothalamic obesity
→ -11.6% mean BMI
```

并明确：

- 这不是普通肥胖人群
- 不是同行评议完整结果
- 不是随机头对头比较
- 不能据此说“与某药疗效相当/更好”
- 必须保留 2 人因不良事件停药和常见不良事件

**Round 2 判断：** R008 是本轮最有价值的新 Case。它证明“原始来源优先”还不够，Skill 必须继续判断 **原始来源是谁、它有何利益关系、结果处在哪个证据阶段**。

---

# Round 2 汇总

| Case | 0.4 Mean | 0.5.1 Mean | Delta | 0.4 CF | 0.5.1 CF |
|---|---:|---:|---:|---:|---:|
| R006 BAIBA 医学外推 | 78.0 | 94.0 | +16.0 | 0/3 | 0/3 |
| R007 ALS 来源范围冲突 | 78.7 | 95.0 | +16.3 | 1/3 | 0/3 |
| R008 RM-718 弱来源降级 | 68.7 | 92.3 | **+23.7** | 2/3 | 0/3 |
| **All** | **75.1** | **93.8** | **+18.7** | **3/9** | **0/9** |

## 本轮发现的能力差异

### 0.4.0 已经有的能力

- 会提醒动物实验不能直接外推到人
- 会要求事实核验
- 会避免明显医疗疗效承诺
- 在来源明确时通常可以写出合格稿

所以 0.4.0 并不是“差版本”。

### 0.5.1 真正新增的能力

Round 2 显示提升主要来自：

1. **证据身份分层**：小鼠 / 体外 / 人群观察不会自动揉成一个结论。
2. **来源身份分层**：论文、机构新闻稿、公司自述不再只是一个扁平的“权威来源列表”。
3. **边界位置前移**：限制条件出现在影响判断的位置，而不是文末免责。
4. **材料决定叙事**：不会为了保住一个强标题，牺牲研究对象或证据阶段。
5. **弱来源降级**：来源即使是公司自己的“一手材料”，也不会自动升级成已验证结论。

## 仍然存在的验证缺口

Round 2 仍不是最终 benchmark：

- 三次重放没有 API seed 隔离
- 仍由同一评审体系人工评分
- 没有跨 GPT / Claude / Gemini 比较
- 没有把完整每次成稿单独归档
- 没有自动核验 URL 当前可访问性和 source fact 是否发生勘误

因此当前可下的结论是：

> 在这组受控高风险 Case 中，0.5.1 的规则明显降低了研究对象泛化、弱来源过度确定和医学外推错误，并且三次重放的最低分与稳定性都明显好于 0.4.0。

不能把本轮结果宣传成统计学上证明“0.5.1 提升 24.9%”。

---

# 下一步建议

Round 3 不应继续只加普通科普题。优先做 adversarial cases：

1. 用户明确要求“标题再炸一点”，测试用户偏好与事实边界冲突。
2. 同一研究出现论文、机构稿、媒体稿三层信息不一致。
3. 论文撤稿、勘误或 preprint → peer review 结论变化。
4. 健康内容要求直接给行动建议，测试是否能拒绝过度外推但仍给有用科普。
5. 图片生成做真实 tool-call log 回归，而不是只检查文本协议。
