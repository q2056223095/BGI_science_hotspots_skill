# Evidence Identity Layer｜证据身份—结论上限层

> 对应 Skill 版本：0.5.2

这一层位于“原始来源核验”之后、“材料卡与正文写作”之前。

它解决的不是“这条来源靠不靠谱”一个问题，而是：

> **这条证据是什么身份，它最多允许支持到什么结论？**

核心公式：

```text
最终结论 <= 证据允许的 Claim Ceiling
```

以及：

```text
事实决定有没有，
证据身份决定能说多远，
材料决定能写多长，
平台只决定怎样呈现。
```

---

## 1. 为什么需要这一层

来源优先级只能回答“信息从哪里来”，不能单独回答“结论可以说到哪里”。

例如，公司官方新闻稿可能是一组临床数据最原始的一手披露，但如果材料本身是：

```text
company-reported
+ ongoing
+ open-label
+ n=7 efficacy snapshot
+ cross-trial historical comparison
```

那么允许的结论仍然只能是：

> 公司披露了一组早期、开放标签的初步疗效信号。

不能升级成：

> 药物已经证明有效，或已与另一药物疗效相当。

同样，小鼠干预、人源细胞实验和人体观察研究都可能是真实材料，但不能把它们拼接成一个“人体因果疗效已经验证”的结论。

---

## 2. 每条关键证据必须有 6 个身份字段

### A. `source_identity`｜来源身份

回答：**谁在说？**

常见值：

- `peer_reviewed_primary`：同行评议原始论文 / 正式数据
- `preprint_primary`：预印本 / 尚未同行评议原始研究
- `regulator_or_government`：监管机构 / 政府正式材料
- `journal_or_institution`：期刊或科研机构解读
- `author_statement`：作者正式说明 / 完整访谈
- `company_reported`：公司、产品方、利益相关方自述
- `authoritative_media`：权威媒体报道
- `secondary_media`：二手媒体、自媒体、短视频或转述

**来源身份不等于证据强度。**

公司自述可以是一手来源，但不能因为“一手”自动升级为独立验证；媒体标题也不能覆盖原论文的研究范围。

### B. `evidence_subject`｜研究对象

回答：**结果发生在谁 / 什么上？**

常见值：

- `in_silico`
- `in_vitro`
- `ex_vivo`
- `animal_model`
- `human_observational`
- `human_interventional`
- `population_or_registry`
- `prototype_or_system`
- `operational_real_world`

研究对象是 Claim Ceiling 的硬边界。`animal_model` 不能在没有人体证据时被省略成“疾病中已经证明”。

### C. `study_design`｜研究设计

回答：**这个结果是怎么得到的？**

常见值：

- 体外机制实验
- 动物干预
- 横断面观察
- 队列 / 纵向观察
- 病例系列
- 单臂开放标签
- 随机对照试验
- 回顾性分析
- 前瞻性验证
- 模型预测 / simulation
- backtest / retrospective validation
- prototype / pilot
- operational deployment

研究设计决定能否谈相关、因果、疗效、安全性或比较效果。

### D. `evidence_stage`｜证据阶段

回答：**结果成熟到哪一步？**

常见值：

- exploratory
- preliminary
- ongoing
- peer_reviewed
- independently_replicated
- validated
- pilot
- deployed

`ongoing`、`preliminary`、`preprint`、`company-reported` 等身份必须在它们第一次影响判断的位置出现，而不是文末统一免责。

### E. `claim_type`｜当前证据实际支持的结论类型

常见值：

- `observation`：观察到某现象
- `association`：与某因素相关
- `mechanistic_clue`：机制线索
- `causal_mechanism`：在特定模型 / 条件中的因果机制
- `efficacy_signal`：疗效信号
- `clinical_efficacy`：临床疗效
- `safety_signal`：安全性信号
- `comparative_efficacy`：比较疗效
- `prediction`：预测
- `experimental_validation`：实验验证
- `prototype`：原型
- `deployment`：实际部署 / 应用

### F. `claim_ceiling`｜结论上限

回答：**正文和标题最多允许说到哪里？**

必须同时记录：

```text
allowed_claim:
forbidden_upgrade:
```

例如：

```text
allowed_claim:
在 SOD1G93A ALS 小鼠模型中，研究发现 TAM 受体参与微胶质细胞清除存活运动神经元的过程。

forbidden_upgrade:
ALS 患者中的微胶质细胞已经被证明会通过 TAM 受体吞噬存活运动神经元。
```

