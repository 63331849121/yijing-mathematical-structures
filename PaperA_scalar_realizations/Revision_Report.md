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

# Paper A 投稿前核心证明收紧

日期：2026-10-12。当前标识：paperA-revised-2026-10-12-submission-tightening。

## 本轮修改

- 增加 Character decomposition 具名辅助引理，写明 S_b 与 E_norm；
  两角色例外分类用集合内/外两类表述。
- 增加 Local averaging in a cyclic group 具名辅助引理；
  两个精确平均由生成元指数和 CRT 证明。
- 明确平均 λ_A 为 θ₂(A)，乘上 θ₂(B) 才得到 θ₂(d)。
- 明确 Kummer 独立性属于函数域乘法群模幂；八点赋值表已经位于正文。
- Theorem 5.24 明确解析集合 S_an 与已覆盖范围 {2,…,32}∪S_an；
  双满阶全维问题 Q-scalar-inner-both-primitive 仍开放。
- 摘要以密度结论开篇；引言补经典输入、贡献边界与范围。
  英中摘要、两份表单与全部正文插入片段同步。

P-scalar-inner-character-decomposition、P-scalar-inner-local-averaging
均先登记待核，纸面证明完成后更新为已证。原 5.21–5.24 保持编号和证明状态。
这些辅助事实是既有论证的明确化，不单列为新的原创贡献。
三种审稿视角的逐项核对、行号、反馈中两处数学错误及文献剩余项见
PaperA_Submission_Stress_Audit.md；不代表三名独立专家或期刊的意见。

修改前全部 66 项文件、原清单和台账已备份于
backups/before_submission_tightening/。本轮源文差异为
PaperA_submission_tightening.diff。编译和静态同步结果在
Submission_Tightening_Final_Audit.json 中记录。
本轮没有增加有限计算范围，也没有重跑旧算术核验器或 Lean。
当前源文已通过内置编译器两次编译；93 个标签、196 处引用解析完成，
摘要、两表单与正文片段同步。69 项当前文件由 SHA-256 清单标识。

---

## 以下为前轮修订记录

# Paper A 修订报告：混合角色与联合生成密度

日期：2026-10-12。前轮标识：paperA-revised-2026-10-12-mixed-character-density。

## 本轮结果与证明位置

| 台账 ID | 状态 | 当前论文位置 | 内容 |
|---|---|---|---|
| Q-scalar-inner-critical-all | 已证（依赖外部定理） | Theorem 5.20，thm:inner-all | 对所有 s≥2，k=2^s−1 可实现；斜率本身有精确阶 d |
| P-scalar-quartic-parametrization | 已证 | Proposition 5.15，prop:inner-quadratic | 完整二次参数化及奇数 s 的两个退化子域解 |
| P-scalar-inner-elliptic-fiber | 已证（依赖外部定理） | Lemmas 5.16–5.17，lem:inner-fiber / lem:inner-character | 光滑 genus 1 纤维、八个非有理边界点；Lang 角色的导子度数恰为 8 |
| P-scalar-inner-effective-bound | 已证（依赖外部定理） | Theorems 5.19–5.20 | 本原斜率主项及显式误差，全部 s≥33 的解析证明 |
| P-scalar-inner-finite-certificates | 已验证（计算） | 计算附录 app:inner-cert | s=2..32 的精确阶证书；s=2..6 的两种独立计数 |

完整数学证明、证明边界、文献、英文正文片段和研究计划见
`Research_Report_inner_critical.md` 的 Parts I–VI。

## 论文实际修改

在 §5 的 Paley 图解释之后补入五个结果及全部证明，给出 k=t−1 与
既有 k=t+1 非实现族的相邻对照。计算附录加入完整 31 行域塔表、
不可约性及素性验证规则，并列出核验后的五行 T_d、R_d 和本原斜率数。
新增数量记为 N_d^{prim}，避免与既有实现根集多项式 P_d 混淆。
摘要、引言、英文/中文摘要以及两个本地投稿表单均同步。
新增 Katz、Farashahi 等及 Kudo–Nogata 引文并明确经典方法的归属。

当前打开的源文件就地更新并经桌面内置编译器成功编译。
交叉引用、文献键、摘要同步与文件哈希另作静态核对。
已有原始投稿源保留；修改前恢复稿和配套资料存于
`backups/before_inner_critical/`。本轮差异文件为 `PaperA_inner_critical_update.diff`。

## 核验和限制

31 个证书由不导入搜索程序的独立验证器复核。素因子通过完整递归
Lucas 证书认证；不存在依赖 probable-prime 输出的证明步骤。
小维计数通过子群枚举与多项式 gcd / Möbius 方法相互验证。
有效常数以整数比较验证。新增结果未作 Lean 形式化；所需 Weil 界
是已发表经典外部定理。有限数据没有外推至无限维。

普遍的 k≤q^{1/4} 结论、两项同时满阶在所有 s≥2 的存在性
以及无有限计算构造仍未证明。联合生成临界渐近式和双满阶渐近式现已补证。文献优先权尚未确认。
本轮没有单独导出 PDF 或逐页进行视觉排版核对。

## 保留的前轮数学结果

结果 5.1–5.14 中的仿射群结构、作用判据、Möbius/Jacobi 筛、固定指数、
指数三阈值、定量密度、范数下降、1/4 障碍、本原分类与生成三角形均保留。
前轮修订报告及研究路线图完整备份，两个旧差异文件也保留。
当前全部复现文件由 PaperA_revised_sha256.json 标识。


