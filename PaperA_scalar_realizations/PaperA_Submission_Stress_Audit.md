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

# Paper A 投稿前核心证明压力审查

日期：2026-10-12。历史审查版本：paperA-revised-2026-10-12-submission-tightening。

审查对象为当前编辑器中的 PaperA_revised.tex，核心范围为
Proposition 5.21、Corollary 5.22、Theorems 5.23–5.24 及其依赖。
以下采用代数、有限域数论、组合定位三种审稿视角，均由本轮同一审查完成；
它们不是三名独立专家的意见，也不是任何期刊的审稿决定。

## 1. 本轮判断与下一步

逐项复核后，未发现足以推翻这四个结果的反例或未闭合的内部证明步骤。
这个判断限于下列检查，不能替代独立专家审查，也不能证明文献首次性。
本轮修改主要补清表达、平均过程和存在范围；没有增加新的研究分支。

下一步最有价值的工作是完成**最接近文献的逐定理直接推论检验**：
将对象、参数、范数约束、几何假设、主项和误差逐一对齐，判断本文的
具体结论是否已经包含在既有结果中。完成这一步后，再确定最终题名、
引言贡献列表及投稿目标。正面的评分或模拟决定不能代替这张对照表。

本轮内置编译与静态核对结果见 Submission_Tightening_Final_Audit.json。
当前源文件已由内置编译器两次成功编译；93 个标签、196 处引用均可解析，
英文摘要与源文经明确数学符号转换逐句一致，两份表单及全部插入片段同步。
当前编辑器保持打开；没有创建另一份论文或单独导出 PDF。

工作副本及审查资料：D:/project/codex/Yishu01/_review_2026-10-12/。
修改前快照：该目录的 backups/before_submission_tightening/，包含原 66 项文件、
SHA-256 清单及证明台账。基线源文 SHA-256 为
da8842f0d9c785dc2f3ab700d33b9247a06bf44aa9e5caa5d6dab7c7a976e79f。

## 2. 先纠正参考反馈中的数学误述

### 2.1 平均系数

正确的是

\[
\frac1A\sum_{b\in U}\lambda_A(b)=\theta_2(A),\qquad
\frac1A\sum_{b\in U}\lambda_A(b)\theta_2(B)=\theta_2(d).
\]

不能省去第二式中的 θ₂(B)，也不能把第一式的右端改成 θ₂(d)。
上一版正文的两条求和式本来正确；本轮把它们提成具名辅助引理，
并用生成元指数和 CRT 证明，便于单独审查。

### 2.2 独立性的所在群

