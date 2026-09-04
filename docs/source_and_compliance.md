# Source and Compliance｜事实来源与合规规则

> 对应 Skill 版本：0.5.2

## 1. 两个不能混为一谈的问题

### Source Priority｜优先去哪里找

通常优先：

1. 原始论文 / 正式数据
2. 监管、政府、期刊或科研机构正式材料
3. 作者完整访谈与正式说明
4. 权威媒体科学报道
5. 其他二手报道

### Evidence Identity｜找到以后它能证明什么

**来源越原始，不等于结论权限越高。**

例如：

- 公司官方披露可以是一手来源，但仍是 `company_reported`。
- 预印本可以是原始研究，但仍未同行评议。
- 机构新闻稿可以准确，也可能在标题中扩大原论文范围。
- 一篇同行评议动物研究仍不能自动变成人体疗效证据。

因此所有重要 Claim 同时遵守：

```text
Source Identity + Evidence Subject + Study Design + Evidence Stage
→ Claim Type
→ Claim Ceiling
```

详细规则：`docs/evidence_identity_layer.md`。

---

## 2. 来源身份

建议内部标记：

- `peer_reviewed_primary`
- `preprint_primary`
- `regulator_or_government`
- `journal_or_institution`
- `author_statement`
- `company_reported`
- `authoritative_media`
- `secondary_media`

谨慎使用：

- 自媒体二次解读
- 没有来源的截图
- 只引用标题不看正文的内容
- 未标明原始研究的短视频或图文
- 只有“专家称”但无具体专家与出处的信息

如果只能找到二手报道，必须降低确定性；如果只有公司自述，必须保留公司归属和研究阶段。

---

## 3. 来源冲突

冲突常见为：

1. **事实冲突**：数字、对象、时间、方法不同。
2. **范围冲突**：传播标题比原论文研究范围更宽。
3. **解释冲突**：机构、作者展望或媒体解释比结果更强。
4. **阶段冲突**：传播材料称“突破”，原材料只是 preliminary / backtest / prototype。

处理：

```text
回到直接支持该 Claim 的原始材料
→ 保留更窄、更具体、更可验证的范围
→ 标记来源身份
→ 无法解决时明确不确定性
```

不要挑最适合传播的一条写死。

---

## 4. 科学表述

推荐按证据身份写：

- 研究观察到……
- 在该模型中……
- 与……相关
- 提供了机制线索
- 公司披露的初步数据显示……
- 回溯测试中……
- 当前仍处于原型 / 试点阶段
- 仍需要独立或更大规模验证

避免在证据不足时使用：

- 已经证明
- 一定会
- 可以治疗
- 能防癌
- 彻底逆转
- 完全推翻
- 已经优于 / 等同另一治疗
- 马上改变生活
- 人人适用
- 已经部署 / 已经落地

---

## 5. 健康 / 医学类内容

必须区分：

```text
动物
≠ 体外
≠ 人群观察
≠ 人体干预
```

如果存在人体干预，还要区分：

```text
single-arm / open-label
≠ randomized controlled trial
≠ head-to-head comparative trial
```

必须避免：

- 医疗诊断
- 个体化用药 / 补剂建议
- 治疗承诺
- 疾病恐吓
- 将动物模型直接外推到人
- 将体外实验直接写成人体结论
- 将人群相关性写成因果
- 将机制研究写成具体生活处方
- 将 company-reported preliminary signal 写成已证实疗效
- 将 cross-trial 历史数字写成优效 / 等效
- 暗示某种产品、课程、服务能解决疾病问题

建议健康类文案保留必要边界，但边界应放在影响判断的位置，而不是只放文末免责声明。

---

## 6. 科研发现类内容

必须避免：

- 用绝对语言描述初步研究
- 只引用二手传播但不核验核心事实
- 新闻标题覆盖原论文研究对象
- 把复杂成果讲成简单确定结论
- 为了传播效果牺牲准确性
- 把“可能”写成“已经”
- 把“观察到”写成“证明了”
- 把“修正认知”写成“彻底推翻”

必须做到：

- 核心事实尽量基于能直接支持该 Claim 的材料
- 论文类内容说明期刊、研究对象、核心发现和阶段
- 有不确定性时明确边界
- 使用符合 Claim Ceiling 的表达
- 让读者知道这项研究处在哪个阶段

---

## 7. 技术 / AI / 材料类内容

至少区分：

```text
prediction
→ experimental validation
→ prototype
→ pilot
→ operational deployment
```

必须避免：

- 把模型预测写成真实发现
- 把 backtest 写成已经在线运行
- 把实验室成果写成马上商业化
- 把 prototype / pilot 写成规模应用
- 夸大 AI 替代科学家的能力
- 把技术突破写成万能解决方案
- 用科幻画面暗示现实已经发生

必须说明：

- 技术解决了什么具体问题
- 原来的难点
- 当前证据阶段
- 局限和下一步验证

---

## 8. 自然 / 生态 / 地球科学类内容

必须避免：

- 过度拟人化
- 把生态关系写成童话
- 为了浪漫牺牲事实
- 把单一发现夸大成完整结论
- 无来源使用保护级别、地理归属、年代数字等敏感事实

必须做到：

- 说明证据来源
- 保留年代、地点、样本等关键信息
- 区分直接观察、间接证据、推测和研究意义

---

## 9. Evidence Laundering Critical Failures

以下不是“措辞不够谨慎”，而是关键事实错误：

- `animal / in vitro → human efficacy`
- `association → causation`
- `mouse model → human disease generalization`
- `company-reported preliminary → independently proven`
- `cross-trial → head-to-head efficacy`
- `preliminary / ongoing / preprint → mature conclusion`
- `prediction / backtest → deployment`
- `prototype / pilot → scaled application`
- 标题超过正文和证据的 Claim Ceiling

---

## 10. 图片来源与生成

如果直接使用论文 / 机构 / 新闻图片：

- 需要标注图源
- 注意版权与商用限制
- 不要裁掉原图出处
- 不要把他人图片伪装成 AI 生成图

更稳妥的做法：

- 基于论文信息科学重绘
- 保留科学结构，不直接搬运原图
- 使用“示意图”“科学重绘”“机制示意”等明确表达
- 不画真实患者、真实儿童或未经授权的个人肖像

图片里的数字、结论和标题同样遵守 Claim Ceiling。

---

## 11. 发布建议

健康类可以在需要时保留：

```text
内容基于公开科研材料整理，不作为个体诊疗建议。
```

科研类可以保留：

```text
内容基于公开研究和正式材料整理，具体结论以原始研究及后续验证为准。
```

技术类可以保留：

```text
相关成果仍处于研究、验证、原型或试点阶段，距离规模应用可能仍有距离。
```

免责声明不能修复正文中已经发生的 Claim Ceiling 越级。

---

## 12. 不建议出现的发布话术

- 看完震惊
- 所有人都该知道
- 不看后悔
- 彻底颠覆认知
- 已经被证明有效（证据不足时）
- 马上改变生活
- 这就是未来趋势
- 普通人赶紧照做

更好的做法是直接说明：

- 原始研究观察到了什么
- 证据发生在哪个对象 / 设计 / 阶段
- 哪一部分传播说法扩大了范围
- 当前最多允许得出什么结论