## 外部审查意见合并（2026-10-12）

| 台账 ID | 状态 | 当前正文 | 修改和依据 |
|---|---|---|---|
| P-scalar-inner-explicit-lang-trace | 已证 | Lemma 5.17，eq:inner-lang-frobenius | 显式 F_Y 与 h 的兼容性；有理纤维 deck 乘子 a/u；几何 Kummer 方程与 K 下降分别说明 |
| P-scalar-inner-four-torsion | 已证（依赖外部定理） | Proposition 5.18，prop:inner-four-torsion | 四阶 K 有理平移、两个边界四点轨道、角色和实性和四整除；有理原点使用经典 Hasse–Weil 界 |
| P-scalar-inner-symmetry-certificates | 已验证（计算） | 计算附录 app:inner-cert；verify_inner_symmetry.py | 全部 s=2..32 的 31 个证书点；s=2..6 的全部本原范数纤维 |

本原斜率计数顺延为 Theorem 5.19，全维存在性为 Theorem 5.20，Singer 应用为 Theorem 5.25。
此前已证内容、数量主项、误差系数及 s≥33 的解析阈值保持有效。
引言增加五项文献；进一步补上 CK21 Remark 4.1 对增长 r 的讨论，避免仅靠“固定/增长指数”暗示优先权。CKR22 的正式刊物编号在比较报告中已校正。
四阶对称未被用于宣称 2√t 的角色界；所需独立导子或上同调分析仍未完成。
此次保留题名和总体章节组织；Weierstrass/j 模型及半直积覆盖的建议尚缺完整核验，没有写为新定理。

修改前全部 46 个配套文件及台账保存在 backups/before_review_merge/。
PaperA_review_merge.diff 给出相对于该保存版本的全部源文差异。
本轮实际重新运行两个相关核验器，完整日志、环境与数据均纳入当前 SHA-256 清单。
旧有其他核验器和 Lean 项目未在此轮重新运行。
详细审查回应及文献适用边界见 Review_Response_2026-10-12.md。

## Mixed Character → Density（当前更新）

| 台账 ID | 当前状态 | 论文位置 |
|---|---|---|
| P-scalar-inner-mixed-character | 已证（依赖外部定理） | Proposition 5.21、Corollary 5.22 |
| P-scalar-inner-fixed-density | 已证（依赖外部定理） | Theorem 5.23、eq:inner-joint-fiber |
| P-scalar-inner-family-density / Q-scalar-inner-joint-count | 已证（依赖外部定理） | Theorem 5.23、eq:inner-joint-total |
| P-scalar-inner-double-count | 已证（依赖外部定理） | Theorem 5.24 |
| P-scalar-inner-double-certificates | 已验证（计算） | 双满阶 s=2..32；全部范数纤维计数 s=2..6 |

原“全部非平凡二角色”估计存在常值范数角色反例；已在正文准确分类。
构造 ν(z)=zσ(z) 的真正代数映射，逐项给出三个 Lang 方程、Frobenius 迹、
八点赋值表、同时 Kummer 独立性、几何连通性及 ≤8 的导子。
固定主系数为 λ_A(b)θ₂(B)，平均后为 θ₂(d)；全参数误差为
θ₂(d)A(8H(A)W(B)−6)√t+2r₀A。双满阶主项为 θ(d)²A²。
实际比例 R_d/T_d=θ₂(d)+O(W(d)/√t)。所有陈述附完整证明。
旧编号 5.1–5.20 保留，Singer 应用顺延至 5.25。
报告、片段、摘要、两表单与当前打开的论文同步；修改前全部文件另行备份。
本轮运行了新的相关算术核验器；旧有无关核验器和 Lean 没有重跑。
全 s≥2 双满阶仍开放，没有将有限证书与渐近范围之间的间隙隐藏。

当前更新已通过内置编译器两次编译；90 个标签、187 处引用及 31 项文献键核对完成。
66 个源文件和配套文件由更新后的 SHA-256 清单记录；本轮未单独导出 PDF。


## General article preprint proof-readiness pass (2026-10-12)

The existing article-class manuscript remains the general preprint master.
Its abstract now foregrounds scalar realization density, states the
fixed-fiber O(t) and full-family O(t^2) scales separately, and disclaims
priority for the standard exact-order primitive-pair formulation. The
introduction identifies the norm-fiber estimate and its exact local averaging
as the quantitative contribution; the existing Cohen, Hachenberger,
primitive-pair and classical-tool attributions remain in place.

The mixed-character proof now exhibits the inertia vectors at
(0,1) and (0,b^{-1}) and verifies directly that they generate
Z/A x Z/B x Z/B. The diagonal four-point proof now explains, using
gcd(2,A)=gcd(2t,B)=1 and gcd(A,B)=1, why every nontrivial character
ramifies at all four boundary points. These are proof-clarity changes; the
theorem bounds are unchanged.

The exact arithmetic rechecks and final compilation status are recorded in
PaperA_Preprint_Proof_and_Readiness_Audit_2026-10-12.md.

The final package check reran all 13 documented finite verification/export
steps against the revised generic article master; all passed and regenerated
data matched the updated manifest. The built-in LaTeX compiler also succeeded.
A scoped proof and readiness audit, including dependencies and remaining
submission work, is in PaperA_Preprint_Proof_and_Readiness_Audit_2026-10-12.md.
