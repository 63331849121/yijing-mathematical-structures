# Paper A：双满阶全维存在性闭合

日期：2026-10-12。版本：`paperA-revised-2026-10-12-double-full-order-closure`。

## 1. 正式结论

**Theorem 5.24（增强）**：对每个整数 $s\ge2$，令

\[
t=2^s,\quad K=\mathbb F_t,\quad E=\mathbb F_{t^2},\quad
L=\mathbb F_{t^4},\quad d=(t+1)(t^2+1).
\]

则 $C_d=\ker N_{L/K}$ 中存在元素 $a$，使

\[
\operatorname{ord}(a)=\operatorname{ord}(1+a)=d.
\]

`Q-scalar-inner-both-primitive`、`P-scalar-inner-double-effective-all`：
**已证（依赖外部定理）**。原双满阶全参数主项与误差不变。
新增 Proposition 5.25（`prop:inner-diagonal-double`）提供独立的有效存在性证明。
Singer 应用顺延为 Theorem 5.26；5.21–5.24 编号保留。

这一结论用无限解析证明和完全覆盖的有限精确证书拼合，不是有限数据外推。

## 2. 核心归约：让两个满阶条件互为共轭

记 $A=t+1$、$B=t^2+1$、$U=\ker N_{E/K}=C_A$、
$V=\ker N_{L/E}=C_B$。两阶互素且均为奇数。
选择 $\gamma\in V$，要求

\[
\tau=\gamma+\gamma^{-1}\in U,\qquad
\operatorname{ord}(\gamma)=B,\quad\operatorname{ord}(\tau)=A.
\]

取 $a=(1+\gamma)^{-1}$。因为 $\gamma^{t^2}=\gamma^{-1}$，

\[
a^{t^2}=\frac{\gamma}{1+\gamma}=1+a,
\qquad a^B=\tau^{-1},\qquad a^{t^2-1}=\gamma.
\]

又 $N_{L/K}(a)=N_{E/K}(\tau^{-1})=1$，故 $\operatorname{ord}(a)\mid AB$。
两个幂的阶分别为 $A$、$B$，迫使 $\operatorname{ord}(a)=AB$。
共轭项 $1+a$ 同阶。构造关于 $\gamma$ 单射。
这样只需同时筛 $\tau$ 与 $\gamma$，不必筛三个独立变量。

设满足上述两个满阶条件的 $\gamma$ 数为 $\Delta_t$。则 $D_d\ge\Delta_t$。

## 3. 特殊范数纤维的完整几何证明

此处直接研究 $X_1$，不能援用要求 $b^3\ne1$ 的 Proposition 5.21。
在代数闭包上的分裂坐标 $x,y$ 中，曲线为以下模型；仅在 $K$-有理点
才有 $x=\gamma,y=\gamma^t$。模型配备范数环面给出的 $K$-下降结构。

\[
Y:\ (x+1)^2(y+1)^2=xy\ \subset\mathbb P^1\times\mathbb P^1.
\]

Frobenius 为 $F_Y(x,y)=(y^{-t},x^t)$。四个边界点是

\[
P_0=(0,1),\ P_\infty=(\infty,1),\quad
Q_0=(1,0),\ Q_\infty=(1,\infty).
\]

仿射偏导为 $y,x$，共同零点不在曲线上。边界处以 $u=y+1$ 为例，
方程为 $(1+x)^2u^2+x(1+u)=0$，对 $x$ 的偏导在 $P_0$ 为 $1$。
互换及倒数坐标处理另三点。因此整个双次数 $(2,2)$ 曲线光滑。
若几何可约，光滑曲线的不同分量须不相交；但总类为 $(2,2)$ 的
有效分量不能两两不交，因交数为 $ad+bc$。故几何不可约，伴随公式给亏格 $1$。

四点构成 Frobenius 四循环 $P_0\to Q_0\to P_\infty\to Q_\infty\to P_0$，
无 $K$-有理边界点，因此开放曲线的点数与射影曲线完全相同，
Hasse 误差为 $2\sqrt t$。

## 4. 实际 Lang 覆盖、赋值和导子

环面映射使用 **$\tau$ 与 $\gamma$ 本身**。设

\[
w_0=(x+1)^2/x,\qquad h=y^t/x.
\]

对 $\mathcal U=\ker N_{E/K}$ 与
$\mathcal V=\operatorname{Res}_{E/K}\ker N_{L/E}$ 的 Lang 拉回为

\[
z_U^A=w_0^{-1},\qquad z_V^B=h.
\]

第二式由 $z_1^{-t}/z_0=x$、$z_0^t/z_1=y$ 消元得到。
覆盖 Frobenius 为

\[
(z_U,z_V)\longmapsto(w_0z_U,xz_V),
\]

满足 $w_0(F_Y)=w_0^{-t}$、$h(F_Y)=x^Bh$。有理点的 deck 乘子
正是 $\tau,\gamma$，故与要估计的角色迹一致。

| 点 | $v(w_0)$ | $v(h)$ |
|---|---:|---:|
| $P_0$ | −2 | −2 |
| $P_\infty$ | −2 | 2 |
| $Q_0$ | 2 | $2t$ |
| $Q_\infty$ | 2 | $−2t$ |

注意这里的重数是 **2**。若

\[
(w_0^{-1})^{Be_0}h^{Ae_1}\in\overline K(Y)^{\times AB},
\quad 0\le e_0<A,\ 0\le e_1<B,
\]

在 $P_0$ 取赋值得 $AB\mid2Be_0-2Ae_1$。分别模 $A$、$B$
即得 $e_0=e_1=0$。Kummer 判据给出全乘积几何单值群，因而覆盖几何连通。

