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

---

以下为此前记录；开放状态、编号、行号及编译统计按各轮历史版本读取，最新结论以上述闭合记录为准。

# Paper A：Mixed Character → Density 完整证明与修订说明

日期：2026-10-12。台账：`PaperA_Mixed_Character_Handoff_v1.md`。
当前打开的 `PaperA_revised.tex` 就地更新；LaTeX 插入片段为
`inner_mixed_character_section.tex.inc`。本文结果未作 Lean 形式化。

## 1. 从原文核实的定义与参数

\[
t=2^s\ (s\ge2),\quad K=\mathbb F_t,\ E=\mathbb F_{t^2},\ L=\mathbb F_{t^4},
\quad A=t+1,\ B=t^2+1,\ d=AB.
\]

$U=\ker N_{E/K}=C_A$、$V=\ker N_{L/E}=C_B$、$C_d=\ker N_{L/K}$，且 $\gcd(A,B)=1$。

\[
X_b(K)=\{a\in L:N_{L/E}(a)=b,\ N_{L/K}(1+a)=1\},\quad b\in U.
\]

其中 $a$ 是四次扩域中的候选斜率，$b=a^B$ 是固定的相对范数。
另设 $w=(1+a)^B\in U$、$v=a^A\in V$、$v_+=(1+a)^A\in V$。
$z\mapsto(z^B,z^A)$ 是 $C_d\simeq U\times V$ 的有限群同构。

### 好纤维与例外纤维

原文 Lemma 5.16 的光滑性证明扩展至**全部 $b^3\ne1$**，无需 $b$ 本原。
它们的光滑 $(2,2)$ 完备模型为

\[
(x+1)(x+b)(y+1)(y+b^{-1})=xy.
\]

八个边界点互异、光滑、没有 $K$-有理点，亏格为一。因此
$\#X_b(K)=A+O(\sqrt t)$，误差常数为 2。

排除集合有 $r_0=\gcd(3,A)\le3$ 个元素。这不是说三个模型都奇异：

- $b=1$ 时八点合并为四点；模型仍光滑。在有限坐标中方程为
  $(x+1)^2(y+1)^2=xy$，偏导为 $y,x$；四个边界点在相应图中也光滑。
  本轮不对它套用八点赋值表。
- 非平凡三次单位根 $b$（仅奇数 $s$ 时出现）使内部点
  $(x,y)=(b^2,b)$ 的两偏导消失，模型确有奇异点。
- 所有例外纤维都满足 $\#X_b(K)\le2A$：每个 $w\in U$ 至多给出
  $X^2+(1+b+w)X+b$ 的两个根。全参数统计据此统一处理。

## 2. 原交接命题必须修正

对 $\xi,\zeta\in\widehat{C_d}$，若
$\xi=\alpha\circ N_{L/E}$、$\zeta=1$，则

\[
S_b(\xi,1)=\alpha(b)\#X_b(K).
\]

即使 $\alpha\ne1$，其绝对值仍约为 $t$。因此“每个非平凡二角色对均为
$O(\sqrt t)$”为假。对 $L^\times$ 的角色还应先限制到 $C_d$；限制后平凡的
角色也不允许当作几何非平凡角色。

正确形式是：所有非平凡三元组
$(\eta,\chi,\psi)\in\widehat U\times\widehat V\times\widehat V$ 满足

\[
\left|\sum_{a\in X_b(K)}\eta(w)\chi(v)\psi(v_+)\right|\le8\sqrt t,
\qquad b^3\ne1.
\]

对二角色作唯一分解
$\xi(z)=\alpha(z^B)\chi(z^A)$、$\zeta(z)=\eta(z^B)\psi(z^A)$；
仅 $\eta=\chi=\psi=1$ 留下常值项，其余均有此界。

## 3. 完整覆盖与 Kummer 独立性

### 3.1 实际的 Lang 拉回

令 $\sigma\in\operatorname{Gal}(L/K)$ 为 $a\mapsto a^t$，对每个 $K$-代数
使用 $\sigma\otimes1$。映射 $\nu(z)=z\sigma(z)$ 在 $K$-点上等于 $z^A$，
并且 $N_{L/E}(\nu(z))=N_{L/K}(z)=1$。
它提供到二维范数环面的代数映射。

这一步不能以几何点上的普通 $A$ 次幂代替；对 $1+a$，后者的相对范数
为变量 $w^A$，并不恒等于一。参考稿中直接使用
$((y+1)^t/(x+1))^A$ 的覆盖缺少范数耦合项。

令 $w_0=(x+1)(x+b)/x$，三个 Lang 覆盖在代数闭包上为

\[
z_U^A=w_0^{-1},\qquad z_1^B=g_1,\qquad z_2^B=g_2,
\]

\[
g_1=b^{-1}y^{t-1}/x^A,\qquad
g_2=w_0^t(y+1)^{t-1}/(x+1)^A.
\]

