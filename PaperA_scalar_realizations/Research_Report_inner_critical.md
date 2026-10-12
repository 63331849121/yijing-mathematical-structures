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

# 临界内侧乘法子群的全维实现性：完整研究报告

日期：2026-10-12。参数为 $t=2^s, s\ge2, q=t^4, d=(t+1)(t^2+1)$。

## Part I — 结论

**命题 A 已证明，而且可以加强为单个斜率生成整个子群：**

\[
\forall s\ge2\quad\exists a\in\mathbb F_{2^{4s}}:
\qquad\operatorname{ord}(a)=d,\qquad(1+a)^d=1.
\]

因此 $a,1+a\in C_d$ 且 $\langle a,1+a\rangle=C_d$。对任意非零平移参数 $c$，仿射完整映射 $f(x)=ax+c$ 与其指定伴随生成 $\mathbb F_q^+\rtimes C_d$。这个群是真本原仿射群。

证明由两部分组成：

- 对 **所有 $s\ge33$**，固定本原相对范数，把候选集化为 genus 1 曲线；证明每个非平凡角色的导子度数恰为 8，应用经典 Weil 界及本原元素筛得到严格正下界。
- 对 **全部 $2\le s\le32$**，给出 31 个明确的有限域塔证书。独立验证器用精确算术核验不可约性、素数分解、范数及每一个阶数条件。有限范围已经穷尽，没有用小维数据外推无限结论。

另得到本原斜率数量的有效估计。令 $A=t+1, B=t^2+1, \theta(B)=\varphi(B)/B, W(B)=2^{\omega(B)}$，并令

\[
N_d^{\mathrm{prim}}=\#\{a\in C_d:\operatorname{ord}(a)=d, 1+a\in C_d\}.
\]

则

\[
\left|N_d^{\mathrm{prim}}-\varphi(A)\theta(B)(t+1)\right|
\le\varphi(A)\theta(B)(8W(B)-6)\sqrt t.
\tag{1}
\]

特别地 $N_d^{\mathrm{prim}}\sim\varphi(A)\theta(B)t$。这是 $N_d^{\mathrm{prim}}$ 的渐近式，不能替换成全部联合生成斜率数 $\lvert\mathcal R_d\rvert$ 的渐近式。

证明状态：**已证（依赖外部定理）**，使用经典 Weil 曲线界并包含有限精确证书；未作 Lean 形式化。文献优先权尚未确认。

## Part II — 定义、引理、定理与完整证明

### 1. 基本分解及二次参数化

置 $K=\mathbb F_t, E=\mathbb F_{t^2}, L=\mathbb F_{t^4}$。因为 $t$ 为偶数，

\[
\gcd(t+1,t^2+1)=1,\quad
C_d=\ker N_{L/K},\quad
U=\ker N_{E/K}=C_A,\quad V=\ker N_{L/E}=C_B.
\]

若 $a\in L\setminus E$，令

\[
b=a^{t^2+1},\quad c=a+a^{t^2},\quad w=(1+a)^{t^2+1}.
\]

则 $c\ne0, w=1+b+c$，而 $a$ 的最小多项式为 $X^2+cX+b$。由范数传递，$a,1+a\in C_d$ 当且仅当 $b,w\in U$。除以 $c^2$ 后的 Artin–Schreier 方程说明不可约的充要条件为

\[
\operatorname{Tr}_{E/\mathbb F_2}(b/c^2)=1.
\]

反之，任取 $b,w\in U$，若 $c=1+b+w\ne0$ 且上述迹为 1，该二次多项式在 $E$ 上不可约，其两个共轭根位于 $L\setminus E$，具有所需的两个范数。每个候选元素确定唯一的有序参数对 $(b,w)$，每个合格参数对给出两个元素。

必须补上 $a\in E$ 的分支。此时 $N_{L/K}(a)=N_{E/K}(a)^2$，故所需条件等价于 $a,1+a\in U$。于是

\[
a^t=a^{-1},\quad(1+a)^t=(1+a)^{-1},\quad
(1+a)(1+a^{-1})=1,
\]

从而 $a^2+a+1=0$。两根在 $U$ 中当且仅当 $3\mid t+1$，即 $s$ 为奇数。它们仅生成 $C_3$，而 $d>3$，所以不贡献实现斜率。对于这两个解，$c=1+b+w=0$。这证明附件参数化对非退化候选的完整性，也准确处理了此前遗漏的子域解。

### 2. 固定本原范数后的几何模型

固定阶为 $A$ 的 $b\in U$，定义

\[
X_b(K)=\{a\in L:N_{L/E}(a)=b, N_{L/K}(1+a)=1\}.
\]

这里相对范数方程按限制标量写成两个 $K$ 方程，所以这是在 $K$ 上定义的曲线。延拓到代数闭包后，四个共轭坐标可写为

\[
(a_0,a_1,a_2,a_3)=(x,y,b/x,b^{-1}/y).
\]

余下的范数条件成为

\[
(x+1)(x+b)(y+1)(y+b^{-1})=xy.\tag{2}
\]

**光滑性。** 记 $P=(x+1)(x+b), Q=(y+1)(y+b^{-1})$。在环面内，曲线上 $PQ=xy\ne0$。若奇异，则两个偏导给出

\[
(b+1)Q+y=0,\qquad(b^{-1}+1)P+x=0.
\]

相乘并用 $PQ=xy$ 得 $b+b^{-1}=1$，即 $b^2+b+1=0$。这与 $b$ 的阶为 $A\ge5$ 矛盾。

在 $\mathbb P^1\times\mathbb P^1$ 中的八个边界点恰为

\[
\begin{aligned}
D_x&=\{(0,1),(0,b^{-1}),(\infty,1),(\infty,b^{-1})\},\\
D_y&=\{(1,0),(b,0),(1,\infty),(b,\infty)\}.
\end{aligned}
\]

它们互异。取适当仿射坐标后，沿有限坐标的偏导是 $1+b$ 或 $1+b^{-1}$ 的非零倍数，故全部光滑。四个角点均不在曲线上。

**几何连通性及亏格。** 该曲线双次数为 $(2,2)$。若光滑曲线可约，不同分支必须不相交；但双次数为 $(r_1,s_1)$、$(r_2,s_2)$ 的分支交数为 $r_1s_2+r_2s_1$。所有交数为零会迫使所有分支都是同一投影的纤维，与总双次数两个分量均为 2 矛盾。因此曲线几何不可约，亏格为 $(2-1)(2-1)=1$。记其在 $K$ 上的光滑完备化为 $C_b$。

**没有有理边界点。** 分裂坐标上的 $t$-Frobenius 为 $(x,y)\mapsto(b/y^t,x^t)$。有理点满足 $y=x^t$。上述八个边界点没有一个满足此式。因此 $C_b(K)=X_b(K)$。经典 Hasse–Weil 界给出

\[
\bigl|\#X_b(K)-(t+1)\bigr|\le2\sqrt t.\tag{3}
\]

### 3. 角色和的统一界：导子计算

令 $u\in U$ 为 $b$ 的唯一平方根。因为 $N_{L/E}(u)=u^2=b$，对每个 $a\in X_b(K)$ 都有 $a/u\in V$。需要估计 $V$ 的角色，而非直接套用 $L^\times$ 上的普通一变量 Jacobi 和。

**外部经典输入。** 对光滑、几何连通、亏格为 $g$ 的曲线上的有限阶、几何非平凡秩一角色，若在 $r$ 个几何边界点均温和且非平凡分歧，则角色和绝对值不超过 $(2g-2+r)\sqrt t$。这来自 Weil 曲线定理：紧支撑上同调的 0、2 次消失，温和 Euler 特征公式给出 1 次维数 $2g-2+r$，迹公式及 Weil 特征根界完成估计。有限阶角色可由相应有限曲线覆盖的角色分量实现。这个经典输入的来源和适用假设见 Part IV；这里不把 Weil 定理重新证明，也不把它列成未证猜想。

令

\[
\mathcal T=\operatorname{Res}_{E/K}(\ker N_{L/E}).
\]

这是二维环面，$\mathcal T(K)=V$。在代数闭包上的两个坐标下，其 Frobenius 为

\[
F_{\mathcal T}(z_0,z_1)=(z_1^{-t},z_0^t).
\]

Lang 映射 $z\mapsto F_{\mathcal T}(z)/z$ 的核是常数循环群 $V$，阶为 $B$。沿 $a\mapsto a/u$ 拉回，并写 $r_0=x/u, r_1=y/u^t$，得到

\[
z_1^{-t}/z_0=r_0,\qquad z_0^t/z_1=r_1.
\]

消去 $z_1$ 即得

\[
z_0^B=h,\qquad h=\frac{(y/u^t)^t}{x/u}.\tag{4}
\]

因此对精确阶为 $m>1, m\mid B$ 的角色，其商覆盖在代数闭包上是 $z^m=h$。$x$ 的四个单零极点支撑于 $D_x$，$y$ 的四个单零极点支撑于不相交的 $D_y$。所以 $h$ 的非零赋值是 $+1,-1,+t,-t$，每种各出现两次。

由于 $m$ 为奇数且 $\gcd(m,t)=1$，每个赋值均与 $m$ 互素，八点全部完全分歧，且为温和分歧。绝对值为 1 的赋值还排除了 $h$ 为真幂的可能，保证商覆盖几何连通。角色的导子度数恰为 8，不随 $m,t,b$ 增长。由此同时排除了几何平凡角色及常数域角色造成的大主项。

Lang 覆盖在有理点上的 Frobenius 类就是 $a/u$，因 Frobenius 约定可能取逆，这不改变绝对值。因此对所有非平凡 $\chi\in\widehat V$，

\[
\left|\sum_{a\in X_b(K)}\chi(a/u)\right|\le8\sqrt t.\tag{5}
\]

这里的统一常数来自明确的八点导子计算，并非未经证明的平方根抵消假设。


