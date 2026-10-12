# Paper A：投稿叙事与近邻文献压力审查

日期：2026-10-12。
版本：paperA-revised-2026-10-12-submission-narrative-priority。
当前源：C:/Users/master/Documents/Codex/2026-10-11/paper-review-recovery/outputs/PaperA_revised.tex。

本轮由同一研究会话完成数学复核和文献比较；不称为三位独立专家审稿。
附件评分与“原创思想”评价仅作为待核意见，未作为证明或首次性证据。

## 1. 已完成的正文修改

题名改为 **Affine companion groups in characteristic two: scalar realizations and density**。
中文题名：**特征二中的仿射伴随群：标量实现与密度**。
摘要和引言依次突出：伴随群结构、临界族实现密度、全维双满阶存在。
原有 triality、定向展、Singer 应用及非线性例子继续作为正文的其他结果。
主要位置：题名 11；引言 50；文献比较 107；
Theorem 5.24 2015；Proposition 5.25 2069。

以下量与前轮完全一致：

$$t=2^s,\quad s\ge2,\quad A=t+1,\quad B=t^2+1,\quad d=AB.$$

- 全参数族 $|\mathcal R_d|$、$D_d$ 的二次主项与显式误差不改；
  固定范数纤维仍为 $O(t)$，不混写为 $O(t^2)$。
- Theorem 5.24 的全部 $s\ge2$ 双满阶存在保持；
  Proposition 5.25 的线性迹一子族量 $\Delta_t$ 保持。
- 覆盖分为 $s=2..32$、$33..113$、$s\ge114$，三个区间没有缺口。
- 5.21–5.26 编号保持；数学依赖仍为经典曲线界及精确有限算术。
- 本轮不增加有限域计算，不重跑 Lean；保留前轮结果的输入哈希与运行记录。

## 2. 最接近文献的逐参数比较

### 2.1 双满阶与 $r$-primitive pair 完全同一对象

令 $L=\mathbb F_{t^4}$、$K=\mathbb F_t$。

$$
N_{L/K}(a)=a^{1+t+t^2+t^3}=a^d,\qquad
d=\frac{t^4-1}{t-1}.
$$

$L^\times$ 为循环群，其唯一的阶 $d$ 子群恰为范数核。
因此

$$
\operatorname{ord}(a)=\operatorname{ord}(1+a)=d
\iff
(a,1+a)\text{ 是 }(t-1)\text{-primitive pair}.
$$

这里两项范数一已由精确阶自动推出，不能宣传为对既有
$r$-primitive pair 的另一项独立附加条件。
范数纤维细分与下降后更强的有效误差才是需要比较的内容。
此归约是循环群阶与范数的初等恒等式。
台账：P-scalar-inner-prescribed-order-comparison，已证；
源引言及本节为证明位置。

### 2.2 CKR22：基本充分界