这里 $w_0^t$ 是必要的耦合项。下降的 Frobenius 在底点上为
$(x,y)\mapsto(b/y^t,x^t)$，在三个覆盖坐标上乘以
$w_0,xy,(x+1)(y+1)$。有理点上这三者正是 $w,v,v_+$，
所以迹确为所需混合角色值，而非只根据裸 Kummer 方程推断。

### 3.2 八点赋值表

| 点 | $w_0$ | $g_1$ | $g_2$ |
|---|---:|---:|---:|
| $(0,1)$ | −1 | −A | −1 |
| $(0,b^{-1})$ | −1 | −A | −t |
| $(\infty,1)$ | −1 | A | t |
| $(\infty,b^{-1})$ | −1 | A | 1 |
| $(1,0)$ | 1 | t−1 | −1 |
| $(b,0)$ | 1 | t−1 | t |
| $(1,\infty)$ | 1 | −(t−1) | −t |
| $(b,\infty)$ | 1 | −(t−1) | 1 |

若 $m\mid B$ 且 $g_1^r g_2^s=f^m$，首两行给出
$m\mid Ar+s$、$m\mid Ar+ts$。
因为 $A(t-1)=B-2$ 且 $B$ 奇数，$\gcd(A(t-1),B)=1$，
相减得到 $m\mid s$，继而 $m\mid r$。
$w_0$ 的 −1 赋值排除任何阶整除 $A$ 的非平凡幂关系。

同时有更强的显式关系检验：

\[
w_0^{Be_0}g_1^{Ae_1}g_2^{Ae_2}\in\overline K(C_b)^{\times AB}
\ \Longrightarrow\ A\mid e_0,\ B\mid e_1,e_2.
\]

由两个惯性群上的角色检验，几何单值群的湮灭角色只有平凡角色。
有限阿贝尔群的任何真子群都有非平凡湮灭角色，所以几何单值群是
整个 $U\times V\times V$。全乘积覆盖与所有角色商覆盖均几何连通；
其光滑完备规范化几何不可约。

交接稿中 $x^r(1+x)^s$ 的裸幂关系也确实可用 $x=0,1$ 的单赋值排除，
但该裸覆盖不能自动提供当前 $K$-定义的范数角色迹。正文改用上述实际覆盖。

### 3.3 分歧、导子及平方根界

所有覆盖次数为奇数，特征为二，因此全部分歧温和、Swan 导子为零。
秩一角色在每行的局部导子为 0 或 1，取决于惯性角色是否抵消。
总导子 $r\le8$，不因角色阶增长。**不声称每个混合角色在八点都分歧。**

具体可计算：取角色指数 $e_0\bmod A,e_1,e_2\bmod B$，第 $P$ 行为活动分歧点
当且仅当

\[
-Be_0\operatorname{ord}_P(w_0)+A(e_1\operatorname{ord}_P(g_1)
+e_2\operatorname{ord}_P(g_2))\not\equiv0\pmod {AB}.
\]

幂关系检验保证非平凡三元组的 $r>0$。延拓过非活动边界点后，
紧支撑 $H_c^0,H_c^2$ 消失，温和 Euler 公式给出 $\dim H_c^1=r$。
经典 Weil 曲线定理作用于有限覆盖的角色分量，特征根绝对值至多 $\sqrt t$。
故角色和不超过 $r\sqrt t\le8\sqrt t$。边界无 $K$-点，不产生额外常数项。

## 4. 联合生成密度：固定与全参数明确分开

记 $\theta_2(n)=\prod_{p\mid n}(1-p^{-2})$、$W(n)=2^{\omega(n)}$，
$J_b=\{p\mid A:b\in U^p\}$、$\lambda_A(b)=\prod_{p\in J_b}(1-p^{-1})$。

固定纤维 $b^3\ne1$ 的总体约为 $A\sim t$，且

\[
\left||\mathcal R_{d,b}|-\lambda_A(b)\theta_2(B)A\right|
\le\lambda_A(b)\theta_2(B)(8\,2^{|J_b|}W(B)-6)\sqrt t.
\]

本原 $b$ 时 $J_b=\varnothing$，系数为 $\theta_2(B)$，不是 $\theta_2(d)$。
原因是 $b$ 已生成整个 $U$；此时 $w$ 无需为 $U$-本原元素。

逐素数角色指标的常数系数与绝对系数总量分别为
$c_b=\lambda_A(b)\theta_2(B)$ 和 $c_b2^{|J_b|}W(B)$。
平凡角色的 Hasse 误差 2 与所有非平凡角色的界 8 合并为 $8M-6$。

令 $H(A)=\prod_{p\mid A}(p+2)/(p+1)\le W(A)$，有限精确平均为

\[
\sum_b\lambda_A(b)=A\theta_2(A),\qquad
\sum_b\lambda_A(b)2^{|J_b|}=A\theta_2(A)H(A).
\]

处理至多 $r_0$ 个例外纤维后，得到全参数总体约为 $A^2\sim t^2$ 的公式

\[
\left||\mathcal R_d|-\theta_2(d)A^2\right|
\le\theta_2(d)A(8H(A)W(B)-6)\sqrt t+2r_0A.
\]