**显式 K 下降及迹归一化（2026-10-12 合并）。** Kummer 方程是在几何分裂坐标中写成的；其 K 结构继承自 Lang 覆盖，不能把 h 直接视为 K(C_b) 的函数。由 u^{t²}=u，有 h=y^t/x。Lang 方程给出 z_1^{-t}=(x/u)z_0，因此

\[
F_Y(x,y,z_0)=(b/y^t,x^t,(x/u)z_0),\qquad
h(F_{C_b}(x,y))=(x/u)^B h(x,y).
\]

在有理点 (x,y)=(a,a^t) 上，底点固定、覆盖纤维上的乘子恰为 a/u∈V，所以角色迹为 χ(a/u)，逆 Frobenius 约定下取逆角色。台账 P-scalar-inner-explicit-lang-trace，正文 Lemma 5.17、eq:inner-lang-frobenius。

**四阶有理平移。** 台账 P-scalar-inner-four-torsion，正文 Proposition 5.18。ρ(x,y)=(1/y,x/b) 是 K 自同构；K 点上的 a↦(a^t)^{-1} 使用 L/K 的 Galois 自同构的张量扩张。ρ²=(b/x,b^{-1}/y) 无几何固定点：八边界点两两互换，内部固定点只能是 (u,u^{-1})，并迫使 b³=1。Hasse–Weil 保证有理原点，随后固定点判据说明 ρ 为四阶有理点平移。两个边界四点轨道、ρ*h=(uy)^B h^{-t}、(ρ²)*h=h^{-1} 都有显式计算。因此 S_b(χ)=S_b(χ^{-t})=S_b(χ^{-1})∈R，且 4 整除 #X_b(K) 和 N_b^{prim}。此结构不自动减小筛的绝对系数总量，后续仍用 8√t。

### 4. 本原筛及数量估计

$a=uv$ 且 $\operatorname{ord}(u)=A, v\in V$。因为 $\gcd(A,B)=1$，

\[
\operatorname{ord}(a)=AB\quad\Longleftrightarrow\quad\operatorname{ord}(v)=B.
\]

循环群的本原元素示性函数为

\[
\mathbf1_{\operatorname{ord}(v)=B}
=\theta(B)\sum_{m\mid B}\frac{\mu(m)}{\varphi(m)}
\sum_{\operatorname{ord}(\chi)=m}\chi(v).\tag{6}
\]

证明此式只需逐素因子相乘：对于 $p\mid B$，括号中的对应因子在 $V^p$ 上为零，在其外为 $p/(p-1)$；再乘 $	heta(B)=\prod_{p\mid B}(p-1)/p$ 即得示性函数。

把式 $6$ 对 $X_b(K)$ 求和。平凡角色贡献为 $	heta(B)\#X_b(K)$。每一个非平凡平方自由除数 $m$ 对应的角色系数绝对值之和为 1，共有 $W(B)-1$ 个。因此由式 $3$、$5$，

\[
\left|N_b^{\mathrm{prim}}-\theta(B)(t+1)\right|
\le\theta(B)\bigl(2+8(W(B)-1)\bigr)\sqrt t
=\theta(B)(8W(B)-6)\sqrt t.\tag{7}
\]

阶为 $d$ 的 $a$ 的相对范数 $a^B$ 的阶恰为 $A$，故全部 $\varphi(A)$ 个本原范数纤维恰好分割 $N_d^{\mathrm{prim}}$，相加得到式 $1$。

最后，对任意 $\epsilon>0$，除有限多个小素数外都有 $2\le p^\epsilon$，从而 $2^{\omega(N)}\le C_\epsilon N^\epsilon$。由 $B\asymp t^2$ 得 $W(B)=t^{o(1)}$。式 $1$ 的相对误差趋于零，证明所述渐近式。

### 5. 显式界：所有 $s\ge33$

若素数 $p\mid B=t^2+1$，则 $p$ 为奇数且 $-1$ 是模 $p$ 平方，故 $p\equiv1\pmod4$。对 $p\ge256$，有 $2\le p^{1/8}$。对其余素数，仅需检查

\[
5,13,17,29,37,41,53,61,73,89,97,101,
109,113,137,149,157,173,181,193,197,229,233,241.
\]

这 24 个素数的乘积为

\[
6045408114863853991373345088496297320256672385.
\]

整数比较 $256^{24}<32^8\prod p$ 给出

\[
W(B)<32B^{1/8}.\tag{8}
\]

考虑重素因子只会使 $B^{1/8}$ 更大，故此界对任意 $B$ 成立。若 $s\ge33$，则 $t^2\ge2^{66}$ 且 $t^2+1<2t^2$，所以

\[
t^4>2^{64}(t^2+1),\qquad
\sqrt t>256B^{1/8}>8W(B).
\]

由式 $7$ 得

\[
N_b^{\mathrm{prim}}\ge\theta(B)\left[t+1-(8W(B)-6)\sqrt t\right]>0.
\]

这对每一个本原范数 $b$ 成立，证明所有 $s\ge33$ 的存在性。

### 6. 有限尾部及群论结论

对 $2\le s\le32$，Part IV 所列证书指定

\[
E=\mathbb F_2[X]/M_s(X),\qquad
L=E[Z]/(Z^2+(1+b+w)Z+b),\qquad a=Z.
\]

每行完成以下精确验证：

1. $M_s$ 首一、次数 $2s$，并满足二元域不可约判据 $X^{2^{2s}}=X\pmod {M_s}$，以及对每个素数 $r\mid2s$，$\gcd(M_s,X^{2^{2s/r}}-X)=1$。
2. $b,w\in U$，$b$ 的阶恰为 $A$，$c=1+b+w\ne0$，且绝对迹为 1，故二次扩张确为 $L$。
3. $a^d=(1+a)^d=1, a^B=b, (1+a)^B=w$。
4. 对完整素因子分解中的每个 $p\mid d$，逐一验证 $a^{d/p}\ne1$。因此 $a$ 的阶恰为 $d$。每个余数均已保存。

素数认证使用完整 Lucas 证书。递归认证 $p-1$ 的全部素因子，并找到整数 $v$ 使 $v^{p-1}\equiv1\pmod p$，且对每个素因子 $r\mid p-1$，$\gcd(v^{(p-1)/r}-1,p)=1$。若 $\ell\mid p$ 为素数，这些条件迫使 $v\bmod\ell$ 的阶为 $p-1$，因此 $p-1\mid\ell-1$，只能 $\ell=p$，所以 $p$ 为素数。递归终点是 2。寻找阶段的快速素性筛不作为证明依据。

31 行证书覆盖解析证明之外的全部参数。因此全维命题已经闭合。

群论方面，$d>t^2-1$。若 $a$ 落在 $L$ 的真二元子域，那个子域至多有 $t^2$ 个元素，与其阶为 $d$ 矛盾。因此 $\mathbb F_2[a]=L$，乘法子群作用不可约。指数 $t-1>1$ 使该子群为真子群；利用现有仿射伴随群结构公式，对每个 $c\ne0$ 均得到 $L^+\rtimes C_d$。这完成强化版命题 A。

## Part III — 证明边界与仍未解决的问题

本轮主命题没有残留的未证中间引理。证明明确使用经典 Weil 曲线定理及其温和角色版本；有限尾部是已核验的算术证书，不是数值趋势。

以下逐项列出当前证明边界（包括本次已闭合条目）：

- 对所有许可指数 $k\le q^{1/4}$ 的普遍实现性。本轮只完全解决 $q=t^4, k=t-1$ 这一临界族。
- 全部联合生成斜率的主项及一致误差现已由 Theorem 5.23 闭合；见下方 Part VII。固定纤维系数取决于范数 b。
- 同时要求 $a$ 与 $1+a$ 都具有阶 $d$ 的全维命题。
- 附件建议的对所有 $h$ 一致的 $T_{d/h}=t^2/h^2+O(t^{3/2})$ 估计。本证明没有使用它，也没有证明它。
- 完全消除有限计算、给出对所有 $s$ 的单一显式公式。当前证明已完备，但不是无计算构造。
- 定理的文献首次性。定向检索不能替代全面优先权核查。

对角限制 $b=w$ 的失败也已准确定位：它会漏掉实际存在的实现元素；在 $s=3,5$ 上，全部对角候选都不能生成 $C_d$。因此它不能作为全维证明的唯一构造。

## Part IV — 可复现计算、证书与文献

### 精确计数

| $s$ | $d$ | $T_d$ | $\lvert\mathcal R_d\rvert$ | $N_d^{\mathrm{prim}}$ | 对角候选数 | 对角实现数 |
|---:|---:|---:|---:|---:|---:|---:|
| 2 | 85 | 24 | 24 | 16 | 8 | 8 |
| 3 | 585 | 86 | 72 | 48 | 4 | 0 |
| 4 | 4369 | 240 | 240 | 224 | 16 | 16 |
| 5 | 33825 | 1214 | 960 | 520 | 44 | 0 |
| 6 | 266305 | 4104 | 3960 | 2928 | 56 | 24 |

前两列计数通过两种独立方法一致核验：直接枚举乘法子群并计算离散指数的最大公因数，以及二元多项式 gcd 配合 Möbius 反演。它们重现附件中的全部五行数据。对每个小维本原范数纤维，还检查了式 $3$ 的整数形式；子域退化解的数量在奇数 $s$ 为 2、偶数 $s$ 为 0。

### 证书文件与复现

- `inner_critical_certificates.json`：全部 $s=2,\ldots,32$ 的域多项式、$b,w,c$、因子分解、阶数余数、递归素数证书。
- `verify_inner_critical.py`：不导入证书搜索程序，独立实现有限域乘法、幂运算及精确认证；只需 Python 标准库。
- `inner_critical_verification.json`：实际验证范围、独立计数及有效常数。
- `find_inner_critical_certificates.py`：可选的确定种子搜索程序。验证既有证书不依赖重跑搜索。
- 论文计算附录包含全部 31 行 $M_s,b,w$ 十六进制表及证书的数学验证规则。

在文件所在目录运行：

```text
python verify_inner_critical.py
```

