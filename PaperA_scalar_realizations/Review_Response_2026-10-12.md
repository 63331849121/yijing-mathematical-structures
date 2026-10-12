# Paper A：外部审查回应及合并记录

日期：2026-10-12。当前版本：paperA-revised-2026-10-12-lang-trace-four-torsion。

## 本轮采用的依据与边界

核查输入为 G:/下载 中的核验版源码、两份审计报告及三份粘贴总结。三份粘贴总结内容和 SHA-256 相同，按一份意见处理。供审查的 PDF 未在本轮逐页视觉检查；附件关于外部专家认可、页数和其他日志的陈述未作为本轮核验结论。
修改在当前编辑器的 PaperA_revised.tex 就地进行。修改前的源与全部 46 项复现资料先按哈希确认，并备份于 backups/before_review_merge/。

## 已合入的证明补充

| 台账 ID | 状态及正文位置 | 本轮完成事项 |
|---|---|---|
| P-scalar-inner-explicit-lang-trace | 已证；Lemma 5.17，eq:inner-lang-frobenius | 由 Lang 方程推出 F_Y，逐式验证 Kummer 方程兼容性；计算有理纤维 deck 元素 a/u |
| P-scalar-inner-four-torsion | 已证（依赖外部定理）；Proposition 5.18 | 给出 K 有理四阶平移、两个边界四点轨道、角色和实性与四整除；有理原点用 Hasse–Weil |
| P-scalar-inner-symmetry-certificates | 已验证（计算）；计算附录及新核验器 | 对 s=2..32 的 31 个证书点核查代数恒等式；对 s=2..6 穷尽全部本原范数纤维 |

令 h=y^t/x，u²=b。覆盖的 Frobenius 为

\[
F_Y(x,y,z_0)=(b/y^t,x^t,(x/u)z_0),
\qquad h(F_{C_b}(x,y))=(x/u)^B h(x,y).
\]

这是在几何分裂坐标中写出的、来自 K-定义 Lang 覆盖的下降。底点为 (a,a^t) 时，Frobenius 的纤维乘子恰为 a/u∈V，故迹函数是 χ(a/u)，逆 Frobenius 约定下取逆角色。八个分歧点的赋值现在按点列明；每个非平凡角色的导子仍恰为 8。

ρ(x,y)=(1/y,x/b) 满足 ρ²=(b/x,b^{-1}/y)。边界无固定点，内部固定点会迫使 b³=1，与 ord(b)=t+1≥5 矛盾。故 ρ² 和 ρ 都无几何固定点。选定有理原点后，将自同构写成 T_P∘α；若 α≠1，则 1−α 是非零且满射的椭圆曲线自同态，从而 T_P∘α 有几何固定点。因此 ρ 是四阶有理点的平移。其 K 点表示 a↦(a^t)^{-1} 使用 Galois 自同构 σ⊗1，并非相对 Frobenius。

ρ*h=(uy)^B h^{-t}、(ρ²)*h=h^{-1}，且 a=uv 被映为 uv^{-t}。这些式子给出 S_b(χ)=S_b(χ^{-t})=S_b(χ^{-1})∈R，以及 4 整除 #X_b(K) 和 N_b^{prim}。按四点角色轨道分组不会减少现有筛系数绝对值之和；本轮没有由此导出 2√t。

新增结构位于 Proposition 5.18；本原斜率计数、全维实现及 Singer 应用依次为 Theorems 5.19、5.20、5.21。全维解析范围仍是 s≥33，有限证书范围仍是 s=2..32。

## 文献比较的必要修正

[Cohen–Kapetanakis 2021](https://doi.org/10.1017/S1446788720000099) 的 Remark 4.1 已讨论适当增长的 r。因此附件以“其主定理固定 r、本稿 r 增长”作对比还不充分；引言已补该备注，要求比较定量条件及同时范数约束。

[Cohen–Kapetanakis–Reis 2022](https://doi.org/10.5802/crmath.328) 的正式期刊版应引用 Proposition 13、Theorem 16、Corollary 17 和 Remark 18。指定阶示性函数及曲线本原点筛是已有方法；本稿的贡献应落在具体纤维和实现应用。

[Choudhary–Sharma Theorem 1，作者全文](https://www.researchgate.net/publication/396016739_Arithmetic_progressions_of_some_special_elements_in_finite_fields) 的充分条件为 q^{n/2−m}>m∏r_iW(Q_{R_i})。代入 q=t,n=4,m=2 得左边 1、右边至少 2，故这一条充分条件不能保证本稿参数的正性；这不排除其他等价结果或改进。

五项新增文献的来源和阅读范围见 Literature_Audit_scalar_realization.md。当前比较为定向核查，未确认全球首次性，也未把审查意见视为领域专家签核。

## 本轮确实执行的精确核查

verify_inner_critical.py 再次核验全部 31 行不可约性、递归 Lucas 素性、范数与精确阶证书；s=2..6 的子群枚举与多项式 gcd / Möbius 计数再次一致。
verify_inner_symmetry.py 使用已独立核验的域运算，无搜索程序导入和浮点角色近似。

| s | 本原范数纤维数 | 全部候选点 | 本原点 | 角色四点轨道数 |
|---:|---:|---:|---:|---:|
| 2 | 4 | 16 | 16 | 4 |
| 3 | 6 | 48 | 48 | 16 |
| 4 | 16 | 224 | 224 | 64 |
| 5 | 20 | 640 | 520 | 256 |
| 6 | 48 | 3072 | 2928 | 1024 |

每个纤维内均核查候选和本原子集的自由四点轨道、范数保持、阶数保持、两项计数四整除及整数角色指数分布在 −t、−1 下的不变性。31 个较大域塔仅检查各给定证书点，没有声称枚举整个大域。

- 完整输出：inner_critical_review_run.log、inner_symmetry_review_run.log。
- 精确对称数据：inner_symmetry_verification.json。
- Python 3.12.14、Windows 环境、实际退出码及输入输出哈希：review_verification_environment.json。
- 全部当前源与配套文件：PaperA_revised_sha256.json。

新增有限范围不替代通用几何证明；新结果未作 Lean 形式化。原有其他核验器在此轮未重新运行。

## 尚未采用的研究和编辑线索

审查提出的显式 Weierstrass 方程及 j 值、半直积覆盖的群与亏格、通过商曲线将字符界降到 2√t，均尚缺本轮可逐步核查的完整推导，未作为定理或现有依赖写入正文。
聚焦 §5、调整题名和拆稿的建议可作为后续编辑选择；此次保留总体组织，先完成证明和归属的增强。两项同时本原、全部联合生成斜率的临界主项及统一 k≤q^{1/4} 仍按现有台账记为开放。

当前源的编译和静态同步记录见 Revision_Report.md；本轮未另行导出 PDF 或声称完成逐页排版审查。