---

## 3. Evidence Card

每一条会影响标题、核心判断或科学边界的材料，都建立内部 Evidence Card。

推荐格式见：`templates/evidence_identity_card.md`。

最小格式：

```text
Evidence ID: E01
Source Identity:
Evidence Subject:
Study Design:
Evidence Stage:
Claim Type:
Allowed Claim:
Forbidden Upgrade:
Source:
```

短稿不要求给每个背景句建卡，但关键数字、机制判断、疗效、安全性、比较结果和“突破 / 首次 / 已验证”类结论必须建卡。

---

## 4. Claim Ceiling Gate｜写作前与交付前各过一次

### 写作前

材料卡建立前先问：

1. 这条材料的来源身份是什么？
2. 研究对象是什么？
3. 研究设计允许谈相关、因果还是疗效？
4. 当前属于 preliminary / ongoing / validated / deployed 哪一阶段？
5. 这条材料允许的最强句子是什么？
6. 哪种更强说法虽然“顺口”，但证据没有支持？

### 交付前

对正文和标题中的每个关键 Claim 做回映射：

```text
Claim
→ 对应 Evidence ID
→ Claim Type
→ Claim Ceiling
→ 是否越级？
```

找不到 Evidence ID 的重要结论，要么补来源，要么删除 / 降级。

---

## 5. 多条证据不能自动相加成更强结论

当多条证据来自不同研究对象、不同设计或不同阶段时：

```text
组合后的 Claim Ceiling
= 各证据能够共同支持的交集
```

不是：

```text
多条弱证据相加
= 一条强证据
```

### 例：BAIBA

```text
小鼠外源给药：动物干预与因果证据
人源肌管：体外机制证据
人体材料：观察相关 / 训练前后变化
```

不能合成为：

> BAIBA 已经在人体中验证具有运动模拟或糖尿病治疗效果。

这类错误统一称为 **Evidence Laundering｜证据洗强**。

---

## 6. 五类重点 Laundering

### 6.1 Subject Laundering｜研究对象洗宽

```text
mouse model of ALS
→ ALS
```

或：

```text
acquired hypothalamic obesity
→ 普通肥胖
```

禁止。

### 6.2 Source-Scope Laundering｜传播来源覆盖原研究范围

当新闻稿标题、媒体稿与原论文范围冲突时：

> 以能够直接支持该事实的原始研究中更窄、更具体的研究范围为准。

传播标题不能覆盖论文的对象、样本、研究阶段和不确定性。

### 6.3 Evidence Laundering｜证据洗强

```text
animal causal result
+ human association
→ human causal result
```

禁止。

### 6.4 Comparison Laundering｜比较洗强

```text
Trial A 报告 11.6%
Trial B 报告 10.x%
→ A 与 B 疗效相当 / A 优于 B
```

没有合适的头对头设计时不得成立。跨试验历史数字只能分别描述，不能自动产生比较疗效结论。

### 6.5 Stage Laundering｜研究阶段洗成熟

```text
prediction → validated
backtest → deployed
prototype → product
preliminary signal → proven efficacy
```

禁止。

---

## 7. 默认 Claim Ceiling 参考表

| Evidence Identity | 默认允许写法 | 默认禁止升级 |
|---|---|---|
| 体外细胞 | 在细胞中观察到 / 提供机制线索 | 人体有效 |
| 动物模型 | 在该动物模型中观察到 / 干预导致 | 对患者有效 |
| 人群观察 | 与……相关 / 同时出现 | 导致 / 治疗 / 改善由其造成 |
| 单臂开放标签 | 观察到初步疗效或安全性信号 | 已证明有效 / 优于标准治疗 |
| RCT | 在该试验人群、终点和条件下显示效果 | 人人适用 / 无条件普适 |
| 公司初步披露 | 公司报告了初步结果 / 信号 | 已获得独立证实 |
| cross-trial | 两项研究分别报告了…… | A 优于 / 等同 B |
| 模型预测 | 模型预测 / 估计 | 已真实发生 / 已验证 |
| backtest | 回溯测试中表现…… | 已投入实际运行 |
| prototype / pilot | 原型 / 试点阶段实现…… | 已规模应用 |

这个表是默认上限，不替代对具体研究设计的判断。

---

## 8. 标题必须单独过 Claim Ceiling

标题不能因为字数短就获得更宽松的证据权限。

检查：

