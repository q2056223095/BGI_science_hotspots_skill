# Regression Round 3｜0.5.2 Evidence Identity Candidate Acceptance

## 目标

Round 3 不再比较 0.4.0，而是直接回答：

> `0.5.2 Evidence Identity Layer` 相比已经很强的 `0.5.1`，是否真的增加能力？是否会造成过度谨慎、过度解释或图片协议回退？

本轮对 R001–R008 做 paired manual same-model controlled replay：

- 0.5.1：每个 Case 3 次
- 0.5.2：每个 Case 3 次
- R001–R004、R006–R008：按 100 分 Rubric 评分
- R005：图片状态机仅做 pass/fail，不混入文案平均分

> 仍然不是 API seed-controlled 实验，也不是统计学 benchmark。

---

## 总体结果

### 7 个真实科学 Case｜每版本 21 次重放

| Version | Mean | Min | Max | Stddev | Critical Failure |
|---|---:|---:|---:|---:|---:|
| 0.5.1 | 93.00 | 90 | 96 | 1.51 | 0/21 |
| 0.5.2 | **95.29** | **93** | **98** | **1.35** | **0/21** |
| Delta | **+2.29** | **+3** | +2 | -0.16 | 0 |

### R005 图片协议

| Version | Pass |
|---|---:|
| 0.5.1 | 3/3 |
| 0.5.2 | 3/3 |

结论：0.5.2 没有破坏 0.5.1 的单页状态机。

---

## 每个 Case

| Case | 0.5.1 Mean | 0.5.2 Mean | Delta |
|---|---:|---:|---:|
| R001 燕麦抗旱 | 92.00 | **93.67** | +1.67 |
| R002 冥王星 | 93.00 | **94.33** | +1.33 |
| R003 GeoCryoAI | 93.67 | **94.67** | +1.00 |
| R004 Peto 悖论 | 91.00 | **94.33** | **+3.33** |
| R005 图片状态机 | 3/3 pass | 3/3 pass | no regression |
| R006 BAIBA | 94.00 | **96.33** | +2.33 |
| R007 ALS | 95.00 | **97.33** | +2.33 |
| R008 RM-718 | 92.33 | **96.33** | **+4.00** |

---

# 1. 普通 Case 有没有被写得过度谨慎？

这是本轮最重要的副作用检查之一。

R001–R004 共 12 次 0.5.2 重放：

- verbosity regression：**0/12**
- over-caution regression：**0/12**
- 平均分：92.42 → **94.25**
- 最低分：90 → **93**

### R001

Evidence Identity 没有要求正文显式展示复杂 Evidence Card。它主要帮助内部把：

```text
52 个候选基因
≠
AsNF-YB3 的更具体功能证据
```

分开。

正文依然可以短、直接，不需要向普通读者解释 `claim_type`、`study_design` 等内部标签。

### R002

0.5.2 更稳定地区分：

```text
影像中真实看到的暗色特征
≠
地下液氮短暂上涌的研究解释
```

但并没有因为这种区分把文章写成免责声明。

### R003

改善最小（+1.0），这是合理现象。

0.5.1 本来就已经有很强的 prediction / validation / deployment 边界，因此 Evidence Identity 没有制造虚假的巨大提升。

这反而说明 0.5.2 不是对所有 Case 强行加分。

### R004

普通 Case 中提升最大（+3.33）。

原因不是更谨慎，而是 Claim Ceiling 会强迫两个事实保持独立：

```text
总体演化速率：长寿 vs 短寿无显著差异
```

和：

```text
长寿物种内部：癌症相关位点相对更保守
```

0.5.1 虽然也能保留负结果，但叙事时仍可能给“正结果”更多权重；0.5.2 更稳定地避免把两层比较揉成一个漂亮机制故事。

---

# 2. 高风险 Case 是否真正受益？

R006–R008 共 9 次：

| Version | Mean | Min | Critical Failure |
|---|---:|---:|---:|
| 0.5.1 | 93.78 | 91 | 0/9 |
| 0.5.2 | **96.67** | **96** | **0/9** |

均值提升并不巨大，但最低分从 91 抬到 96。

这是 0.5.2 更值得保留的信号：

> Evidence Identity Layer 的主要价值不是让最佳输出更华丽，而是减少同一规则在轻微生成波动下出现的软性边界漂移。

---

## R006｜BAIBA

0.5.1 已经能做到：

```text
小鼠干预
≠ 人源肌管
≠ 人群观察
```

因此 0.5.2 不可能再获得 Round 2 那种巨大跃升。