不要使用禁用断言的 `-O` 参数。正常结果逐行报告 31 个参数全部验证完成，随后报告 $s=2,\ldots,6$ 的两种计数一致。完整论文的旧有复现入口 `python reproduce_paperA.py` 也已接入此验证器。

### 阅读过的直接文献及适用边界

1. N. M. Katz, *An Estimate for Character Sums*, J. Amer. Math. Soc. 2 $1989$, 197–200。[作者全文](https://web.math.princeton.edu/~nmk/old/estcharsums.pdf)。使用其 Lang 覆盖与角色层的标准解释；该文的直线角色和主定理并不是本报告 genus 1 界的直接替代。本报告另行证明拉回后的八点分歧。
2. R. R. Farashahi, P.-A. Fouque, I. E. Shparlinski, M. Tibouchi, J. F. Voloch, *Indifferentiable Deterministic Hashing to Elliptic and Hyperelliptic Curves*, Math. Comp. 82 $2013$, 491–512。[DOI](https://doi.org/10.1090/S0025-5718-2012-02606-8)、[作者全文](https://www.normalesup.org/~tibouchi/papers/welldistributed.pdf)。作者稿 §4、Lemma 1 给出亏格和导子形式的曲线 Artin 角色界。这里还明确核实了几何非平凡性，避免把常数域角色套入平方根界。
3. H. Kudo, Y. Nogata, *Cyclotomic Numbers of Order $q-1$ over $\mathbb F_{q^r}$*，2026-04-28 预印本，[arXiv:2604.25461](https://arxiv.org/abs/2604.25461)。其对象包含本报告 $r=4$ 的普通范数一交数；全文 Proposition 4.3 通过基域上的计数表达一般交数。本报告不能把普通 $T_d$ 计数视为新结果；新增目标是指定子群内的精确阶及伴随实现性。
4. D. Hachenberger, *Ovoids and Primitive Normal Bases for Quartic Extensions of Galois Fields*, J. Algebraic Combin. 53 $2021$, 85–114，[DOI](https://doi.org/10.1007/s10801-019-00920-8)。与四次扩张的子群分解、卵形及本原正规元素有关。所查目标与本报告“$a$ 的阶等于范数核大小，且 $1+a$ 仍在范数核”的条件不同，不能把全文标题中的 primitive 自动等同于本报告的子群生成条件。

与此前已引 Jacobi 和、广义 Paley 图及范数下降文献的合并比较，见 `Literature_Audit_scalar_realization.md`。以上属于有边界的定向核查；没有确认首次性。

## Part V — 可直接并入正文的英文 LaTeX

完整英文陈述和证明已同步到当前打开的 `PaperA_revised.tex`，对应 Proposition 5.15、Lemmas 5.16–5.17、Proposition 5.18、Theorems 5.19–5.20，以及新增结果 5.21–5.24。可移植片段为 `inner_critical_section.tex.inc`，配套有限表为 `inner_critical_appendix.tex.inc`；它们是正文片段，不是替代论文。

```latex
\subsection{Realization at the inner quarter-power boundary}
\label{subsec:inner-critical}

The obstruction at $k=t+1$ has a positive counterpart at $k=t-1$.
Throughout this subsection put
\[
 t=2^s\ (s\ge2),\quad K=\mathbb F_t,\quad E=\mathbb F_{t^2},
 \quad L=\mathbb F_{t^4},\quad A=t+1,\quad B=t^2+1,\quad d=AB.
\]
Then $\gcd(A,B)=1$ and $C_d=\ker N_{L/K}$.
Write $U=\ker N_{E/K}=C_A$ and $V=\ker N_{L/E}=C_B$.
The next results prove the stronger assertion that some $a\in C_d$
has order $d$ and satisfies $1+a\in C_d$.

\begin{proposition}[Quadratic parametrization]\label{prop:inner-quadratic}
The elements $a\in L\setminus E$ with $a,1+a\in C_d$ correspond,
two at a time, to the ordered pairs $(b,w)\in U^2$ satisfying
\[
 c=1+b+w\ne0,\qquad
 \operatorname{Tr}_{E/\mathbb F_2}(b/c^2)=1.
\]
The two elements are the roots of $X^2+cX+b$, and
$N_{L/E}(a)=b$, $N_{L/E}(1+a)=w$.
The remaining elements, in $E$, are precisely the two roots of
$X^2+X+1$ when $s$ is odd, and there are none when $s$ is even.
These remaining elements generate only $C_3$.
\end{proposition}
\begin{proof}
If $a\notin E$, write $b=a^{t^2+1}$ and $c=a+a^{t^2}$.
Then $c\ne0$, the minimal polynomial is $X^2+cX+b$, and
$(1+a)^{t^2+1}=1+b+c=w$. Norm transitivity puts $b,w$ in $U$.
After division by $c^2$, the quadratic is an Artin--Schreier equation;
it is irreducible exactly when the displayed absolute trace is one.
Conversely, that trace condition makes the quadratic irreducible over
$E$, with both roots in $L\setminus E$. Their two relative norms are
$b,w$, so norm transitivity gives $a,1+a\in C_d$.
The relative norms determine the ordered pair uniquely.

For $a\in E$, the same norm conditions reduce to $a,1+a\in U$, since
$N_{L/K}(a)=N_{E/K}(a)^2$. Thus $a^t=a^{-1}$ and
$(1+a)^t=(1+a)^{-1}$. Substitution gives
$(1+a)(1+a^{-1})=1$, or $a^2+a+1=0$.
Such roots lie in $U$ exactly when $3\mid t+1$, equivalently when
$s$ is odd. Their two norms satisfy $1+b+w=0$.
In particular, the omitted $c=0$ branch contributes no realizing slope.
\end{proof}

\begin{lemma}[A genus-one norm fiber]\label{lem:inner-fiber}
Fix $b\in U$ with $b^3\ne1$ and put
\[
 X_b(K)=\{a\in L:N_{L/E}(a)=b,\ N_{L/K}(1+a)=1\}.
\]
This set is the full set of $K$-points of a smooth projective
geometrically connected curve $C_b/K$ of genus one. Over $\overline K$
the affine part has equation
\begin{equation}\label{eq:inner-fiber}
 (x+1)(x+b)(y+1)(y+b^{-1})=xy
 \qquad (x,y\ne0).
\end{equation}
Its completion in $\mathbb P^1\times\mathbb P^1$ has eight boundary
points, none rational over $K$. Consequently
\[
 \bigl|\#X_b(K)-(t+1)\bigr|\le2\sqrt t.
\]
\end{lemma}
\begin{proof}
The relative-norm equation defines a variety over $K$ by restriction
of scalars. In the four split coordinates of $\operatorname{Res}_{L/K}
\mathbb G_m$, write
$(a_0,a_1,a_2,a_3)=(x,y,b/x,b^{-1}/y)$.
The remaining norm equation is exactly \eqref{eq:inner-fiber}.
Let $P=(x+1)(x+b)$ and $Q=(y+1)(y+b^{-1})$.
At a singular point in the torus, $PQ=xy\ne0$ and
\[
 (b+1)Q+y=0,\qquad (b^{-1}+1)P+x=0.
\]
Multiplication would force $b+b^{-1}=1$, hence $b^3=1$.
This contradicts the hypothesis $b^3\ne1$.
The boundary points are
\[
\begin{split}
 D_x&=\{(0,1),(0,b^{-1}),(\infty,1),(\infty,b^{-1})\},\\
 D_y&=\{(1,0),(b,0),(1,\infty),(b,\infty)\}.
\end{split}
\]
They are distinct and smooth: in the appropriate affine charts the
derivative along the finite coordinate is a nonzero multiple of
$1+b$ or $1+b^{-1}$. No corner of the square is on the curve.
The smooth bidegree-$(2,2)$ curve is geometrically connected:
distinct components with zero intersection would all have to be
fibers of the same projection, contrary to the total bidegree.
It is therefore geometrically irreducible and has genus
$(2-1)(2-1)=1$. Its smooth completion descends to $K$.

The $t$-power Frobenius on these coordinates is
$(x,y)\mapsto(b/y^t,x^t)$. A rational point satisfies $y=x^t$,
which excludes all eight boundary points. Hence
$C_b(K)=X_b(K)$, with the stated interpretation in $L$.
The final bound is the Hasse--Weil bound.
\end{proof}

\begin{lemma}[Uniform character bound on a norm fiber]
\label{lem:inner-character}
Let $b$ be as in Lemma~\ref{lem:inner-fiber}, and let $u\in U$ be
the unique square root of $b$. For every nontrivial multiplicative
character $\chi$ of $V$, one has
\begin{equation}\label{eq:inner-character}
 \left|\sum_{a\in X_b(K)}\chi(a/u)\right|\le8\sqrt t.
\end{equation}
\end{lemma}
\begin{proof}
We use the classical Weil bound for a geometrically nontrivial
finite-order rank-one character on a curve: on a genus-$g$ curve,
tame ramification at $r$ geometric points gives the bound
$(2g-2+r)\sqrt t$, when the character is nontrivial at every one
of those points. This is the curve Artin-character estimate
discussed in \cite[\S4]{FFSTV13}; the Lang-torsor interpretation
of finite-field multiplicative characters is also used in \cite{Katz89}.
For completeness, the dimension underlying this estimate is
$2g-2+r$: compactly supported cohomology in degrees zero and two
vanishes, and the tame Euler-characteristic formula gives this
dimension in degree one. The trace formula and the Weil theorem
for curves bound each eigenvalue by $\sqrt t$.
For finite-order characters this is a character component of a
finite cover of the curve. We now check all these hypotheses here.

Let $\mathcal T=\operatorname{Res}_{E/K}
(\ker N_{L/E})$ denote the two-dimensional norm torus.
It has $\mathcal T(K)=V$, and $a\mapsto a/u$ maps $X_b$ to
$\mathcal T$, since $N_{L/E}(u)=u^2=b$.
Over $\overline K$ use coordinates $(z_0,z_1)$ on the torus;
its Frobenius is
\[
 F_{\mathcal T}(z_0,z_1)=(z_1^{-t},z_0^t).
\]
The Lang isogeny $z\mapsto F_{\mathcal T}(z)/z$ has constant
kernel $V$. Pulling it back along $a\mapsto a/u$, and writing
$r_0=x/u$, $r_1=y/u^t$, gives
\[
 \frac{z_1^{-t}}{z_0}=r_0,\qquad
 \frac{z_0^t}{z_1}=r_1,
 \qquad\text{hence}\qquad
 z_0^B=\frac{r_1^t}{r_0}.
\]
Thus this pullback is geometrically a Kummer cover with defining
function $h=(y/u^t)^t/(x/u)=y^t/x$, since $u^{t^2}=u$.
For a character of exact order $m\mid B$, its quotient cover has
equation $z^m=h$ over $\overline K$.
This geometric Kummer presentation must be distinguished from the
$K$-structure of the quotient cover: the latter is inherited from
the pullback of the $K$-defined Lang isogeny, with its corresponding
Frobenius descent datum. In particular, $h$ need not belong to the
function field $K(C_b)$ in these split coordinates. All statements
about geometric ramification and geometric connectedness are checked
after base change to $\overline K$, whereas the character sum is
taken using the descended $K$-cover.

The Frobenius descent can be made explicit, so that the character
trace is not merely inferred from a convention.  On geometric points,
the $K$-Frobenius on the base and on the pullback Lang cover is
\begin{equation}\label{eq:inner-lang-frobenius}
 \begin{aligned}
 F_{C_b}(x,y)&=\left(\frac b{y^t},x^t\right),\\
 F_Y(x,y,z_0)&=\left(\frac b{y^t},x^t,\frac xu z_0\right).
 \end{aligned}
\end{equation}
Indeed, the two Lang equations give $z_1^{-t}=r_0z_0$, while
$F_{\mathcal T}$ acts on the first split coordinate as
$z_0\mapsto z_1^{-t}$.  The displayed formula is also compatible
with the Kummer equation, since $u^B=b$ and
\[
 h\left(\frac b{y^t},x^t\right)
  =\frac{x^{t^2}y^t}{b}
  =\left(\frac xu\right)^B h(x,y).
\]
For a $K$-rational point, $(x,y)=(a,a^t)$ with $a^B=b$;
thus Frobenius fixes the base point and acts on its geometric
Lang fiber by $z_0\mapsto(a/u)z_0$.  This is precisely the deck
transformation indexed by $a/u\in V$.  In the character eigensheaf
associated with $\chi$, its Frobenius trace is therefore
$\chi(a/u)$, or $\chi^{-1}(a/u)$ if the inverse Frobenius convention
is used.  The latter choice is immaterial for the asserted bound.
In particular, this computation verifies the Frobenius trace
identification for the actual $K$-descent of the cover, rather
than for the bare geometric Kummer equation.

The zeros and poles of $x$ are simple and supported on $D_x$;
those of $y$ are simple and supported on the disjoint set $D_y$.
The valuations can be read point by point:
\[
 \begin{array}{c|c}
 \text{points}&\operatorname{ord}_P(h)\\\hline
 (0,1),\ (0,b^{-1})&-1\\
 (\infty,1),\ (\infty,b^{-1})&1\\
 (1,0),\ (b,0)&t\\
 (1,\infty),\ (b,\infty)&-t
 \end{array}
\]
Thus the eight nonzero valuations are $1,-1,t,-t$, each twice.
Since $m$ is odd and $\gcd(m,t)=1$, the character is tamely and
nontrivially ramified at all eight points. A valuation of absolute
value one also makes this cover geometrically connected, excluding
a constant-field character or a geometrically trivial pullback.
The conductor degree is consequently exactly eight, independently
of $m,t,b$. Lemma~\ref{lem:inner-fiber} and the curve bound now give
$(2\cdot1-2+8)\sqrt t=8\sqrt t$.
\end{proof}


\begin{proposition}[Four-torsion symmetry of a norm fiber]
\label{prop:inner-four-torsion}
In the setting of Lemma~\ref{lem:inner-fiber}, let $u\in U$ satisfy
$u^2=b$. On the geometric $(x,y)$-model of $C_b$ set
\[
 \rho(x,y)=\left(\frac1y,\frac xb\right),\qquad
 h=\frac{(y/u^t)^t}{x/u}=\frac{y^t}{x}.
\]
Then $\rho$ descends to a $K$-automorphism of order four. After
choosing a $K$-rational origin, it is translation by a $K$-rational
point of exact order four. The eight boundary points form exactly
two $\rho$-orbits of length four:
\[
 \begin{split}
 (0,1)&\longmapsto(1,0)\longmapsto(\infty,b^{-1})
     \longmapsto(b,\infty)\longmapsto(0,1),\\
 (0,b^{-1})&\longmapsto(b,0)\longmapsto(\infty,1)
     \longmapsto(1,\infty)\longmapsto(0,b^{-1}).
 \end{split}
\]
Moreover, as identities in the geometric function field,
\begin{equation}\label{eq:inner-rho-kummer}
 \rho^*h=(uy)^B h^{-t},\qquad (\rho^2)^*h=h^{-1}.
\end{equation}
For every character $\chi$ of $V$, the sums in
Lemma~\ref{lem:inner-character} satisfy
\[
 S_b(\chi):=\sum_{a\in X_b(K)}\chi(a/u)
      =S_b(\chi^{-t})=S_b(\chi^{-1})\in\mathbb R.
\]
Every nontrivial character belongs to an orbit of length four
under $\chi\mapsto\chi^{-t}$. If
$N_b^{\mathrm{prim}}$ denotes the number of $a\in X_b(K)$
with $\operatorname{ord}(a)=d$, then
$4\mid\#X_b(K)$ and $4\mid N_b^{\mathrm{prim}}$.
\end{proposition}
\begin{proof}
The field automorphism $\sigma:a\mapsto a^t$ of $L/K$
extends as $\sigma\otimes1$ to an $R$-linear automorphism of
$L\otimes_K R$ for every $K$-algebra $R$;
composing this extension with inversion gives a $K$-automorphism
of the ambient restriction-of-scalars torus. On $K$-points its
action is $a\mapsto(a^t)^{-1}$. Here this notation refers to the
Galois automorphism $\sigma$, not the relative Frobenius morphism
on the torus. The functorial norm identities
\[
 N_{L/E}((\sigma a)^{-1})=b^{-t}=b,\qquad
 N_{L/K}(1+(\sigma a)^{-1})
   =\frac{N_{L/K}(1+a)}{N_{L/K}(a)}=1
\]
show that it preserves both defining conditions, since
$N_{L/K}(a)=N_{E/K}(b)=1$. It gives the displayed $\rho$
in split coordinates. Equivalently, the split-coordinate
$K$-Frobenius descent is $(x,y)\mapsto(b/y^t,x^t)$, with which
$\rho$ commutes. Direct
iteration gives
\[
 \rho^2(x,y)=(b/x,b^{-1}/y),\qquad \rho^4=1.
\]
The eight boundary points are paired without fixed points by
$\rho^2$. Any remaining geometric fixed point would have
$x^2=b$, $y^2=b^{-1}$, hence $(x,y)=(u,u^{-1})$.
Substitution in the equation of $C_b$ forces
$b+b^{-1}=1$, equivalently $u^2+u+1=0$, whence $b^3=1$,
contrary to $b^3\ne1$. Thus $\rho^2$,
and hence $\rho$, has no geometric fixed point. The bound
$\#C_b(K)\ge t+1-2\sqrt t>0$ supplies a rational origin.
After choosing a rational origin, any automorphism of a genus-one
curve is a translation followed by an origin-preserving
automorphism. If the latter is nontrivial, its difference from the
identity is a nonzero, hence surjective, elliptic-curve
endomorphism, so the composite has a geometric fixed point.
Consequently $\rho$ is a translation, necessarily by a
$K$-rational point of exact order four.

The two boundary cycles follow by substitution in the rational
formula, interpreted on $\mathbb P^1\times\mathbb P^1$. Since
$u^{t+1}=1$, $u^B=u^2=b$ and $b^t=b^{-1}$,
\[
 \rho^*h=\frac{(x/b)^t}{1/y}
   =b x^t y=(uy)^B\left(\frac{y^t}{x}\right)^{-t},
\]
while the formula for $\rho^2$ yields $(\rho^2)^*h=h^{-1}$.
For $a=uv$ with $v\in V$, $\rho$ sends $a$ to
$uv^{-t}$. It therefore permutes $X_b(K)$ and preserves
$\operatorname{ord}(a)$; changing variables in the character sum
proves the stated equalities. Finally $B=t^2+1$ is odd,
$(-t)^2\equiv-1\pmod B$. For a character of order $m>1$,
an orbit of length one or two would imply $m\mid2$,
which is impossible since $m\mid B$ is odd. Thus every
nontrivial character has an orbit of length four. Translation
by a point of exact order four acts freely, proving both
divisibilities.
\end{proof}

These symmetries do not by themselves reduce the bound in
Lemma~\ref{lem:inner-character}: grouping the characters into
four-element orbits leaves the total absolute sieve coefficients
unchanged. The estimate used below remains $8\sqrt t$.

\begin{theorem}[Primitive slopes in the inner critical family]
\label{thm:inner-primitive-count}
Put $\theta(B)=\varphi(B)/B$ and $W(B)=2^{\omega(B)}$.
For each $b\in U$ of order $A$, let
\[
 N_b^{\mathrm{prim}}=\#\{a\in X_b(K):\operatorname{ord}(a)=d\}.
\]
Then
\begin{equation}\label{eq:inner-fiber-count}
 \bigl|N_b^{\mathrm{prim}}-\theta(B)(t+1)\bigr|
 \le\theta(B)(8W(B)-6)\sqrt t.
\end{equation}
In particular, with
$N_d^{\mathrm{prim}}=\#\{a\in C_d:\operatorname{ord}(a)=d,\ 1+a\in C_d\}$,
\begin{equation}\label{eq:inner-total-count}
 \bigl|N_d^{\mathrm{prim}}-\varphi(A)\theta(B)(t+1)\bigr|
 \le\varphi(A)\theta(B)(8W(B)-6)\sqrt t.
\end{equation}
Thus $N_d^{\mathrm{prim}}\sim\varphi(A)\theta(B)t$ as $s\to\infty$.
\end{theorem}
\begin{proof}
Every $a\in X_b(K)$ has a unique expression $a=uv$ with
$v\in V$, where $u$ is the square root of $b$ in $U$.
Since $\operatorname{ord}(u)=A$ and $\gcd(A,B)=1$, it has order
$d$ exactly when $v$ has order $B$.
The usual character indicator in a cyclic group of order $B$ is
\[
 \mathbf1_{\operatorname{ord}(v)=B}
 =\theta(B)\sum_{m\mid B}\frac{\mu(m)}{\varphi(m)}
   \sum_{\operatorname{ord}(\chi)=m}\chi(v).
\]
Indeed the sum factors over primes $p\mid B$: the corresponding
factor is zero on $V^p$ and $p/(p-1)$ off $V^p$, which cancels
the factor $(p-1)/p$ in $\theta(B)$.
The trivial-character term is $\theta(B)\#X_b(K)$.
For each nontrivial squarefree divisor $m$ the sum of the absolute
values of its coefficients is one. There are $W(B)-1$ such
divisors. Lemmas~\ref{lem:inner-fiber} and~\ref{lem:inner-character}
therefore give an error of at most
$\theta(B)(2+8(W(B)-1))\sqrt t$, proving
\eqref{eq:inner-fiber-count}.

An element of order $d$ has relative norm of order $A$, because
$N_{L/E}(a)=a^B$. Hence these $\varphi(A)$ norm fibers partition
the elements counted by $N_d^{\mathrm{prim}}$. Summing proves
\eqref{eq:inner-total-count}. Finally $2^{\omega(N)}=N^{o(1)}$:
for any $\epsilon>0$, all but finitely many primes satisfy
$2\le p^\epsilon$, and the remaining primes contribute only a
constant. Since $B\asymp t^2$, the relative error tends to zero.
\end{proof}

\begin{theorem}[All-dimensional realization at index $t-1$]
\label{thm:inner-all}
For every $s\ge2$, there exists $a\in\mathbb F_{2^{4s}}$ with
\[
 \operatorname{ord}(a)=(2^s+1)(2^{2s}+1),\qquad
 (1+a)^{(2^s+1)(2^{2s}+1)}=1.
\]
Consequently $\mathcal R_d\ne\varnothing$ at $k=t-1$ for every
such $s$. The proper primitive group $L^+\rtimes C_d$ is generated
by $f(x)=ax+c$ and $F(f)$ for every $c\in L^\times$.
\end{theorem}
\begin{proof}
Every prime divisor $p$ of $B=t^2+1$ is $1$ modulo $4$, since
$t^2\equiv-1\pmod p$. If $p\ge256$, then $2\le p^{1/8}$.
For the smaller primes a direct integer product gives
\[
 \prod_{\substack{p<256\ \mathrm{prime}\\p\equiv1\pmod4}}
 \frac{256}{p}<32^8.
\]
The 24 primes in this product and the exact integer comparison
are supplied with the finite verifier in Appendix~\ref{app:inner-cert}.
It follows for every $B$ under consideration that
\[
 W(B)<32B^{1/8}.
\]
For $s\ge33$, $t^2\ge2^{66}$ and $t^2+1<2t^2$ imply
$t^4>2^{64}(t^2+1)$. Equivalently,
$\sqrt t>256B^{1/8}>8W(B)$.
The lower bound in \eqref{eq:inner-fiber-count} is then positive
for every primitive $b\in U$.

For $2\le s\le32$, Appendix~\ref{app:inner-cert} gives explicit
field towers $E=\mathbb F_2[X]/(M_s)$ and
$L=E[Z]/(Z^2+cZ+b)$, in which $a=Z$ is a certificate.
Irreducibility, both norm conditions and the exact order $d$
are verified by deterministic finite arithmetic, with complete
factorizations and recursively certified primes. These 31 cases
exhaust the remaining range; they are not an extrapolation.

Finally $d>t^2-1$ implies $\mathbb F_2[a]=L$: every proper
subfield of $L$ has at most $t^2$ elements. Thus $C_d$ acts
irreducibly, while $k=t-1>1$ makes it a proper multiplier group.
The affine conclusion follows from
Corollary~\ref{cor:scalar-realization}.
\end{proof}

The two adjacent indices $t-1$ and $t+1$ therefore have opposite
realization behavior for every $s\ge2$.
This does not settle the universal question for all admissible
$k\le q^{1/4}$. Also, $N_d^{\mathrm{prim}}$ counts primitive individual slopes;
it is a subset count within $|\mathcal R_d|$. The joint and
double full-order counts below require the mixed-character estimate.
Ordinary intersections for index $t-1$ belong to cyclotomic
number theory, including the general norm-based treatment of
Kudo and Nogata \cite{KN26}. The additional exact-order condition
is the focus here. The classical Weil bound, Lang construction,
and primitive-character sieve are attributed above; priority
for this particular realization theorem is not asserted.


\paragraph{Mixed characters and joint densities.}
We now retain all three varying character components on a norm fiber.
For $a\in X_b(K)$ put
\begin{equation}\label{eq:inner-mixed-variables}
 w=(1+a)^B\in U,\qquad v=a^A\in V,\qquad v_+=(1+a)^A\in V.
\end{equation}
\begin{auxlemma}[Character decomposition]
The map $C_d\longrightarrow U\times V$, $z\mapsto(z^B,z^A)$,
is an isomorphism. Every pair $\xi,\zeta\in\widehat{C_d}$ has a
unique decomposition
\[
 \xi(z)=\alpha(z^B)\chi(z^A),\qquad
 \zeta(z)=\eta(z^B)\psi(z^A),
 \quad \alpha,\eta\in\widehat U,\quad\chi,\psi\in\widehat V.
\]
Define the two-character sum and the norm-character exception set by
\begin{equation}\label{eq:inner-pair-sum}
 \begin{aligned}
 S_b(\xi,\zeta)&=\sum_{a\in X_b(K)}\xi(a)\zeta(1+a),\\
 \mathcal E_{\mathrm{norm}}
 &=\{(\alpha\circ(z\mapsto z^B),1):\alpha\in\widehat U\}.
 \end{aligned}
\end{equation}
For every $b\in U$ the sum is
\[
 S_b(\xi,\zeta)=\alpha(b)
       \sum_{a\in X_b(K)}\eta(w)\chi(v)\psi(v_+).
\]
Moreover $(\xi,\zeta)\in\mathcal E_{\mathrm{norm}}$ if and only if
$\eta=\chi=\psi=1$.
\end{auxlemma}
\begin{proof}
The two powers have orders dividing $A$ and $B$, respectively.
An element in the kernel has both its $A$-th and $B$-th powers equal
to one, hence is one because $\gcd(A,B)=1$.
The source and target have the same order $AB$, so the map is an
isomorphism. Taking characters gives the unique decomposition.
On the fiber $a^B=b$; substitution gives the identity for the sum.
Uniqueness also proves the stated equivalence for the exception set.
\end{proof}

\begin{proposition}[Mixed characters on a norm fiber]
\label{prop:inner-mixed-character}
Let $b\in U$ satisfy $b^3\ne1$. For characters
$\eta\in\widehat U$ and $\chi,\psi\in\widehat V$, not all trivial,
\begin{equation}\label{eq:inner-mixed-bound}
 \left|\sum_{a\in X_b(K)}\eta(w)\chi(v)\psi(v_+)\right|
 \le8\sqrt t.
\end{equation}
The product Lang cover used for this sum is geometrically connected,
and hence its smooth projective normalization is geometrically irreducible.
Every character quotient is tame, with conductor degree at most eight.
\end{proposition}
\begin{proof}
Let $C_b^\circ=C_b\setminus(D_x\cup D_y)$, with the eight points of
Lemma~\ref{lem:inner-fiber}. This open curve has
$C_b^\circ(K)=X_b(K)$. Write $\sigma\in\operatorname{Gal}(L/K)$
for $z\mapsto z^t$, extended as $\sigma\otimes1$ on every
$L\otimes_K R$. The algebraic map
\[
 \nu(z)=z\,\sigma(z)
\]
sends the norm-one torus $\ker N_{L/K}$ to
$\mathcal T=\operatorname{Res}_{E/K}(\ker N_{L/E})$:
\[
 N_{L/E}(\nu(z))=N_{L/E}(z)\,\sigma(N_{L/E}(z))=N_{L/K}(z)=1.
\]
Its value on $K$-points is $z^A$. This construction is needed for
the varying norm of $1+a$: exponentiation by $A$ on geometric
points would give relative norm $w^A$, which is not the constant
function one.

Set $w_0=(x+1)(x+b)/x$. The split coordinates of the three
$K$-defined maps to the norm tori are
\[
\begin{array}{c|cc}
 &\text{first coordinate}&\text{second coordinate}\\\hline
 N_{L/E}(1+a)&w_0&w_0^{-1}\\
 \nu(a)&xy&by/x\\
 \nu(1+a)&(x+1)(y+1)&(y+1)(x+b)/x
\end{array}
\]
The first row is a map to $\mathcal U=\ker N_{E/K}$, and
$\mathcal U(K)=U$, $\mathcal T(K)=V$.
On $\mathcal U$ the Frobenius is $z\mapsto z^{-t}$; its Lang
equation is $z^{-A}=w_0$. On $\mathcal T$ the Frobenius is
$(z_0,z_1)\mapsto(z_1^{-t},z_0^t)$; the Lang equations
$z_1^{-t}/z_0=r_0$, $z_0^t/z_1=r_1$ give
$z_0^B=r_1^t/r_0$.
Consequently the product pullback is, over $\overline K$,
\begin{equation}\label{eq:inner-mixed-cover}
 z_U^A=w_0^{-1},\qquad z_1^B=g_1,\qquad z_2^B=g_2,
\end{equation}
where
\begin{equation}\label{eq:inner-mixed-functions}
 g_1=b^{-1}\frac{y^{t-1}}{x^A},\qquad
 g_2=w_0^t\frac{(y+1)^{t-1}}{(x+1)^A}.
\end{equation}
For the second formula, substitute
$x+b=xw_0/(x+1)$ in $r_1^t/r_0$.

These geometric equations inherit their $K$-structure from the
Lang pullbacks. More explicitly, above
$F_{C_b}(x,y)=(b/y^t,x^t)$ their Frobenius sends the three
displayed covering coordinates to
\begin{equation}\label{eq:inner-mixed-frobenius}
 \bigl(w_0z_U,\;xy z_1,\;(x+1)(y+1)z_2\bigr).
\end{equation}
This follows from $F(z)=r z$ in the Lang equations.
It is compatible with \eqref{eq:inner-mixed-cover}, since
\[
 w_0(F_{C_b})=w_0^{-t},\quad
 g_1(F_{C_b})=(xy)^B g_1,\quad
 g_2(F_{C_b})=((x+1)(y+1))^B g_2.
\]
At a rational point $(x,y)=(a,a^t)$, the three deck multipliers
in \eqref{eq:inner-mixed-frobenius} are precisely $w,v,v_+$.
Thus the character component has trace $\eta(w)\chi(v)\psi(v_+)$;
the inverse Frobenius convention simultaneously inverts the
characters and gives the same bound.

We check geometric connectedness and the conductor directly.
The divisors of $w_0,g_1,g_2$ are supported on the eight boundary
points. Their valuations are
\begin{equation}\label{eq:inner-mixed-valuations}
\begin{array}{c|rrr}
 P&\operatorname{ord}_P(w_0)&\operatorname{ord}_P(g_1)&
       \operatorname{ord}_P(g_2)\\\hline
 (0,1)&-1&-A&-1\\
 (0,b^{-1})&-1&-A&-t\\
 (\infty,1)&-1&A&t\\
 (\infty,b^{-1})&-1&A&1\\
 (1,0)&1&t-1&-1\\
 (b,0)&1&t-1&t\\
 (1,\infty)&1&-(t-1)&-t\\
 (b,\infty)&1&-(t-1)&1
\end{array}
\end{equation}
Indeed $x,y$ have simple zeros and poles on $D_x,D_y$;
$x+1$ has simple zeros at $(1,0),(1,\infty)$ and simple poles
at the two points with $x=\infty$, and the corresponding assertion
holds for $y+1$. Substitution in \eqref{eq:inner-mixed-functions}
gives each entry of the table.

For every $m\mid B$, a relation $g_1^r g_2^s=f^m$ in
$\overline K(C_b)^\times$ would imply, at $(0,1)$ and
$(0,b^{-1})$,
\[
 m\mid Ar+s,\qquad m\mid Ar+ts.
\]
Now $\gcd(B,t-1)=\gcd(t^2+1,t-1)=1$ and $\gcd(A,B)=1$.
Subtracting forces $m\mid s$, and then $m\mid r$.
The valuation $-1$ of $w_0$ likewise excludes every nontrivial
Kummer power relation for an order dividing $A$.
One can verify simultaneous independence in a common exponent:
\[
 w_0^{Be_0}g_1^{Ae_1}g_2^{Ae_2}
       \in\overline K(C_b)^{\times AB}
 \quad\Longrightarrow\quad
 A\mid e_0,\ B\mid e_1,\ B\mid e_2.
\]
Reduction of the first two valuations modulo $A$ gives $A\mid e_0$;
their difference modulo $B$ gives $B\mid e_2$, and either valuation
then gives $B\mid e_1$.
This is independence of the relevant functions modulo powers in
$\overline K(C_b)^\times$, verified by their local valuations.

Equivalently, consider the geometric monodromy subgroup of the
product deck group $G=U\times V\times V$.
If a character were trivial on that subgroup, it would be trivial
on both of the above inertia groups. The coprime $A$- and
$B$-parts cannot cancel. The $A$-part first forces $\eta=1$;
the two $B$-equations just proved force $\chi=\psi=1$.
Every proper subgroup of a finite abelian group has a nontrivial
annihilating character. The monodromy subgroup is therefore all
of $G$, proving geometric connectedness of the full product cover
and of every character quotient.

All covering degrees are odd, so wild inertia is trivial.
For a rank-one character its local Artin conductor is one if
the inertia character is nontrivial, and zero otherwise.
Thus its conductor degree is the number $r$ of active rows of
\eqref{eq:inner-mixed-valuations}, and $r\le8$.
Cancellation can occur at individual rows; we do not presume
ramification at every boundary point. For a nontrivial character
triple the inertia test proves geometric nontriviality and $r>0$.
The genus-one Artin-character Weil bound now gives
$(2\cdot1-2+r)\sqrt t\le8\sqrt t$; see
\cite[\S4, Lemma~1]{FFSTV13} and the Lang construction in
\cite[pp.~198--199]{Katz89}.
In cohomological terms, extend over the inactive boundary points.
On the complement of the $r$ active points, $H_c^0,H_c^2$ vanish
and the tame Euler-characteristic formula gives
$\dim H_c^1=2g-2+r=r$.
The eigenvalues have absolute value at most $\sqrt t$, by the
Weil theorem on the character component of the finite cover.
No active boundary point is $K$-rational, so this trace sum is
exactly the sum over $X_b(K)$, with no rational boundary correction.
\end{proof}

\begin{corollary}[The precise two-character exception]
\label{cor:inner-mixed-exception}
Let $b\in U$ satisfy $b^3\ne1$ and let $\xi,\zeta\in\widehat{C_d}$.
Use the character decomposition lemma and \eqref{eq:inner-pair-sum}.
If $(\xi,\zeta)\in\mathcal E_{\mathrm{norm}}$, then
\[
 S_b(\xi,\zeta)=\alpha(b)\#X_b(K).
\]
In every other case $|S_b(\xi,\zeta)|\le8\sqrt t$.
In particular, the assertion for every nontrivial two-character
pair is false: a nontrivial $\alpha\circ N_{L/E}$ with $\zeta=1$
is constant on the norm fiber.
\end{corollary}
\begin{proof}
The decomposition lemma identifies the exception set with the
trivial varying triple. That triple gives the exact constant sum.
Every pair outside the set has a nontrivial varying triple, so
Proposition~\ref{prop:inner-mixed-character} gives the bound.
\end{proof}

\begin{auxlemma}[Local averaging in a cyclic group]
Put
\[
 \begin{aligned}
 \theta_2(n)&=\prod_{p\mid n}(1-p^{-2}),&
 J_b&=\{p\mid A:b\in U^p\},\\
 \lambda_A(b)&=\prod_{p\in J_b}(1-p^{-1}),&
 H(A)&=\prod_{p\mid A}\frac{p+2}{p+1}.
 \end{aligned}
\]
The following are exact averages over all $A$ elements of $U$:
\begin{equation}\label{eq:inner-local-averages}
 \begin{aligned}
  \frac1A\sum_{b\in U}\lambda_A(b)&=\theta_2(A),\\
  \frac1A\sum_{b\in U}\lambda_A(b)2^{|J_b|}
       &=\theta_2(A)H(A).
 \end{aligned}
\end{equation}
In particular the average of $\lambda_A(b)\theta_2(B)$ is
$\theta_2(A)\theta_2(B)=\theta_2(d)$.
\end{auxlemma}
\begin{proof}
Fix a generator $u$ and write $b=u^j$, $j\in\mathbb Z/A\mathbb Z$.
For $p\mid A$ the condition $b\in U^p$ is equivalent to $p\mid j$.
Reduction of uniform $j$ modulo $\operatorname{rad}(A)$ is uniform;
the Chinese remainder theorem makes the residues modulo the distinct
primes independent. The probability of $p\in J_b$ is therefore $1/p$.
The local expectation for $\lambda_A$ is
\[
 (1-1/p)+\frac1p(1-1/p)=1-p^{-2}.
\]
For $\lambda_A(b)2^{|J_b|}$ it is
\[
 (1-1/p)+\frac2p(1-1/p)
       =(1-p^{-2})\frac{p+2}{p+1}.
\]
Multiplication of these independent local expectations proves both
identities. Since $\gcd(A,B)=1$, their prime supports are disjoint,
which proves the last equality.
\end{proof}

\begin{theorem}[Joint generation density at the inner boundary]
\label{thm:inner-joint-density}
Use $\theta_2,\lambda_A,J_b,H(A)$ from the local averaging lemma,
and put $W(n)=2^{\omega(n)}$, $r_0=\gcd(3,A)\le3$.
Let $\mathcal R_{d,b}=\mathcal R_d\cap X_b(K)$.
For every $b\in U$ with $b^3\ne1$,
\begin{equation}\label{eq:inner-joint-fiber}
 \bigl||\mathcal R_{d,b}|-\lambda_A(b)\theta_2(B)A\bigr|
 \le\lambda_A(b)\theta_2(B)
       \bigl(8\,2^{|J_b|}W(B)-6\bigr)\sqrt t.
\end{equation}
For the full family,
\begin{equation}\label{eq:inner-joint-total}
 \bigl||\mathcal R_d|-\theta_2(d)A^2\bigr|
 \le\theta_2(d)A\bigl(8H(A)W(B)-6\bigr)\sqrt t+2r_0A.
\end{equation}
Since $H(A)\le W(A)$, this implies
\[
 |\mathcal R_d|=\theta_2(d)t^2+O(t^{3/2}W(d)),\qquad
 |\mathcal R_d|\sim\theta_2(d)t^2.
\]
The fixed-fiber population is $O(t)$, and its coefficient depends
on $b$. If $b$ is primitive in $U$, then $J_b$ is empty and
the coefficient is $\theta_2(B)$.
Moreover $|T_d-A^2|\le2A\sqrt t+r_0A$, so the actual proportion
of jointly generating slopes among the ordinary intersection is
$|\mathcal R_d|/T_d=\theta_2(d)+O(W(d)/\sqrt t)$.
\end{theorem}
\begin{proof}
The group isomorphism gives
\[
 \langle a,1+a\rangle=C_d
 \quad\Longleftrightarrow\quad
 \langle b,w\rangle=U\ \text{and}\ \langle v,v_+\rangle=V.
\]
For $p\mid A$ with $b\notin U^p$ the first condition is automatic.
For $p\in J_b$ it requires $w\notin U^p$. By orthogonality its
indicator is the product of the factors
\[
 1-\frac1p\sum_{\eta^p=1}\eta(w),\qquad p\in J_b.
\]
Each factor has constant coefficient $1-1/p$ and total absolute
coefficient sum $2(1-1/p)$.
The second condition has indicator
\[
 \prod_{p\mid B}\left(1-\frac1{p^2}
        \sum_{\chi^p=\psi^p=1}\chi(v)\psi(v_+)\right).
\]
Here each factor has constant coefficient $1-1/p^2$ and total
absolute coefficient sum $2(1-1/p^2)$.
Characters belonging to different prime-primary components have
unique products, so multiplying these expansions gives constant
coefficient $c_b=\lambda_A(b)\theta_2(B)$ and total absolute
coefficient sum $c_b2^{|J_b|}W(B)$.
The Hasse error for the trivial triple is $2c_b\sqrt t$;
Proposition~\ref{prop:inner-mixed-character} bounds all other
terms by $8\sqrt t$. This proves \eqref{eq:inner-joint-fiber}.

The local averaging lemma supplies \eqref{eq:inner-local-averages}.
Multiplication by $\theta_2(B)$ turns $\theta_2(A)$ into
$\theta_2(d)$; it also turns the weighted average into
$\theta_2(d)H(A)$. These identities average over all $b\in U$,
before separating the exceptional fibers.

There are precisely $r_0$ exceptional $b$ with $b^3=1$.
For every $b$, each $w\in U$ allows at most two roots of
$X^2+(1+b+w)X+b$. Thus $\#X_b(K)\le2A$ even in an exceptional
fiber. Its contribution differs from the formal main term
$c_bA\in[0,A]$ by at most $2A$.
Sum \eqref{eq:inner-joint-fiber} over the good fibers, bound
the positive error coefficients by their sum over all $b$, and
use the two exact averages. This gives
\eqref{eq:inner-joint-total}. It includes all exceptional and
subfield points, rather than applying the smooth-fiber bound to them.
Finally $W(d)=d^{o(1)}=t^{o(1)}$, while $\theta_2(d)\ge1/2$:
the latter follows by comparison with the telescoping product
$\prod_{n=2}^\infty(1-n^{-2})=1/2$.
Replacing $A^2=(t+1)^2$ by $t^2$ gives the stated asymptotic.
For $T_d$ sum the Hasse bound over the good fibers and use
$|\#X_b(K)-A|\le A$ on each exceptional fiber.
This proves its bound and, by division, the density assertion.
\end{proof}

\begin{theorem}[Double full-order statistics and all-dimensional existence]
\label{thm:inner-double-count}
Define $\theta(n)=\varphi(n)/n$ and
\[
 D_{d,b}=\#\{a\in X_b(K):\operatorname{ord}(a)
                          =\operatorname{ord}(1+a)=d\},\qquad
 D_d=\sum_{b\in U}D_{d,b}.
\]
If $b$ is not primitive in $U$, then $D_{d,b}=0$.
For primitive $b$, put $c=\theta(A)\theta(B)^2$. Then
\begin{equation}\label{eq:inner-double-fiber}
 |D_{d,b}-cA|\le c\bigl(8W(A)W(B)^2-6\bigr)\sqrt t.
\end{equation}
In particular,
\begin{equation}\label{eq:inner-double-total}
 |D_d-\theta(d)^2A^2|
 \le\theta(d)^2A\bigl(8W(A)W(B)^2-6\bigr)\sqrt t,
\end{equation}
and $D_d\sim\theta(d)^2t^2$ as $s\to\infty$.
Define the explicit analytic range
\begin{equation}\label{eq:inner-double-range}
 \mathcal S_{\mathrm{an}}
 =\{s\in\mathbb Z_{\ge2}:A>(8W(A)W(B)^2-6)\sqrt t\},
\end{equation}
with $t=2^s$, $A=t+1$, and $B=t^2+1$.
For every $s\in\mathcal S_{\mathrm{an}}$ and every primitive
$b\in U$, $D_{d,b}>0$. This set contains all sufficiently large
integers $s$. Moreover, $D_d>0$ for every integer $s\ge2$.
\end{theorem}
\begin{proof}
Order $d$ forces $a^B=b$ to have order $A$, which proves the
vanishing assertion. For primitive $b$, the two full-order conditions
are exactly that $w$ is primitive in $U$ and $v,v_+$ are primitive
in $V$. Apply the primitive-character indicator proved in
Theorem~\ref{thm:inner-primitive-count} separately to these three
variables. For a cyclic group of order $n$ it has constant coefficient
$\theta(n)$ and total absolute coefficient sum $\theta(n)W(n)$.
The product therefore has constant coefficient $c$ and total
absolute coefficient sum $cW(A)W(B)^2$.
The trivial triple contributes $c\#X_b(K)$, with Hasse error
$2c\sqrt t$; every other triple has the mixed bound
$8\sqrt t$. This proves \eqref{eq:inner-double-fiber}.
Sum over the $\varphi(A)=A\theta(A)$ primitive norm fibers and
use $\theta(d)=\theta(A)\theta(B)$ to obtain
\eqref{eq:inner-double-total}.
The relative error tends to zero because
$W(A)W(B)^2=t^{o(1)}$. The stated inequality makes the lower
bound positive in every primitive norm fiber.
For all-dimensional existence, Proposition~\ref{prop:inner-diagonal-double}
below gives $D_d\ge\Delta_t>0$ for $s\ge33$, independently of
the preceding three-character sieve. The exact certificates in
Appendix~\ref{app:inner-cert} prove $D_d>0$ for each $2\le s\le32$.
\end{proof}

\begin{proposition}[A trace-one double full-order subfamily]
\label{prop:inner-diagonal-double}
For $t=2^s$, $s\ge2$, use $A=t+1$, $B=t^2+1$ and $d=AB$ as above.
Put
\[
 \Delta_t=\#\{\gamma\in V:\tau=\gamma+\gamma^{-1}\in U,
                 \ \operatorname{ord}(\gamma)=B,
                 \ \operatorname{ord}(\tau)=A\}.
\]
Every element counted by $\Delta_t$ gives, injectively,
\begin{equation}\label{eq:inner-diagonal-construction}
 a=(1+\gamma)^{-1}\in C_d,\qquad
 1+a=a^{t^2},\qquad
 \operatorname{ord}(a)=\operatorname{ord}(1+a)=d.
\end{equation}
In particular $D_d\ge\Delta_t$. For any characters $\eta$ of $U$
and $\chi$ of $V$ with $(\eta,\chi)\ne(1,1)$,
\begin{equation}\label{eq:inner-diagonal-character}
 \left|\sum_{\substack{\gamma\in V\\
                       \gamma+\gamma^{-1}\in U}}
       \eta(\gamma+\gamma^{-1})\chi(\gamma)\right|\le4\sqrt t.
\end{equation}
Consequently
\begin{equation}\label{eq:inner-diagonal-count}
 |\Delta_t-\theta(d)(t+1)|
       \le\theta(d)\bigl(4W(d)-2\bigr)\sqrt t.
\end{equation}
The sufficient condition $\sqrt t\ge4W(d)$ implies $\Delta_t>0$;
it holds for every $s\ge33$ by the integer bounds in
Appendix~\ref{app:inner-cert}.
\end{proposition}
\begin{proof}
\textit{The full-order construction.}\par
Here $\gamma^{t^2}=\gamma^{-1}$ and $\gamma\ne1$.
Thus $a^{t^2}=\gamma/(1+\gamma)=1+a$.
Also
\[
 N_{L/E}(1+\gamma)=\gamma+\gamma^{-1}=\tau,
 \qquad a^B=\tau^{-1},\qquad a^{t^2-1}=\gamma.
\]
Since $N_{E/K}(\tau)=1$, the norm of $a$ to $K$ is one, so
$\operatorname{ord}(a)$ divides $d$. The two displayed powers
force both $A$ and $B$ to divide this order. Their gcd is one,
and hence the order is $d$. The conjugate $1+a$ has the same
order. The formula for $a$ is injective in $\gamma$.

\smallskip\noindent\textit{The curve and its four boundary points.}\par
We analyze the norm fiber $X_1$ directly, rather than applying
Proposition~\ref{prop:inner-mixed-character}, whose good-fiber
hypothesis excludes this parameter. Write its variable as $\gamma$.
Over $\overline K$, the relative norm-one torus has coordinates
$(x,y,x^{-1},y^{-1})$. Its $K$-points have
$x=\gamma$, $y=\gamma^t$, $\gamma\in V$, and its Frobenius is
\[
 F_Y(x,y)=(y^{-t},x^t).
\]
The condition $N_{E/K}(\gamma+\gamma^{-1})=1$ gives the
projective closure $Y_{\overline K}\subset\mathbb P^1\times\mathbb P^1$ of
\begin{equation}\label{eq:inner-diagonal-curve}
 (x+1)^2(y+1)^2=xy.
\end{equation}
Here $Y$ denotes the $K$-curve with the inherited torus descent
$F_Y$, not the split curve equipped with coordinatewise
$t$-power Frobenius. The descent extends to the projective
closure and preserves its boundary. In particular the relation
$y=x^t$ is imposed on $K$-points, not in its geometric function field.
On the affine chart the two partial derivatives are $y$ and $x$;
their only common zero $(0,0)$ is not on the curve. The boundary is
\[
 P_0=(0,1),\quad P_\infty=(\infty,1),\quad
 Q_0=(1,0),\quad Q_\infty=(1,\infty).
\]
At $P_0$, with $u=y+1$, the equation is
$(1+x)^2u^2+x(1+u)=0$, whose derivative with respect to $x$
is one at the point. Thus it is smooth and $v_{P_0}(x)=2$.
Reciprocating $x$ or $y$, and interchanging them, gives the
same smoothness test at the other boundary points.
This proves that the bidegree-$(2,2)$ curve is smooth.
It is geometrically irreducible. Smoothness implies that
the curve is reduced and that distinct irreducible components
would be disjoint. Every component has a nonzero effective
bidegree $(a_i,b_i)$, with $a_i,b_i\ge0$ and
$\sum_i(a_i,b_i)=(2,2)$. If one component has both entries
positive, its intersection $a_ib_j+a_jb_i$ with every other
component is positive. If no component has both entries
positive, the sum $(2,2)$ forces a pure vertical component
and a pure horizontal component, whose intersection is again
positive. Both possibilities contradict disjointness.
Adjunction on $\mathbb P^1\times\mathbb P^1$ now gives genus
$(2-1)(2-1)=1$.
Frobenius permutes the four boundary points in the cycle
\[
 P_0\longmapsto Q_0\longmapsto P_\infty
      \longmapsto Q_\infty\longmapsto P_0.
\]
There is no $K$-rational boundary point. Therefore the open curve
$Y^\circ$ has exactly the points in the sum
\eqref{eq:inner-diagonal-character}, and
$|\#Y^\circ(K)-(t+1)|\le2\sqrt t$ by Hasse--Weil.

\smallskip\noindent\textit{Actual Lang covers and their character traces.}\par
Let $\mathcal U=\ker N_{E/K}$ and
$\mathcal V=\operatorname{Res}_{E/K}(\ker N_{L/E})$;
their $K$-point groups are $U$ and $V$. On $Y^\circ$ use the
maps $\tau=\gamma+\gamma^{-1}$ to $\mathcal U$ and $\gamma$
to $\mathcal V$ itself. Write
\[
 w_0=(x+1)^2/x,\qquad h=y^t/x.
\]
The split coordinates of $\tau$ are $(w_0,w_0^{-1})$.
The two Lang pullbacks, with their inherited $K$-structures, are
\begin{equation}\label{eq:inner-diagonal-lang}
 z_U^A=w_0^{-1},\qquad z_V^B=h.
\end{equation}
For the first, the Lang equation is $z_U^{-t}/z_U=w_0$.
For the second, the split equations are
$z_1^{-t}/z_0=x$, $z_0^t/z_1=y$; elimination gives
$z_0^B=y^t/x$, with $z_V=z_0$.
Thus the actual functions are $w_0^{-1}$ and $h$, not merely
a geometrically convenient Kummer model.
Above $F_Y$, Frobenius on the two covering coordinates is
\[
 (z_U,z_V)\longmapsto(w_0z_U,xz_V).
\]
This follows from the split Lang equations. It also respects
\eqref{eq:inner-diagonal-lang}, since
$w_0(F_Y)=w_0^{-t}$ and $h(F_Y)=x^Bh$.
At a $K$-point the deck multipliers are exactly
$\tau$ and $\gamma$. Choosing the character convention for
these multipliers gives trace $\eta(\tau)\chi(\gamma)$;
the inverse convention just inverts both characters.

\smallskip\noindent\textit{Geometric connectedness and conductor.}\par
The complete boundary valuation table is
\begin{equation}\label{eq:inner-diagonal-valuations}
\begin{array}{c|rr}
 &w_0&h\\\hline
 P_0&-2&-2\\
 P_\infty&-2&2\\
 Q_0&2&2t\\
 Q_\infty&2&-2t
\end{array}
\end{equation}
For example $x+1$ has simple zeros at $Q_0,Q_\infty$ and
a double pole at $P_\infty$; $y$ has a double zero at $Q_0$
and a double pole at $Q_\infty$. These observations give every
entry of the table.
Suppose for $0\le e_0<A$, $0\le e_1<B$ that
\[
 (w_0^{-1})^{Be_0}h^{Ae_1}
       \in\overline K(Y)^{\times AB}.
\]
Its valuation at $P_0$ is $2Be_0-2Ae_1$.
Reduction modulo $A$ and modulo $B$, using that $A,B$ are
odd and coprime, gives $A\mid e_0$ and $B\mid e_1$.
This single valuation separates the two cyclic components
because reduction modulo each order kills the other component.
Thus $e_0=e_1=0$. The Kummer criterion proves that the
product cover in \eqref{eq:inner-diagonal-lang} is geometrically
connected with full group $U\times V$; in particular every
nontrivial character quotient is geometrically nontrivial.

All cover degrees are odd, so the ramification is tame.
At every boundary point the valuation of $w_0^{-1}$ is a unit
modulo $A$, and that of $h$ is a unit modulo $B$.
A nontrivial character of either group is therefore ramified
there. The two inertia characters cannot cancel, because their
orders divide the coprime integers $A$ and $B$.
Hence every nontrivial pair is ramified at all four points,
with Swan conductor zero and local Artin conductor one.
Its total conductor is exactly four, and it is unramified on
$Y^\circ$.
The associated rank-one finite-monodromy sheaf is pure of weight
zero and geometrically nontrivial. Thus $H_c^0=H_c^2=0$, and
Grothendieck--Ogg--Shafarevich gives
$\dim H_c^1=2g(Y)-2+4=4$.
The classical curve character bound
\cite[Lemma~1]{FFSTV13}, with the Lang construction as in
\cite{Katz89}, bounds each Frobenius eigenvalue by $\sqrt t$.
This proves \eqref{eq:inner-diagonal-character}.

\smallskip\noindent\textit{The two primitive indicators and positivity.}\par
Apply the primitive-character indicator to $\tau\in U$ and
$\gamma\in V$. Their product has constant coefficient
$\theta(A)\theta(B)=\theta(d)$ and total absolute coefficient
sum $\theta(d)W(A)W(B)=\theta(d)W(d)$.
The trivial pair has Hasse error $2\theta(d)\sqrt t$.
The other pairs have total coefficient mass
$\theta(d)(W(d)-1)$ and character bound $4\sqrt t$.
Their sum is exactly the error in \eqref{eq:inner-diagonal-count}.
If $\sqrt t\ge4W(d)$, then
$(t+1)-(4W(d)-2)\sqrt t>0$, proving positivity.
For $33\le s\le113$, the complete integer certificates in
Appendix~\ref{app:inner-cert} give
$\omega(d)\le r_s$ with $s\ge4+2r_s$, hence this condition.
For $s\ge114$, the same appendix proves for every odd $n$ that
$W(n)<4096n^{1/8}$. Since $d<2t^3$,
\[
 (4W(d))^8<2^{113}t^3<t^4=(\sqrt t)^8.
\]
These two ranges prove $\Delta_t>0$ for every $s\ge33$.
\end{proof}

The construction \eqref{eq:inner-diagonal-construction} is the
classical trace-one reciprocal-trace change of variable
\cite[\S4]{Coh}, applied here with the additional condition
$N_{E/K}(\tau)=1$ and the smaller exact order $A=t+1$.
The estimate established above concerns this specified fiber;
the Frobenius identity itself is not a priority claim.
It also implies
$\operatorname{Tr}_{L/K}(a)=(a+a^{t^2})+(a^t+a^{t^3})=1+1=0$,
so these particular slopes are not normal over $K$.

The three populations $|\mathcal R_d|$, $N_d^{\mathrm{prim}}$
and $D_d$ have different main terms. Theorem~\ref{thm:inner-double-count}
now gives $D_d>0$ for every $s\ge2$, using the trace-one subfamily
of Proposition~\ref{prop:inner-diagonal-double} for $s\ge33$
and the exact double-order certificates for $2\le s\le32$.
This subfamily has a linear main term $\theta(d)(t+1)$; it does
not replace the quadratic full-family main term
$\theta(d)^2(t+1)^2$. Nor does all-dimensional existence assert
positivity in every primitive norm fiber at small $s$.
Indeed $\Delta_t=0$ at $s=3,5$; the finite certificates at these
parameters use slopes outside this trace-one subfamily.


```

## Part VI — 本条主线的当前范围

Mixed Character → Joint Generation Density → Double Primitive Count 已由完整证明闭合。
固定纤维总体为 O(t)，全参数总体为 O(t²)；固定系数 λ_A(b)θ₂(B) 与全参数系数 θ₂(d) 不可混用。
全维双满阶现已闭合：Theorem 5.24、Proposition 5.25 及计算附录完整覆盖全部参数。
原单斜率全维 Theorem 5.20 继续成立。当前研究按交接要求仅沿本条主线推进。

## Part VII — Mixed Character → Density 的完整证明

正文新增 Proposition 5.21、Corollary 5.22、Theorems 5.23–5.24；
完整中文推导、证明依赖与漏洞边界见 `PaperA_Mixed_Character_Proof_and_Density.md`，
英文全部证明已包含于 Part V 及 `inner_mixed_character_section.tex.inc`。
`verify_inner_mixed.py` 实际核验双满阶证书 s=2..32 和全部范数纤维 s=2..6。
先前外部审查与四阶对称记录保存在 `Review_Response_2026-10-12.md` 及旧版本备份。


## Part VIII — 前轮投稿收紧（历史记录）

5.21–5.24 编号保持；新增具名辅助引理明确唯一角色分解和例外集合，
以及两条精确有限平均。平均 λ_A 为 θ₂(A)，乘以 θ₂(B) 才得到 θ₂(d)。
幂关系的独立性位于函数域乘法群模幂，不能表述为 Picard 群中主除子的独立性。
双满阶解析范围记为 S_an，已覆盖范围为 {2,…,32}∪S_an；全 s≥2 仍开放。
逐项审查、原文行号及文献边界见 PaperA_Submission_Stress_Audit.md。

## Part IX — 双满阶全维闭合

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