核对正式发表版 Cohen–Kapetanakis–Reis，
[The existence of Fq-primitive points on curves using freeness](https://comptes-rendus.academie-sciences.fr/mathematique/item/10.5802/crmath.328.pdf)，
C. R. Math. 360 (2022), 641–652，DOI 10.5802/crmath.328。
实际位置：Definition 8、Remark 9(ii)、Theorem 16、Corollary 17，
pp.644、646–647；素数筛为 Theorem 20，pp.648–649。

使用下面的精确字典，不能把其 $r$ 与本稿指数直接混用：

| CKR22 参数 | 本稿取值 |
|---|---|
| ambient field size $q$ | $Q=t^4$ |
| $f,F$ | $X,X+1$ |
| subgroup indices $n,N$ | $t-1,t-1$ |
| freeness parameters $r,R$ | $d,d$ |
| number of distinct roots $D+1$ | $2$，所以 $D=1$ |

两多项式非恒定、平方自由且比值非恒定，几何假设满足。
$(d,t-1)$-free 恰为阶 $d$，故 Theorem 16 确实在数同一个 $D_d$。
其估计代入后为

$$
\left|D_d-\theta(d)^2\frac{t^4}{(t-1)^2}\right|
\le\theta(d)^2t^2W(d)^2.
$$

Corollary 17 的正性要求

$$t^2>(t-1)^2W(d)^2.$$

$A,B$ 是互素的奇整数且均大于1，故 $\omega(d)\ge2$、$W(d)\ge4$。
对 $t\ge4$，$16(t-1)^2>t^2$，所以该条件在本族所有参数均失败。
主项和本稿的 $\theta(d)^2(t+1)^2$ 仅相差

$$\theta(d)^2\frac{2t^2-1}{(t-1)^2}=O(1).$$

真正差别在于误差的数量级：基本环境域界为 $t^{2+o(1)}$，
本稿下降后的双满阶误差为 $t^{3/2+o(1)}$。
这项比较不能被改写成“旧文献研究了不同对象”。

### 2.3 CKR22：任意素数筛分拆也不能给出正值

按其 Theorem 20，把 $\operatorname{rad}(d)$ 在两项中各分成
core $k_r,k_R$ 和待筛素数。设待筛数目共 $m=u+v$，
并令

$$
\delta=1-\sum_{i=1}^u p_i^{-1}-\sum_{j=1}^v \ell_j^{-1}>0,\qquad
\Lambda=W(k_r)W(k_R)\left(\frac{m-1}{\delta}+2\right).
$$

该下界的括号能为正必须满足

$$\frac{t^2}{(t-1)^2}>\Lambda.$$

对任意合法分拆：

- 若 $m=0$，两项 core 都含 $\operatorname{rad}(d)$，
  $\delta=1$，所以 $\Lambda=W(d)^2\ge16$。
- 若 $m=1$，只从两份 core 的总计至少四个素数位中删去一个，
  所以 $W(k_r)W(k_R)\ge8$，而括号为2，仍有 $\Lambda\ge16$。
- 若 $m\ge2$，由 $0<\delta\le1$，括号至少为 $m+1\ge3$；
  因 $W(k_r)W(k_R)\ge1$，所以 $\Lambda\ge3$。

而 $t\ge4$ 给出

$$\frac{t^2}{(t-1)^2}\le\frac{16}{9}<3.$$

因此 Theorem 20 的任何合法 core/prime 分拆均无法在本参数下
通过其显示的充分下界给出正值。$\delta\le0$ 的分拆本来不满足定理假设。
这是全部分拆的代数证明，无须按 $s$ 搜索，也不涉及把未知余数当素数。
它不排除更强的局部角色和、其他论文或对同一方法另作改进。

### 2.4 AN22：宽松指标版本的比较

读取 Aguirre–Neumann，
[Pairs of r-primitive and k-normal elements in finite fields](https://arxiv.org/pdf/2210.11504)，
arXiv:2210.11504v1 (2022)，Definition 3.1 和 Theorem 3.2，
打印页7–8；引用预印本版本，不虚构期刊信息。

在其一般计数中取

$$
q=t,\ n=4,\ F(X)=X+1,\ (m_1,m_2)=(1,0),\
r_1=r_2=t-1,\ R_1=R_2=d,\
f_1=f_2=1,\ g_1=g_2=1.
$$

$f_i=1$ 为线性化恒等算子，$\beta_i$ 唯一由 $\alpha,F(\alpha)$ 确定；
$g_i=1$ 使加性 freeness 指标恒为1，故该一般计数没有正规性限制。
Theorem 3.2 的 $M=2$，正性充分条件变为

$$t^2\ge2(t-1)^2W(d)^2,$$

同样全部失败。这里用一般计数的自由指标版本；
不能把 $k_i=0$ 本身解释成“没有 normality”，因为其 normal 特例中
$k=0$ 的含义恰为正规。此处只比较已代入的 Theorem 3.2，
不宣称穷尽该文全部筛或其他结果。

### 2.5 Cohen 2003：Frobenius 耦合机制已有经典前例

核对 Cohen，
[The orders of related elements of a finite field](https://doi.org/10.1023/A:1026295128600)，
Ramanujan J. 7 (2003), 169–183，Theorem 1.5 p.170、
Theorem 1.6 p.171、§4 pp.175–176。
本地正式 PDF：D:/project/codex/Yishu01/_lit/cohen2003_orders_related.pdf。
SHA-256：96060ce6b809bfa298d8ae213d130f228a287799169ee87799d6e814e984b11c。
当前工作区核心证明 B2a–B2c 本来已记录这条归约。

经典偶特征迹一关系通过分式线性替换，把范数一
$\gamma$ 的互反迹与 $a$ 的范数相联，并有 $a^q=1+a$。
因此反馈所称“发现 Frobenius 绑定是原创思想”需要撤回到具体纤维的层面；
不是新增一般构造技巧。

但以 $q=t^2$ 代入 Theorem 1.5，只得到

$$
\operatorname{ord}(\gamma)=B=t^2+1,\qquad
\operatorname{ord}(\tau)=t^2-1=(t-1)A.
$$

本稿要求 $\operatorname{ord}(\tau)=A=t+1$。
前者的 $N_{E/K}(\tau)=\tau^{t+1}$ 具有阶 $t-1>1$；
后者要求该范数等于1。因而 Theorem 1.5 的这些点不落在目标互反迹纤维。
不能直接由这一具体定理代入关闭本稿条件，也不能仅凭这一差别
宣布所有相关文献均未覆盖本稿。

正文引言和 Proposition 5.25 后现明确引用经典变换；
贡献表述集中在该指定纤维的几何、四点导子、有效计数和完整参数覆盖。

### 2.6 其余最接近来源及阅读边界

| 来源 | 本轮或前轮实际阅读位置 | 可以得出的结论 |
|---|---|---|
| [Cohen–Kapetanakis 2021 出版商全文](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/E05DAD9652876E917A902EDA282FFA6F/S1446788720000099a.pdf/finite-field-extensions-with-the-line-or-translate-property-for-dollarrdollar-primitive-elements.pdf) | 前轮 Theorem 1.3、式(4-3)、Remark 4.1 | 已有指定阶 line/translate，且提及增长 $r$；仅凭 $r=t-1$ 变化不能证明首次性 |
| [Gupta–Sharma–Cohen 2018 作者机构全文](https://web.iitd.ac.in/~rksharma/Research%20Publications/Journal/Primitive%20element%20pairs%20with%20one%20prescribed%20trace%20over%20a%20finite%20field%20FFA%20paper%202.pdf) | 本轮 Theorem 1.1、Corollary 1.2，pp.2–3 | 结论针对扩张次数 $n\ge5$、全乘法群本原的互反迹对；不是 $n=4$ 的两指定子群阶，不能由该结论直接代入 |
| [Hachenberger 2021 出版商预览](https://link.springer.com/article/10.1007/s10801-019-00920-8)；[作者2016报告](https://imsarchives.nus.edu.sg/oldwww/Programs/016combin/files/Hachenberger.pdf) | 正式全文未取得；预览及报告逻辑页13–14、19（PDF页42–51、73） | quartic norm factors 与本稿确有重合；其 normal-basis 结论本身不供给下面的 trace-zero 点；不排除正式全文其他定理 |
| [Sharma–Sarma–Laishram 2024 机构条目](https://digitalcommons.isical.ac.in/journal-articles/4612/)；[作者出版目录](https://web.iitd.ac.in/~ritumoni/publications.html) | 本轮元数据、摘要；DOI 10.1007/s00574-024-00412-9 的正式全文未取得 | 已研究 $r$-primitive 算术级数；不能据摘要排除其全部定量或小参数结果，须作为剩余重点 |
| [Chatterjee 等作者预印本](https://arxiv.org/pdf/2401.01819) | 前轮 v3 定义、Lemma 3.5、Theorem 4.1 | 要求 $n>2m$，$n=4,m=2$ 不满足；只排除这个直接代入，不排除正式版其他结果 |
| [Choudhary–Sharma 作者上传](https://www.researchgate.net/publication/396016739_Arithmetic_progressions_of_some_special_elements_in_finite_fields) | 前轮 Definitions 3.1、Theorem 1 | 引言已有逐参数不等式失败比较；不能外推为全部论文方法失效 |

本稿迹一子族满足

$$
\operatorname{Tr}_{L/K}(a)
  =(a+a^{t^2})+(a^t+a^{t^3})=1+1=0.
$$

所以其四个 Frobenius 共轭线性相关，点不正规。
这项初等检查说明“有 primitive normal basis”不自动产生这里的迹一点。
但 norm-one projective representative 与本稿的阶 $d$ 点有同一乘法因子结构，
不能用“射影对象不同”一句话判定不重合。
Hachenberger 正式全文仍须读到相应 ovoid 与 trace-kernel 交数。

**阅读边界**：本文未确认首次性；未宣称完整排除所有外部定理。
两份未取得的正式全文是明确的剩余文献核查对象。
记录一个充分条件失败，只是直接推论检验的结果。

## 3. Proposition 5.25 的几何压力核查

台账 P-scalar-inner-diagonal-double，已证（依赖外部定理）；
纸面证明在源 Proposition 5.25 与 PaperA_Double_Full_Order_Closure.md §§2–4。

### 3.1 光滑模型和正确下降

几何模型为

$$Y_{\overline K}:(x+1)^2(y+1)^2=xy\subset\mathbb P^1\times\mathbb P^1.$$

它不是直接使用系数所在 $\mathbb F_2$ 的普通 split curve：
本稿 $K$-结构来自 torus，Frobenius 为 $(x,y)\mapsto(y^{-t},x^t)$。
关系 $y=x^t$ 只在 $K$-点成立，不可拿到几何函数域中消元。
源第 2129 行起已补明。

仿射偏导分别为 $y,x$，共同零点 $(0,0)$ 不在曲线上。
边界仅有 $P_0=(0,1),P_\infty=(\infty,1),Q_0=(1,0),Q_\infty=(1,\infty)$。
$P_0$ 处用 $u=y+1$，方程为 $(1+x)^2u^2+x(1+u)=0$，
对 $x$ 的偏导在点处为1；其余点由倒数和交换坐标给出同一检查。
因此几何模型处处光滑。

### 3.2 不可约性不能只由双次数推出

源第 2146 行起已展开证明。光滑蕴含约化，
而不同不可约分量若相交就使该点局部环不是正则一维整环。
假设有多个互不相交分量，其有效双次数 $(a_i,b_i)$ 非零且非负，
总和为 $(2,2)$。若有混合双次数分量，则它以正交数
$a_ib_j+a_jb_i$ 遇到每个其他分量；若全为纯类，
总双次数要求同时有 vertical 和 horizontal 分量，两者也正相交。
两种情况均矛盾，故几何不可约。此后才能用 adjunction 得 genus 1。

Frobenius 把边界四点组成一个4-cycle，所以没有 $K$-有理边界点。
Hasse–Weil 因而直接给开曲线总体 $t+1+O(2\sqrt t)$。
若错误使用普通坐标逐项 Frobenius，这个边界判断会错。

### 3.3 实际 Lang 函数、幂关系与四点导子

$w_0=(x+1)^2/x$、$h=y^t/x$。
实际拉回为 $z_U^A=w_0^{-1}$、$z_V^B=h$，而非任取同 divisor 的方便模型。
Lang 坐标 Frobenius 的乘子在 $K$-点为 $\tau,\gamma$，
故角色迹确是 $\eta(\tau)\chi(\gamma)$（或统一逆角色约定）。

| 点 | $v(w_0)$ | $v(h)$ |
|---|---:|---:|
| $P_0$ | −2 | −2 |
| $P_\infty$ | −2 | 2 |
| $Q_0$ | 2 | $2t$ |
| $Q_\infty$ | 2 | $-2t$ |

若 $(w_0^{-1})^{Be_0}h^{Ae_1}$ 为 $AB$ 次幂，
$P_0$ 赋值给出 $AB\mid2Be_0-2Ae_1$。
分别模 $A,B$，因它们奇且互素，得 $A\mid e_0,B\mid e_1$。
源第 2223 行起已解释：单个赋值可用，是因为两次模约化分别
杀掉另一分量，而不是未经证明的“一般二函数 Kummer 独立性”。
这证明整个 product cover 的全几何单值群。

四处每个赋值均是相应奇阶的单位。
非平凡角色分量在每处都分歧；两个分量阶互素，惯性角色不能相消。
故每个非平凡角色对的总 Artin 导子恰为4，Swan 为0。
纯权0、几何非平凡的 rank-one 层有 $H_c^0=H_c^2=0$；
GOS 给 $\dim H_c^1=2g-2+4=4$，经典曲线界才给 $4\sqrt t$。
不能把有限群角色非平凡直接当作几何非平凡。

### 3.4 筛误差与三个区间

两 primitive 指标的常数项 $\theta(A)\theta(B)=\theta(d)$，
全部绝对系数和为 $\theta(d)W(d)$。
Hasse 项给 $2\theta(d)\sqrt t$，其余系数用 $4\sqrt t$，
所以总误差恰为 $\theta(d)(4W(d)-2)\sqrt t$。
充分条件 $\sqrt t\ge4W(d)$ 不等同于对所有小 $s$ 都成立。

| 参数 | 实际依据 | 证据边界 |
|---|---|---|
| $2\le s\le32$ | 前轮31个精确有限域证书 | 范数、完整素因子及阶逐项认证；不是无限外推 |
| $33\le s\le113$ | 前轮81个完整整数上界 + 本命题 | 大余数未假设为素数；只需其最小可能素因子和幂界 |
| $s\ge114$ | 统一 $W(n)<4096n^{1/8}$ | 解析无限尾部；无遗漏维度 |

三个区间的结果共同给 $D_d>0$ 对每个 $s\ge2$。
$\Delta_t=0$ 在 $s=3,5$，因此它只被保证在 $s\ge33$ 非空。
保留31个初始证书是有效证明的一部分，不能为弱化“计算感”而省略。
源和报告已坚持这一边界。

## 4. 已纠正与尚待核查的事项

| 级别 | 反馈或原表达 | 处理 |
|---|---|---|
| 重要 | 将 Frobenius 绑定当作首次一般技巧 | 源引言及 2272 行起归属 Cohen §4 |
| 重要 | 双满阶之外另附 norm-one 条件而据此区分旧 primitive pair | §2.1 证明 norm-one 自动成立；源明确对象等价 |
| 重要 | 用一般 sieve 基本界失败作为全部方法都失败的证据 | 对 CKR22 素数筛完成任意分拆的证明；其他文献限定到实际读过的陈述 |
| 重要 | 几何方程系数在 F2，容易误用普通 Frobenius | 明确扭曲 K-下降与 K-点条件；四点循环来自 torus Frobenius |
| 微小 | “不同光滑分量不能不交”缺少具体双次数推导 | 现写出有效类的两种情况及交数 |
| 待核 | Hachenberger 2021 与 SSL24 全文可能含更直接结论 | 未取得正式全文，不能以预览/摘要判定排除；保留首次性未确认 |

## 5. 结论与下一步

**GO**：本轮正文修订、具体参数比较与 Proposition 5.25 的表达收紧；
全维数学结论的既有证明状态保持，未发现本次复核推翻其内部步骤的理由。

**NO-GO**：把此轮描述为“已完成穷尽优先权审查”或“Frobenius 耦合首次发现”。
前者缺两份重点全文及对其其他定理的比较，后者有明确经典前例。
这不是要求再扩张研究方向或更多有限算例。

下一步首先取得并对齐 Hachenberger 2021 的 ovoid/trace-kernel 陈述与
Sharma–Sarma–Laishram 2024 的增长指数/二项进展定量界。
正文现已使用不依赖首次性确认的准确贡献表述，可据此继续专家审查和投稿准备。
编译状态、跨文件一致性和本轮未重跑的计算范围见
Submission_Narrative_Final_Audit.json；本文不宣称任何期刊作出接收判断。


## 6. 当前源编译与同步记录

本轮源已经通过桌面编辑器内置编译器编译；未创建新编辑页或导出独立PDF。
静态核查：100标签、202引用、33文献；所有文献都有正文引用。
题名、两个摘要、两份本地表单与六个插入片段一致。
Theorems 5.19–5.24 的陈述/证明及 Proposition 5.25 的陈述相对前轮逐字保持。
新源、报告、差异及配套资料共82项进入 SHA-256 清单；
47项已有计算代码、数据、日志和历史核验记录相对前轮哈希保持。
旧计算结果本轮没有重新运行；JSON 审计明确记录了这一点。
工具只报告编译成功，未提供完整告警日志；不据此声称“零排版告警”。