主除子 div(f) 的线丛同构于平凡线丛，因此其 Picard 类为零。
不能声称 div(a)、div(1+a) 在 Picard 群中独立。
本文所用的是函数域乘法群模幂中的 Kummer 独立性，由局部赋值排除幂关系。
除子类群对主除子的商定义及光滑曲线上的 Picard–除子类对应可参见
[Stacks 的除子定义](https://stacks.math.columbia.edu/tag/0BE0)和
[Picard–除子类对应](https://stacks.math.columbia.edu/tag/02SI)。

### 2.3 已经存在的内容

- 八点赋值表已经在 Proposition 5.21 的正文证明中，当前源文第 1769 行。
- 两角色常值例外已经在 Corollary 5.22 分类，本轮进一步定义显式集合 E_norm。
- 旧标题是 “Double full-order count”，并非反馈假定的标题。
  本轮改成 “Double full-order asymptotics and eventual existence”。
- Theorem 5.20 的全维存在是**单斜率**满阶；其 s≥33 的阈值不能用于双满阶。

## 3. 固定定义与证明状态

\[
t=2^s\ (s\ge2),\quad K=\mathbb F_t,\quad E=\mathbb F_{t^2},\quad
L=\mathbb F_{t^4},\quad A=t+1,\quad B=t^2+1,\quad d=AB.
\]

U=C_A=ker N_{E/K}，V=C_B=ker N_{L/E}，C_d=ker N_{L/K}，gcd(A,B)=1。

\[
X_b(K)=\{a\in L:N_{L/E}(a)=b,\ N_{L/K}(1+a)=1\},\quad b\in U,
\]

w=(1+a)^B、v=a^A、v₊=(1+a)^A。好纤维条件是 b³≠1，不要求 b 本原。

| 台账 ID | 状态 | 当前证明位置 |
|---|---|---|
| P-scalar-inner-character-decomposition | 已证 | 5.21 前 Character decomposition 辅助引理，第 1651 行 |
| P-scalar-inner-mixed-character | 已证（依赖外部定理） | Proposition 5.21、Corollary 5.22，第 1687、1846 行 |
| P-scalar-inner-local-averaging | 已证 | 5.23 前 Local averaging in a cyclic group 辅助引理，第 1865 行 |
| P-scalar-inner-fixed-density | 已证（依赖外部定理） | Theorem 5.23、eq:inner-joint-fiber，第 1912 行 |
| P-scalar-inner-family-density / Q-scalar-inner-joint-count | 已证（依赖外部定理） | Theorem 5.23、eq:inner-joint-total，第 1918 行 |
| P-scalar-inner-double-count | 已证（依赖外部定理） | Theorem 5.24，第 1990 行 |
| P-scalar-inner-double-certificates | 已验证（计算） | 前轮独立核验：双满阶 s=2..32；全部范数纤维 s=2..6 |
| Q-scalar-inner-both-primitive | 开放 | 全 s≥2 双满阶存在；不是现有渐近定理的依赖 |

两条辅助引理先在 _证明台账.md 登记待核，完成纸面证明后更新为已证。
它们明确化既有步骤，不单列为新的原创贡献。5.21–5.24 的编号保持。

## 4. 代数审稿视角：统计对象是否真的实现本原群？

审查链条：一般仿射群公式 → 标量特化 → 联合生成条件 → 本原性。

对 f(x)=ax+c、c≠0，乘子部分是 ⟨a,(1+a)⁻¹⟩=⟨a,1+a⟩。
若它为 C_d，则 C_d 包含于 F₂[a]^×。L 的任何真子域大小至多 t²，
而 d=(t+1)(t²+1)>t²−1，故 F₂[a]=L。于是平移模为 L，
生成群为 L⁺⋊C_d，且 C_d 不可约，仿射作用本原。
不需要另行假设 a 自己已经满阶；这是联合生成与单满阶的区别。

因此 R_d 的斜率确实对应目标群。论文数量公式计数斜率 a；
若计数实现映射，还须按此前的非零平移与共轭计数公式转换，
不能把斜率数量直接称为所有仿射映射数量。

**本视角结论：** 未发现群结构特化与统计条件之间的缺口。
一般半直积、不可约性判据和循环群生成概率属于经典机制；
具体伴随约束与范数族的应用才是本稿需要比较的对象。

## 5. 有限域数论审稿视角：逐项攻击混合角色界

### 5.1 角色覆盖与例外集合

有限群同构 z↦(z^B,z^A) 的核平凡，源、目标同阶 AB，故为同构。
取对偶即得到唯一分解

\[
\xi(z)=\alpha(z^B)\chi(z^A),\qquad
\zeta(z)=\eta(z^B)\psi(z^A).
\]

固定纤维上 S_b=α(b)Ση(w)χ(v)ψ(v₊)。恰当的例外集合为
E_norm={(α∘(z↦z^B),1):α∈Û}，包含平凡角色对。
集合内的和精确为 α(b)#X_b；集合外的变化三元组非平凡，才应用 8√t 界。
如果原角色来自 L^×，应先限制到 C_d，再做此分类。

### 5.2 代数映射与下降

实际使用 ν(z)=zσ(z)，其中 σ∈Gal(L/K) 并延拓为 σ⊗1。
它在 K-点上给出 z^A，同时作为代数映射落入所需范数环面。
直接在几何点上把 (1+a)^A 当作相对范数一函数，会丢失范数耦合项。

实际 Lang 函数和 Frobenius 下降在第 1739、1750 行：

\[
w_0=(x+1)(x+b)/x,\quad
g_1=b^{-1}y^{t-1}/x^A,\quad
g_2=w_0^t(y+1)^{t-1}/(x+1)^A.
\]

覆盖 z_U^A=w₀⁻¹、z₁^B=g₁、z₂^B=g₂ 有由 Lang 拉回继承的 K-结构。
Frobenius 的三个乘子为 w₀、xy、(x+1)(y+1)，在 K-点上就是 w、v、v₊。
字符表示取与此一致的迹约定；若改用逆 Frobenius，字符同时取逆，估计不变。
裸 Kummer 方程本身不代替这一步迹识别。

### 5.3 几何连通性

对 m|B，首两个边界点给出

\[
g_1^r g_2^u=f^m\Longrightarrow m\mid Ar+u,\quad m\mid Ar+tu.
\]

gcd(B,t−1)=gcd(B,A)=1，故 m|u、m|r。
w₀ 的 −1 赋值排除 A 分量的非平凡幂关系。
在共同指数 AB 下，首两行也排除全部同时关系：
先模 A 得 A|e₀，再模 B 的行差得 B|e₂，最后得 B|e₁。
等价的惯性角色检验说明几何单值群在 U×V×V 中没有非平凡湮灭角色，
因而是整个乘积群。几何连通的有限 étale 开覆盖在光滑曲线上几何不可约；
其光滑完备规范化亦然。

这里没有把 P¹ 上的单赋值论证直接移植为 X_b 上的结论，
也没有在 Picard 群中使用不存在的主除子独立性。

### 5.4 分歧和导子

覆盖次数均为奇数，特征为二，故分歧温和、Swan 导子为零。
秩一字符在每个活动边界点的 Artin 导子为一，非活动点为零。
八点以外函数均为单位，没有其他分歧；总导子 r≤8。
部分点可以抵消；两个惯性方程保证非平凡三元组不能在全部点抵消。
因此没有把所有混合字符的导子误写成“恰为八”。

延拓过非活动点，几何非平凡性使 H_c² 消失，非完备性使 H_c⁰ 消失。
温和 Euler 特征公式给出 dim H_c¹=2g−2+r=r，Weil 特征根界给出 r√t。
边界没有 K-点，所以没有另需加入的有理边界误差项。
经典依据是 [Farashahi 等作者稿 §4、Lemma 1](https://www.normalesup.org/~tibouchi/papers/welldistributed.pdf)
中的 Artin 字符和界，以及 [Katz pp.198–199](https://web.math.princeton.edu/~nmk/old/estcharsums.pdf)
的 Lang 角色层构造；本文另行验证几何非平凡性和导子。

**本视角结论：** 对规定的角色与好纤维，覆盖、迹、几何连通性和导子链条闭合。
这并不把经典 Weil–Lang 方法变成新的通用角色和定理。

## 6. 两种筛、平均与误差的重新推导

每个 p-primary 字符分量相互独立，乘积展开中的字符表示唯一。
设常数系数 c、绝对系数总和 cM。平凡项的 Hasse 误差为 2c√t，
其他项合计至多 8c(M−1)√t，故总误差为 c(8M−6)√t。

| 计数 | 固定好纤维的 c | M | 纤维总体 |
|---|---|---|---|
| 联合生成 R_{d,b} | λ_A(b)θ₂(B) | 2^{|J_b|}W(B) | O(t) |
| 双满阶 D_{d,b}，b 本原 | θ(A)θ(B)² | W(A)W(B)² | O(t) |

联合生成在 V 部分逐素数排除“两个分量同时为 p 次幂”，
不是分别强迫两个分量都本原。其常数为 1−p⁻²，绝对系数总和为两倍该常数，
所以总误差只有 W(B)；双满阶分别筛两次，才出现 W(B)²。

固定 b=u^j 时 b∈U^p 等价于 p|j。均匀 j 的模 p 条件由 CRT 独立，
两条精确平均分别为 θ₂(A) 与 θ₂(A)H(A)。**平均的是全部 b∈U，
不是仅好纤维或仅本原 b。**乘上 θ₂(B) 才得到 θ₂(d)。

好纤维的误差系数均非负，可以用全部 b 的加权平均作上界。
至多 r₀=gcd(3,A) 个例外纤维各有至多 2A 点，其实际贡献与形式主项的差
至多 2A，因而全参数误差包含 2r₀A。b=1 的边界合并不代表模型奇异；
本轮仍将它统一纳入例外误差，不套用八点表。

双满阶只在本原 b 上非零；本原 b 的数量为 φ(A)=Aθ(A)，
乘上 θ(A)θ(B)²A 得到 θ(d)²A²。这里不存在把 θ₂ 与 θ 混用的步骤。

W(A)W(B)²=t^{o(1)}，双满阶相对误差趋零；该论证无需 θ(d) 有正常数下界。
联合生成的主项还可用 θ₂(d)≥1/2 控制相对误差。

## 7. 存在范围与组合解释

Theorem 5.24 的解析范围是

\[
\mathcal S_{\rm an}=\{s\ge2:2^s+1>
(8W(2^s+1)W(2^{2s}+1)^2-6)2^{s/2}\}.
\]

每个 s∈S_an 的每个本原范数纤维都有双满阶斜率。
它包含所有充分大的整数 s；本轮没有给出独立的统一数值截点。
结合旧证书，已覆盖 {2,…,32}∪S_an；不能未经验证说该并集就是全部 s≥2。
全维单满阶结论不依赖此遗漏，全维双满阶也不作为现有渐近结果的前提。

从组合视角，R_d/T_d 是普通交集中满足联合生成的比例。
这比普通交数更细；但“密度”本身不是新颖性证据，标准循环群因子也不是新发现。
所证的是这些特定筛的统计及字符和界，不能据此声称所有可能事件都独立，
或整个三变量分布在总变差意义下接近乘积均匀分布。

## 8. 文献边界：已核实与尚需比较

| 经典来源 | 本轮实际检查 | 对本文的准确影响 |
|---|---|---|
| Katz 1989 | 作者全文 pp.198–199 | Lang 与角色层、温和 Euler 特征是经典工具；其直线主定理不自动验证本稿亏格一纤维的全部假设 |
| Farashahi 等 2013 | 作者稿 §4 Lemma 1 | 亏格/导子平方根界是外部经典定理；本稿提供适用条件的验证 |
| [Cohen–Kapetanakis–Reis 2022](https://comptes-rendus.academie-sciences.fr/mathematique/item/10.5802/crmath.328.pdf) | 正式版 Proposition 13、Theorem 16、Corollary 17、Remark 18 | 本原/指定阶指标、角色非退化检验与筛已有先例；不能把指标方法或循环概率列为原创 |
| [Chatterjee 等作者预印本 v3](https://arxiv.org/pdf/2401.01819) | 定义、Lemma 3.5、Theorem 4.1 | 此版 Th.4.1 要求 n>2m，n=4,m=2 不满足；其 primitive 指整个乘法群本原。该特定定理不直接给本稿结论，仍须核对正式版及其他定理 |
| Choudhary–Sharma 2025 | 上轮已查 Th.1 与范数归约，来源见 Literature_Audit_scalar_realization.md | 上轮代入 q=t,n=4,m=2 后充分条件不为正；只能排除该条件直接适用，不能排除其方法的改进 |
| Kudo–Nogata 2026 | 上轮已查 Prop.4.3，来源见 Literature_Audit_scalar_realization.md | 普通范数交数 T_d 已有来源；必须比较附加联合生成及双满阶条件，不能声称整个普通交数是新结论 |

建议完成一个有界的文献对照任务：

1. 对 CKR22 的曲线筛及 Remark 18，明确在本稿范数环面下降后能否直接推出同一混合界与显式常数。
2. 对指定范数/指定阶级数文献的正式版本，代入 t、4、2 与 r=t−1，比较所有额外条件，而不只比较文章标题。
3. 对 KN26 的 quartic 普通交数及其引用链，核对是否已经给出相同精确阶或生成子群细分。

输出应区分“经典工具”“直接推论”“需要本文新的几何验证”“优先权仍不确定”。
即使某一引理已有出处，也应按查到的来源调整贡献措辞，而不是靠更多数值例子支撑新颖性。

## 9. 本轮发现、原文位置与处理

下列均为本轮实际处理记录；它们不假装原稿已有错误的平均公式。

| 级别 | 原位置 / 原文 | 问题与处理 |
|---|---|---|
| 重要，已处理 | 修改前 PaperA_revised.tex:1633，"is an isomorphism of finite groups because ..." | 角色唯一分解仅作为正文衔接；现第 1651 行加具名引理并写出 S_b 与 E_norm |
| 重要，已处理 | 修改前 :1882，"Uniform b ... Consequently ..." | 原平均本来正确；现第 1865 行给出独立引理，完整证明全部 b 的两个精确平均 |
| 重要，已处理 | 修改前 :1932，"an explicit sufficient condition is ..." | 需要便于追踪的存在范围；现第 2009 行定义 S_an，并在第 2047 行写出证书与解析范围的并集 |
| 建议，已处理 | 修改前 :16，"A complete mapping ..." | 密度结果在摘要中靠后；现摘要从标量实现密度、范数纤维和双满阶渐近开篇 |
| 重要，待完成 | 当前 :75 起相关工作及 Literature_Audit_scalar_realization.md | 定向查询不等于直接推论检验；按 §8 的三项任务完成最近文献的逐假设对照 |
| 建议，待完成 | 最终编辑器 PDF 预览 | 本轮只有内置编译与静态核对；最终逐页版式核查未完成 |

修改前行号指 backups/before_submission_tightening/PaperA_revised.tex；
当前行号指编辑器源文和工作副本同一文本。差异见 PaperA_submission_tightening.diff。

## 10. 投稿就绪结论

**NO-GO：本轮尚不足以确认“可以立即投稿”。**剩余项是 §8 的最近文献
直接推论检验与最终版式核查，不是要求把双满阶全维开放问题作为投稿前必须解决的定理。
在本次明确审查的 5.21–5.24 范围内，未发现新的数学阻断项；仍建议由熟悉
有限域角色和的独立专家检查 Lang 下降及 Artin 字符界的应用。
这不是模拟录用概率，也不是期刊会给 Major Revision 或 Reject 的预测。