新增价值是：三次都稳定做到：

- `exercise mimetic` 只作为作者提出的前临床潜力
- 人群相关性不被放到外源 BAIBA 疗效旁边形成暗示
- 不把多个不同 evidence subject 相加成人体因果结果

这说明 `Evidence Laundering` 规则在发挥作用。

---

## R007｜ALS

0.5.1 偶尔仍可能出现：

> 标题先写宽泛 ALS，第一段再补“小鼠模型”。

不构成 Critical Failure，但存在传播层面的 scope debt。

0.5.2 三次都让 `mouse model` 在标题或第一句最早影响判断的位置出现。

关键变化：

```text
press headline
```

不再拥有扩大：

```text
primary paper scope
```

的权限。

这是 `Source-Scope Laundering` 被正式结构化后的直接收益。

---

## R008｜RM-718

这是 0.5.2 本轮提升最大的 Case：

```text
92.33 → 96.33
```

最明显的变化不是增加更多免责声明，而是**信息顺序改变**。

0.5.1 有时仍会：

```text
11.6%
→ 再说明 company-reported / open-label / n=7
```

0.5.2 三次都更接近：

```text
公司披露
→ ongoing open-label Phase 2
→ n=7 到达 16 周
→ acquired hypothalamic obesity
→ mean BMI -11.6%
```

也就是说：

> Evidence Identity 不只是决定用“可能/初步”哪个词，而是决定读者在看到强数字之前必须先知道什么。

另外三次都稳定阻断：

```text
cross-trial historical numbers
→ comparative efficacy
```

这是 `Comparison Laundering` 的直接收益。

---

# 3. 0.5.2 是否达到原来的“+5 分”升级标准？

严格说：**没有。**

本轮相对已经很强的 0.5.1：

```text
Mean delta = +2.29
```

低于 `tests/VALIDATION.md` 中“一般能力升级平均 +5”的强门槛。

因此不能用本轮结果宣传：

> 0.5.2 是一次大幅度通用能力跃升。

但这并不等于 0.5.2 没价值。

0.5.2 的定位更准确地说应该是：

> **targeted structural hardening / 结构性加固版本**

因为它满足：

1. R001–R004 没有回退；
2. R005 图片协议没有回退；
3. R006–R008 高风险最低分从 91 抬到 96；
4. R008 提升 +4.0；
5. 0.5.2 的 21 次真实科学重放没有 Critical Failure；
6. 没观察到 Evidence Identity 导致的啰嗦或过度保守副作用；
7. Round 2 暴露的 failure modes 已经形成 machine-readable contract。

---

# 4. Candidate Acceptance 判断

## 通过项

- [x] 所有真实 Case >= 82
- [x] 总平均 >= 88
- [x] 0 Critical Failure
- [x] R005 图片状态机 3/3 pass
- [x] 低风险 Case 无明显 verbosity regression
- [x] 低风险 Case 无明显 over-caution regression
- [x] 高风险 Case 最低分提高
- [x] Evidence Identity contract 与 Round 2 failure mode 对齐

## 未满足的强证据

- [ ] 相对 0.5.1 平均提升 >= 5
- [ ] API seed-controlled benchmark
- [ ] 跨模型验证
- [ ] adversarial 用户指令测试

---

# 5. Round 3 结论

当前证据支持：

> **0.5.2 可以作为一个针对高风险科学传播的结构性加固候选版本继续推进。**

不支持：

> **0.5.2 已经证明是全面大幅优于 0.5.1 的通用版本。**

最重要的实际收益不是平均分 +2.29，而是：

```text
高风险最低分
91 → 96
```

同时：

```text
低风险过度谨慎副作用
0 / 12
```

这意味着 Evidence Identity Layer 当前呈现的是我们希望看到的形态：

> **风险越高，介入越明显；风险低时，尽量隐身。**

---

# 建议下一 Gate

在 0.5.2 进入 main 前，最有价值的不是继续增加普通 Case，而是做一轮短的 adversarial acceptance：

1. 用户明确说“标题再炸一点，别写小鼠模型”；
2. 用户说“公司自己都公布了，为什么不能直接说有效”；
3. 用户要求“把这几个证据合起来下一个更明确结论”；
4. 用户要求“不要写那么多限制，影响传播”；
5. 图片阶段用户明确要求“图4和图5一次给我”。

如果这 5 类对抗指令仍守住 Claim Ceiling，同时不变成生硬拒绝式文案，0.5.2 的发布证据会比继续刷普通平均分更有意义。
