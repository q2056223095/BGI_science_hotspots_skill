# 0.5.2 Release Notes

## Evidence Identity & Claim Ceiling

0.5.2 在写作前为关键证据建立身份，并规定每条证据最多允许支持到什么结论：

```text
最终结论 <= 证据允许的 Claim Ceiling
```

新增六个 Evidence Identity 字段、Claim Ceiling Gate，以及 Subject、Source-Scope、Evidence、Comparison、Stage 五类 Evidence Laundering 检查。

## Cooperative Boundary Response

发布前五项 adversarial acceptance 暴露了一个重要交互缺口：守住边界不能等于停止帮助。

当用户要求删掉研究对象、夸大公司数据、把多条弱证据洗成强结论、省略关键限制，或一次生成多页图片时，0.5.2 现在要求：

1. 保留用户合法的传播或生产目标；
2. 用一句话指出不能采用的事实升级；
3. 给出 Claim Ceiling 内最有力度的替代；
4. 直接继续完成交付。

“只说不能、不给替代、不继续任务”现在被定义为 Cooperation Failure。

## Validation

- Round 3：0.5.2 在21次真实科学案例重放中均分95.29，最低93，0 Critical Failure。
- 高风险 R006–R008：最低分从0.5.1的91提高到96。
- 低风险 R001–R004：未观察到啰嗦或过度谨慎回退。
- Adversarial final gate：五类压力在 Boundary 与 Cooperation 两条轴上均通过。
- R005 单页图片状态机保持不变。

这些结果来自 manual same-model replay 与 specification-level adversarial review，不是 seed-controlled 或统计学 benchmark。0.5.2 的准确定位是 **targeted structural hardening**，不是全面能力跃升。

## Upgrade Notes

现有0.5.1图片协议无需迁移：仍按 P1确认后逐页生成，且一次调用只生成一个独立画布。内容工作流新增 Evidence Identity Table、Claim Ceiling Gate 与 Cooperative Boundary Response。

## New assets

- `docs/evidence_identity_layer.md`
- `templates/evidence_identity_card.md`
- `tests/regression/evidence_identity_contract.json`
- `tests/regression/adversarial_acceptance_contract.json`
- `tests/regression/results/adversarial_acceptance.md`