每个边界点的两个赋值分别是模 $A$、$B$ 的单位。任意非平凡角色对
在每个边界点均非平凡分歧；两个分量的阶互素，不能抵消。覆盖次数奇数，
故均为温和分歧；Swan 为 $0$，局部 Artin 导子为 $1$，总导子 **恰为4**。
相应秩一层几何非平凡、权 $0$，$H_c^0=H_c^2=0$，
GOS 给 $\dim H_c^1=2g-2+4=4$。经典曲线 Weil 界由此给

\[
\left|\sum_{\gamma\in V,\ \gamma+\gamma^{-1}\in U}
\eta(\gamma+\gamma^{-1})\chi(\gamma)\right|\le4\sqrt t
\quad((\eta,\chi)\ne(1,1)).
\]

这是一段独立证明，没有从一般纤维的单角色或三角色论证省略推导。

## 5. 两项筛与三个完整参数区间

两个本原角色指标的常数系数是 $\theta(A)\theta(B)=\theta(d)$，
系数绝对值总和为 $\theta(d)W(d)$。平凡角色 Hasse 误差与非平凡界相加，得

\[
\boxed{|\Delta_t-\theta(d)(t+1)|
\le\theta(d)(4W(d)-2)\sqrt t.}
\]

因此 $\sqrt t\ge4W(d)$ 足以推出 $\Delta_t>0$。覆盖情况如下：

| 区间 | 依据 | 本轮核验 |
|---|---|---|
| $2\le s\le32$ | 31份既有双满阶域塔证书 | 重新逐一检查两项精确阶、域塔与递归 Lucas 素数证书 |
| $33\le s\le113$ | 81个整数上界 $\omega(d)\le r_s$，$s\ge4+2r_s$ | 每个小因子、余数及整数幂比较均独立复核 |
| $s\ge114$ | 对一切奇数 $n$，$W(n)<4096n^{1/8}$ | 统一常数的53个小素数及精确整数比较已复核；无限范围用纸面不等式 |

中间段仅试除所有不大于4096的素数。余数每个素因子至少4097，
若 $4097^k\le R<4097^{k+1}$，则其不同素因子数至多 $k$。
这不要求大余数为素数，不要求完全分解。

统一常数：令 $P$ 为53个小于256的奇素数之积，精确检查
$256^{53}<4096^8P$。任意奇数 $n$ 满足

\[
W(n)^8/n\le256^{53}/P<4096^8.
\]

又 $d<2t^3$，故当 $s\ge114$ 时

\[
(4W(d))^8<2^{113}t^3<t^4=(\sqrt t)^8.
\]

三个区间不留空缺，故全维结论成立。新增 
`P-scalar-inner-double-omega-tail` 为 **已验证（计算，s=33..113）**。

## 6. 证明依赖、风险和范围

- Lang 覆盖和有限域角色层：经典工具，见
  [Katz 1989, pp.198–199](https://web.math.princeton.edu/~nmk/old/estcharsums.pdf)。
- 曲线角色界及导子方法：经典工具，见
  [Farashahi 等作者稿 §4](https://www.normalesup.org/~tibouchi/papers/welldistributed.pdf)。
  本文显式核实几何非平凡、温和性及导子；不声称新的一般 Weil 定理。
- 本原角色指标：正文 Theorem 5.19 中的既有证明；有限证书的素性是确定性 Lucas 认证。
- **未作 Lean 形式化**。几何证明经本轮纸面逐项核查，算术部分有独立验证器及完整日志。
- **不声称所有范数纤维都在小维有双满阶点**；结论是存在某一纤维。
- **不声称特殊子族全维非空**：$\Delta_t=0$ 在 $s=3,5$；这两维用非对角证书。
- 线性子族主项 $\theta(d)(t+1)$ 与全参数二次主项 $\theta(d)^2(t+1)^2$ 均保留。
- 无有限计算的统一构造、一般指数分类、具体文献优先权仍未解决；它们不阻塞当前全维存在定理。
- 当前文件就地修改，编译状态与源哈希由 `Double_Full_Order_Final_Audit.json` 记录。

## 7. 交付与复现

- 正文 `PaperA_revised.tex`：Theorem 5.24、Proposition 5.25、计算附录。
- 插入片段 `inner_diagonal_double_section.tex.inc` 与 `inner_double_omega_appendix.tex.inc`。
- 完整证明账本新增三条 ID，并关闭 `Q-scalar-inner-both-primitive`。
- 数据 `inner_double_omega_certificates.json`；原31份双满阶证书未改。
- 独立复核：`python verify_inner_double_all.py`，须不使用 `-O`。
- 输出 `inner_double_all_verification.json`、`inner_double_all_run.log`、
  `double_all_verification_environment.json`。
- 修改前69项配套资料已保存在 `backups/before_double_closure/`；
  本轮逐行差异为 `PaperA_double_closure.diff`。



## 8. 本轮后的归属与几何表达修订（2026-10-12）

当前题名与引言已突出全维双满阶结论及密度主线。Proposition 5.25 的
方程是在代数闭包上的双次数模型，K-结构由扭曲 Frobenius 决定；
正文现明确此点，并展开有效分量交数的几何不可约证明。
Cohen 2003 §4 已有互反迹与迹一的分式线性归约。
Frobenius 耦合不是本稿首次提出的一般技巧。
本稿进一步要求 τ=γ+γ⁻¹ 的精确阶为 t+1，且 N_{E/K}(τ)=1；
Cohen Theorem 1.5 在 q=t² 下给出的阶为 t²−1，不能直接替代此要求。
四点导子及指定纤维的有效计数属于此处证明的具体内容。
完整文献边界见 PaperA_Submission_Narrative_and_Priority_Audit.md；
全维结论与 s=2..32、33..113、s≥114 的覆盖不改。