所以 $|\mathcal R_d|=\theta_2(d)t^2+O(t^{3/2}W(d))$，并且
$|\mathcal R_d|\sim\theta_2(d)t^2$。
另有 $|T_d-A^2|\le2A\sqrt t+r_0A$，因而实际联合生成比例为
$|\mathcal R_d|/T_d=\theta_2(d)+O(W(d)/\sqrt t)$。

## 5. 双满阶统计

$D_{d,b}$ 计数固定纤维中 $a,1+a$ 均具有阶 $d$ 的元素，$D_d=\sum_b D_{d,b}$。
非本原 $b$ 时为零；本原 $b$ 时须同时筛 $w,v,v_+$ 的本原性。
令 $\theta(n)=\varphi(n)/n$、$c=\theta(A)\theta(B)^2$，则

\[
|D_{d,b}-cA|\le c(8W(A)W(B)^2-6)\sqrt t,
\]

\[
|D_d-\theta(d)^2A^2|
\le\theta(d)^2A(8W(A)W(B)^2-6)\sqrt t.
\]

由于 $W(A)W(B)^2=t^{o(1)}$，得到 $D_d\sim\theta(d)^2t^2$，
从而充分大的 $s$ 必有双满阶斜率。显式充分条件为
$A>(8W(A)W(B)^2-6)\sqrt t$。

## 6. 证明依赖与有限核验

| 输入 | 使用位置 | 范围 |
|---|---|---|
| Kummer 局部赋值与有限阿贝尔群湮灭角色判据 | Mixed Proposition 的几何连通性 | 正文完整给出 |
| Lang 等源映射及有限域角色迹 | 三个实际范数环面覆盖 | [Katz 1989，pp.198–199](https://web.math.princeton.edu/~nmk/old/estcharsums.pdf)；下降另逐项给出 |
| Hasse–Weil 曲线点数界 | 平凡角色项 | 亏格一、好纤维 |
| 曲线 Artin 角色的 Weil 界、温和 Euler 公式、迹公式 | 非平凡角色项 | [Farashahi 等作者稿 §4 Lemma 1](https://www.normalesup.org/~tibouchi/papers/welldistributed.pdf)；所有局部条件在正文核实 |
| 循环群的本原元素角色指标 | 双满阶筛 | 正文旧 Theorem 5.19 已给出；[CKR 2022 Proposition 13](https://comptes-rendus.academie-sciences.fr/mathematique/item/10.5802/crmath.328.pdf) 为一般指标背景 |

独立复核结果：

- 附件 31 份双满阶域塔证书 $s=2..32$ 全部通过不可约性、完整素数认证、
  范数、两个元素的全部 $d/p$ 阶数余数检验；完整余数保存到结果 JSON。
- $s=2..6$ 全部范数纤维枚举，核查两项有限平均、好纤维 Hasse 界、
  固定纤维计数界及下表。没有用浮点角色值判断精确等式。
- 证书点上另核对了修正后的两个 Lang 函数与三个迹乘子。
- 程序不导入外部证书搜索器；共用此前独立验证器的有限域算术和递归 Lucas 证书。

| s | R_d | D_d |
|---:|---:|---:|
| 2 | 24 | 8 |
| 3 | 72 | 24 |
| 4 | 240 | 208 |
| 5 | 960 | 240 |
| 6 | 3960 | 1992 |

这些有限核验不替代几何证明，也未验证所有参数的双满阶存在性。

## 7. 修正与剩余漏洞边界

1. 原非平凡二角色命题有明确反例；正文已分类并保留常值项。
2. 固定密度必须保留 $b$；本原范数时主系数是 $\theta_2(B)$。
3. 裸 Kummer 幂关系、有限域点幂运算与真实 Lang 拉回不可混同；
   正文显式构造 $\nu$、$g_2$ 的耦合项以及 Frobenius 下降。
4. 混合角色存在局部分歧抵消；正文只用总导子 ≤8，没有假设八点全分歧。
5. 例外纤维没有套用好纤维的光滑或角色界，统一以 ≤2A 根数处理。
6. 全维双满阶已由 Proposition 5.25 与完整算术覆盖闭合；特殊迹一子族在 s=3,5 为空。
7. 经典方法均已归属；具体结果的优先权未确认，未作 Lean 形式化。

## 8. 正式交付位置

- Proposition 5.21：`prop:inner-mixed-character`，完整混合覆盖及角色界。
- Corollary 5.22：`cor:inner-mixed-exception`，二角色例外的准确分类。
- Theorem 5.23：`thm:inner-joint-density`，固定及全参数联合生成密度。
- Theorem 5.24：`thm:inner-double-count`，双满阶计数及充分大参数存在性。
- LaTeX：`inner_mixed_character_section.tex.inc`，含全部陈述、赋值表及证明。
- 数学记录：主证明台账中五个新增 ID，以及已闭合的 `Q-scalar-inner-joint-count`。
- 原先单斜率全维结论及其有限证书保留，迹一子族现为 Proposition 5.25，Singer 应用为 Theorem 5.26。


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
