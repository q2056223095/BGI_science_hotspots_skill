# Evidence Identity Card｜证据身份工作卡

> 对应 Skill 版本：0.5.2

这张卡在写正文前内部使用，不要求原样展示给用户。

核心目的：

```text
先确定证据身份
→ 再确定 Claim Ceiling
→ 最后才决定标题和正文能怎么说
```

---

## 1. 单条 Evidence Card

```text
Evidence ID: E01

Source Identity:
- peer_reviewed_primary / preprint_primary / regulator_or_government
- journal_or_institution / author_statement / company_reported
- authoritative_media / secondary_media

Source:

Evidence Subject:
- in_silico / in_vitro / ex_vivo / animal_model
- human_observational / human_interventional
- population_or_registry / prototype_or_system / operational_real_world

Study Design:

Evidence Stage:
- exploratory / preliminary / ongoing / peer_reviewed
- independently_replicated / validated / pilot / deployed

Claim Type:
- observation / association / mechanistic_clue / causal_mechanism
- efficacy_signal / clinical_efficacy / safety_signal
- comparative_efficacy / prediction / experimental_validation
- prototype / deployment

Directly Supported Fact:

Allowed Claim:

Forbidden Upgrade:

Important Limitation:

Conflict / Competing Source:

Used In:
- title / paragraph / carousel page / boundary only
```

---

## 2. 多证据总表

| ID | Source Identity | Subject | Design / Stage | Claim Type | Allowed Claim | Forbidden Upgrade |
|---|---|---|---|---|---|---|
| E01 |  |  |  |  |  |  |
| E02 |  |  |  |  |  |  |
| E03 |  |  |  |  |  |  |
| E04 |  |  |  |  |  |  |
| E05 |  |  |  |  |  |  |

---

## 3. Claim Ceiling Gate

正文初稿完成后，把关键句反向映射：

| Claim | Evidence ID | 是否在 Claim Ceiling 内 | 处理 |
|---|---|---|---|
|  |  | Yes / No | 保留 / 降级 / 删除 / 补来源 |
|  |  | Yes / No |  |
|  |  | Yes / No |  |

以下内容必须逐条过 Gate：

- 标题核心判断
- 关键数字
- 因果 / 机制判断
- 疗效 / 安全性判断
- “首次 / 突破 / 已验证 / 已应用”
- 比较优效 / 等效判断
- 从动物、体外或人群观察外推到人的句子

---

## 4. Laundering 快速检查

- [ ] `mouse model → disease in humans`？
- [ ] `in vitro → human effect`？
- [ ] `association → causation`？
- [ ] `company-reported → independently proven`？
- [ ] `cross-trial → head-to-head comparison`？
- [ ] `preliminary / ongoing → proven`？
- [ ] `prediction / backtest → deployment`？
- [ ] `prototype / pilot → scaled application`？
- [ ] 新闻标题是否比论文研究范围更宽？
- [ ] 多条弱证据是否被拼成一个更强、任何单条都不支持的结论？

任意一项为 Yes，回到 Evidence Card 重写 Claim Ceiling。