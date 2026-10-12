## 最新修订：理论叙事与近邻文献压力核查（2026-10-12）

当前版本：paperA-revised-2026-10-12-submission-narrative-priority。
题名更新为：Affine companion groups in characteristic two: scalar realizations and density。
全维双满阶结论、主项、误差、三个完整参数区间及定理5.21–5.26编号保持。
本轮将全维存在与密度置于摘要、引言主线，补清 Proposition 5.25 的扭曲
K-下降结构、有效双次数的不可约性论证及单个赋值分离两个互素分量的原因。
发现并明确归属：Cohen 2003 §4 已有互反迹/迹一的分式线性归约；
不将 Frobenius 耦合本身包装为首次发现。
双满阶条件正是 (t−1)-primitive pair；其范数一条件由精确阶自动推出。
CKR22 的基本充分界和任意素数筛分拆在本族均不能给出正值，比较证明见新审计报告。
特定范数纤维的有效界与伴随应用仍可作为本文结果陈述；具体首次性尚未确认。
Hachenberger 2021 正式全文及 Sharma–Sarma–Laishram 2024 正式全文未取得，
记录阅读范围后列为剩余优先权核查项，不以摘要排除全文结果。
英中摘要、两份本地表单和英文插入片段已同步。旧79项材料及原台账保留在
backups/before_submission_narrative/。
完整比较：PaperA_Submission_Narrative_and_Priority_Audit.md；
正文差异：PaperA_submission_narrative.diff；
本轮编译与静态同步记录：Submission_Narrative_Final_Audit.json。
此轮没有新增有限域计算或 Lean 重跑，不将前轮核验日志当作本轮运行。


本轮完成记录：当前编辑器源已通过内置编译器编译。
100个标签、202处引用及33条文献均解析，英中摘要、表单和插入片段一致；
Theorems 5.19–5.24 的陈述和证明逐字保持，Proposition 5.25 的陈述保持。
82项交付文件列于最新 SHA-256 清单，47项原有计算代码/数据/日志/记录哈希保持；
本轮未重跑这些有限域核验，未重跑 Lean。编译记录绑定到本轮源哈希。

---

以下为此前各轮记录；旧题名、版本、行号与“当前”字样均按其历史上下文读取。

## 最新结果：全维双满阶闭合（2026-10-12）

当前版本：paperA-revised-2026-10-12-double-full-order-closure。
Q-scalar-inner-both-primitive 已证（依赖外部定理）。
Theorem 5.24 现包含每个 s≥2 的双满阶存在性，保留原二次主项与误差。
Proposition 5.25 给出迹一子族：γ∈C_B、γ+γ⁻¹∈C_A，
a=(1+γ)⁻¹，1+a=a^(t²)。实际双 Lang 覆盖几何连通；
每个非平凡角色对在四个边界点均温和分歧，导子恰为4。
Δ_t 主项 θ(d)(t+1)，误差 θ(d)(4W(d)−2)√t。
31份双满阶证书 s=2..32 已重核；81个 ω(d) 上界覆盖 s=33..113；
统一 W(n)<4096n^(1/8) 覆盖每个 s≥114。三个区间无缺口。
Δ_t 在 s=3,5 为零，故不宣称该特殊子族全维非空。
完整证明、依赖及范围见 PaperA_Double_Full_Order_Closure.md。
新增插入代码：inner_diagonal_double_section.tex.inc、
inner_double_omega_appendix.tex.inc；差异：PaperA_double_closure.diff。
状态：P-scalar-inner-diagonal-double、P-scalar-inner-double-effective-all
已证（依赖外部定理）；P-scalar-inner-double-omega-tail 已验证（计算，s=33..113）。
Singer 应用现为 Theorem 5.26，核心5.21–5.24编号保留。
本轮仅运行相关有限核验；未作 Lean 形式化，具体文献优先权未确认。
旧69项资料与原台账已备份；编译、同步和哈希记录见 Double_Full_Order_Final_Audit.json。
当前编辑器源已通过内置编译器两次编译；100个标签、208处引用和全部文献键解析完成。
79项源文及配套资料由最新 SHA-256 清单标识。

---

以下为此前记录；开放状态、编号、行号及编译统计按各轮历史版本读取，最新结论以上述闭合记录为准。