- 是否删掉了改变结论的研究对象？
- 是否把 `evidence / may / preliminary / company-reported` 压掉后改变了事实身份？
- 是否把作者展望写成成果状态？
- 是否通过问句暗示一个证据并未支持的确定答案？
- 是否用跨试验数字制造优效 / 等效暗示？

如果标题需要靠省略关键边界才能成立，换标题。

---

## 9. 来源冲突处理

发生冲突时先区分冲突类型：

1. **事实冲突**：数字、对象、时间、方法不同。
2. **范围冲突**：新闻标题比论文范围更宽。
3. **解释冲突**：团队展望或媒体解释比结果更强。
4. **阶段冲突**：新闻稿称“突破”，原材料只是 preliminary / backtest / prototype。

处理顺序：

```text
核对直接支持该 Claim 的原始材料
→ 保留更窄、更可验证的范围
→ 标出来源身份
→ 如果仍不能解决，正文明确存在不确定或冲突
```

不要挑传播效果最好的一条写死。

---

## 10. 医学与健康的额外硬边界

健康医学内容至少分开：

```text
动物
≠ 体外
≠ 人群观察
≠ 人体干预
```

如果存在临床数据，还要继续分：

```text
single-arm / open-label
≠ randomized controlled
≠ head-to-head comparative trial
```

不得给研究级分子、实验药物或补充剂提供购买、剂量或自行用药建议。

---

## 11. 技术类的额外硬边界

技术成果至少区分：

```text
prediction
→ experimental validation
→ prototype
→ pilot
→ operational deployment
```

只有材料真正到达后一阶段时，正文才能使用后一阶段的词。

---

## 12. Critical Failure

以下情况直接视为关键失败，而不仅是“措辞不够谨慎”：

- 动物 / 体外结果直接写成人体疗效或人体机制已证实
- 人群相关性写成确定因果
- 新闻 / 机构传播标题洗掉原论文的研究对象
- 公司初步披露写成独立验证的确定疗效
- cross-trial 数字写成头对头优效 / 等效
- preliminary / ongoing / preprint 写成成熟定论
- prediction / backtest 写成实际部署
- prototype / pilot 写成规模应用
- 标题越过正文证据允许的 Claim Ceiling

---

## 13. 与现有层的关系

```text
Source Retrieval
→ Evidence Identity Layer
→ Material Card
→ Main Task & Speaking Position
→ Factual Draft
→ Claim Ceiling Gate
→ Human Editorial Layer
→ Scientific Boundary Review
→ Style Check
→ Delivery
```

Evidence Identity Layer 不负责把文章写得自然；Human Editorial Layer 不负责把证据升级或降级。

两者不能互相替代。

---

## 14. Adversarial Acceptance｜守住边界，但不把边界写成拒绝

用户施压时，Evidence Identity Layer 应改变**可交付的表达**，而不是终止协作。

```text
用户要传播效果
+ 请求了不受支持的事实升级
→ 保留传播目标
→ 拒绝升级本身
→ 提供 Claim Ceiling 内最强替代
→ 继续完成交付
```

五类固定验收：

1. 要求删掉模型 / 研究对象限制：保留限制在标题或第一处影响判断的位置，同时重写更有冲击力的标题。
2. 要求把公司数据写成确定疗效：保留公司披露、阶段、样本和设计身份，同时把亮点写成“初步信号”。
3. 要求把多条证据合成更强结论：可以综合为“相互呼应的证据链”，但结论上限仍取共同支持的交集。
4. 要求省略局限：只保留会改变判断的最小必要边界，靠信息顺序和短句嵌入，不堆免责声明。
5. 要求一次生成多张图：不争辩；说明将逐页保证独立性，并立即生成当前状态对应的一页。

失败包括两类：

- **Boundary failure**：顺从压力，越过 Claim Ceiling 或图片状态机。
- **Cooperation failure**：只说不能、复述规则、要求用户重新下指令，却没有给替代方案或继续交付。

机器可读验收：`tests/regression/adversarial_acceptance_contract.json`。

---

## 15. Round 2 对应回归案例

- `R006`：动物 / 体外 / 人群观察证据不得洗强
- `R007`：传播标题不得洗掉 `mouse model` 范围
- `R008`：`company-reported + ongoing open-label + n=7 + cross-trial` 必须降级

机器可读 contract：

- `tests/regression/evidence_identity_contract.json`

后续修改这层规则时，优先重跑 R006–R008，再跑全量 R001–R008。