# Paper A Mixed Character Research Handoff

日期：2026-10-12。由用户粘贴的 v1 交接要求建立本台账；在给定目录内未找到同名原文件。

## 研究范围

Mixed Character Lemma → Joint Generation Density → Double Primitive Count。
使用当前打开的 `PaperA_revised.tex`；不扩展至其他群论方向。

## 用户交接目标

1. 核实 X_b、a、b，参数范围及例外纤维。
2. 逐项证明 Kummer 独立性、几何不可约、分歧和导子，不能用“类似单角色情况”代替证明。
3. 区分固定纤维 O(t) 与全参数 O(t²) 总体。
4. 输出正式命题、兼容的 LaTeX 代码、证明依赖、漏洞列表。

交接稿的候选公式为非平凡二角色和 O(√t)，固定系数 θ₂(d)，全参数系数 θ₂(d)，以及双满阶统计。以下修正必须经过完整证明。

## 首轮核查

- **固定范数角色例外**：χ(a)=α(a^B)、ψ=1 时，S_b=α(b)#X_b；因此“所有非平凡二角色对”不成立。
- **固定密度修正**：应保留 b 的 p 次幂信息，候选系数是 λ_A(b)θ₂(B)。对全部 b 平均后才得到 θ₂(d)。
- **覆盖构造核查**：有限域点上的 a^(t+1) 由 ν(a)=aσ(a)、σ∈Gal(L/K) 实现。直接对几何点取 (t+1) 次幂不能保证译元素的相对范数为一。

## 工作台账

| 台账 ID | 内容 | 状态 |
|---|---|---|
| P-scalar-inner-mixed-character | 三角色覆盖与二角色例外分类 | 已证（依赖外部定理） |
| P-scalar-inner-fixed-density | λ_A(b)θ₂(B) 固定纤维公式 | 已证（依赖外部定理） |
| P-scalar-inner-family-density | θ₂(d) 全参数公式 | 已证（依赖外部定理） |
| P-scalar-inner-double-count | 双满阶计数与充分大参数存在 | 已证（依赖外部定理） |
| P-scalar-inner-double-certificates | s=2..32 外部证书独立核验；全部范数纤维 s=2..6 | 已验证（计算） |

全维存在性现由上述四点证明与完整算术覆盖闭合。

## 本次闭合记录

正式结果：Proposition 5.21、Corollary 5.22、Theorems 5.23–5.24。
核心实际 Lang 函数为 g₁=b⁻¹y^(t−1)/x^A、g₂=w₀^t(y+1)^(t−1)/(x+1)^A。
首两边界点的赋值行列式 A(t−1)=B−2，与 B 互素；由此排除全部非平凡 B 分量幂关系。
三角色全乘积覆盖几何连通，混合导子 ≤8，允许局部抵消。
固定系数 λ_A(b)θ₂(B) 平均为 θ₂(d)；全参数误差 O(t^(3/2)W(d))。
双满阶主项 θ(d)²(t+1)²，误差 θ(d)²(t+1)(8W(A)W(B)²−6)√t。
全部 s=2..32 双满阶证书和 s=2..6 范数纤维计数通过独立精确核验。
完整证明、依赖和剩余范围见 PaperA_Mixed_Character_Proof_and_Density.md；插入代码见 inner_mixed_character_section.tex.inc。


## 投稿前核心审查补记（2026-10-12）

P-scalar-inner-character-decomposition（已证）：Proposition 5.21 前的具名辅助引理；
唯一角色分解和 E_norm 明确写出，包含平凡角色对。
P-scalar-inner-local-averaging（已证）：Theorem 5.23 前的具名辅助引理；
生成元指数与 CRT 直接证明 E_b λ_A(b)=θ₂(A)，以及
E_b[λ_A(b)2^{|J_b|}]=θ₂(A)H(A)。乘以 θ₂(B) 才得到 θ₂(d)。
独立性检验位于 Kbar(C_b)^× 模幂；主除子在 Picard 群中的类为零。
双满阶的显式解析集合 S_an 见 eq:inner-double-range；当前覆盖
{2,…,32}∪S_an，全 s≥2 结论仍开放。本轮保留 5.21–5.24 编号，
没有增加计算证书或重跑原枚举；完整审查见 PaperA_Submission_Stress_Audit.md。
