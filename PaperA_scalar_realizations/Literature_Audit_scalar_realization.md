# Paper A：标量实现与 Paley 图文献核查

核查日期：2026-10-12。范围：直接阅读原论文或作者提供的全文。
这是一轮定向核查，不是对全部文献的穷尽搜索。

## 已确认应归属的内容

| 文献 | 核查位置 | 与本轮结果的关系 |
|---|---|---|
| [van Wamelen, *Jacobi sums over finite fields*](https://doi.org/10.4064/aa102-1-1), 2002 | Theorems 1–2 | Jacobi 和的特殊值及平方根模长是经典输入；正文给出所需推导，不声称方法创新 |
| [Lim–Praeger, *On generalized Paley graphs and their automorphism groups*](https://arxiv.org/abs/math/0605252), Michigan Math. J. 58 (2009), 293–308 | Theorem 2.2、Theorem 1.2 | 乘法连接子群的不可约性、图连通性及真子域连通分量已有系统研究；图全自同构群可能大于指定半线性群 |
| [Dawsey–McCarthy, *Generalized Paley graphs and their complete subgraphs of orders three and four*](https://arxiv.org/abs/2006.14716), Res. Math. Sci. 8 (2021), Article 18 | §2.2、Theorem 2.9 | 广义 Paley 图的普通三角形数已有 Jacobi 和公式，包括偶特征；不能把 T_d 或其字符表达式当新结果 |
| [Podestá–Videla, arXiv:1812.03332v7](https://arxiv.org/abs/1812.03332v7), 2024 版本 | Definition 2.1、Theorem 5.2 | 本轮 q=t⁴、k=t+1 的图正是其 Γ_{t,4}(1)；普通相邻交数 t−2 已包含在该参数公式中，图族本身也已有研究 |
| [Cohen, *Consecutive non-square non-primitive pairs in a finite field*](https://arxiv.org/abs/2604.21429), 2026 | 摘要、对象范围 | 讨论奇素数幂有限域中的连续非平方、非本原元素；不能直接作为本轮特征二、指定 C_d、联合生成条件的定理依据 |

## 本轮论文的准确定位

1. 对已有交数 T_d 加入〈a,1+a〉=C_d 的条件，通过 Möbius 反演得到 |R_d|。
   主项与误差是经典字符方法的推论，正文只作明确的对象专门化。
2. 给出一般相对范数下降：d=u(2^r+1)、u∣2^s−1、s 真除 r 时，
   两项均在 C_d 的元素必降入 F_{2^{2s}}，并确定交子群的精确阶。
3. 在 t⁴ 族中，这一位置定理使所有候选对落入 F_t；
   由此推出本原仿射伴随群的非实现性及统一增长指数的 1/4 障碍。
4. 生成三角形使用归一化比率生成子群。正文的 |R_d|/6 轨道数只涉及
   H_d 的作用；本原实现映射的 |R_d|/n 则涉及线性共轭。

本轮已确认图族、普通交数、连通性及 Jacobi 方法有明确前人来源，
并在论文中添加相应引用。一般范数下降、伴随非实现应用、1/4 统一障碍
和上述分类组合的文献优先权尚未确认；不以“未找到同式”证明首创。

## 投稿前需要继续追查

- 半本原 cyclotomy、椭圆二次曲面及仿射极图中是否已有同样的候选子域位置定理。
- 指定乘法子群中的 a、1+a 联合生成，是否已有与本轮 Möbius 计数等价的表述。
- 不同于“所有 complete mappings 共同生成的群”的“一个映射及其指定伴随生成的群”，是否已有等价逆向分类。

即使某个引理已有出处，伴随实现的统一范围及障碍仍可以作为应用表述；
应在出处明确后相应降低独立原创贡献的措辞。

## 临界内侧 k=t−1 的全维实现：追加核查

日期：2026-10-12。新结论见 Theorems 5.19–5.20。

| 阅读来源 | 直接使用或比较的位置 | 准确范围 |
|---|---|---|
| [Katz, 1989 作者全文](https://web.math.princeton.edu/~nmk/old/estcharsums.pdf) | pp.198–199 Lang 覆盖、角色层、几何非平凡性与温和 Euler 特征 | 使用经典方法；其直线主定理不直接代替本轮 genus 1 导子计算 |
| [Farashahi 等, 2013 作者全文](https://www.normalesup.org/~tibouchi/papers/welldistributed.pdf)；[DOI](https://doi.org/10.1090/S0025-5718-2012-02606-8) | 作者稿 §4、Lemma 1 的曲线 Artin 角色和界 | 经典亏格/导子平方根界；本轮单独验证几何非平凡与八点温和分歧 |
| [Kudo–Nogata, 2026](https://arxiv.org/abs/2604.25461) | 全文 Proposition 4.3、范数交数对象 | 包含 r=4、指数 t−1 的普通交数；不把 T_d 及其范数解释列为新贡献 |
| [Hachenberger, 2021](https://doi.org/10.1007/s10801-019-00920-8) | 四次扩张、卵形与本原正规基对象比较 | 全乘法群本原或射影对象不能自动替代本轮指定范数核精确阶条件 |

本轮在每个本原相对范数纤维上证明导子恰为 8，并通过本原角色筛
得到计数和全维存在性。文中将此作为指定仿射伴随实现问题的结果，
没有声称 Weil 方法、Lang 构造或本原示性函数是新方法。
当前查询不构成穷尽式优先权审查。


## 指定阶、曲线本原点与范数约束：审查合并核查

| 文献与来源 | 实际阅读范围 | 应采用的比较 |
|---|---|---|
| [Cohen–Kapetanakis 2021，出版商全文](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/E05DAD9652876E917A902EDA282FFA6F/S1446788720000099a.pdf/finite-field-extensions-with-the-line-or-translate-property-for-dollarrdollar-primitive-elements.pdf) | Theorem 1.3、证明式 (4-3)、Remark 4.1 | 主定理固定 r,n；Remark 4.1 已明确讨论适当增长的 r。只以 r=t−1 增长不能断言文献不覆盖，更不能证明新颖性；须比较定量假设与同时范数条件 |
| [Cohen–Kapetanakis–Reis 2022，出版商全文](https://comptes-rendus.academie-sciences.fr/mathematique/item/10.5802/crmath.328.pdf) | Proposition 13、Theorem 16、Corollary 17、Remark 18 | 本原/指定阶示性函数和曲线点筛已有来源。附件使用的 Theorem 4.2 属不同编号；本地报告按正式期刊版校正。一般充分界的参数需逐项代入，不能因方法名称不同就推断排他性 |
| [Sharma–Sarma–Laishram 2024，出版商页面](https://link.springer.com/article/10.1007/s00574-024-00412-9) | 元数据和摘要 | 已有 r-primitive 算术级数研究；本轮仅核实范围概述，未把摘要当作排除全部正文结果的证明 |
| [Chatterjee 等 2025，作者预印本](https://arxiv.org/pdf/2401.01819) | 摘要及引言、指定范数对象 | 已有 primitive 算术级数与规定范数研究；全文的 primitive 指全乘法群本原，仍需比较指定子群精确阶 |
| [Choudhary–Sharma，作者上传全文](https://www.researchgate.net/publication/396016739_Arithmetic_progressions_of_some_special_elements_in_finite_fields)；[DOI](https://doi.org/10.1080/00927872.2025.2561951) | Definitions 3.1、Theorem 1 及范数/freeness 归约 | Theorem 1 的充分条件 q^{n/2−m}>m∏r_iW(Q_{R_i}) 在 q=t,n=4,m=2 时左边为 1、右边至少为 2，不能由这一条件得本稿正性。这一比较不排除其他筛的改进或等价结果 |

这五条均已加入当前正文参考文献。引言说明经典方法的归属，具体贡献定位于指定范数纤维和伴随实现应用，不声称首次性。
四阶有理平移的代数证明已合入 Proposition 5.18，但该具体结构的文献优先权仍未确认。

## 投稿前核心压力审查：追加原文核对

日期：2026-10-12。核心编号 5.21–5.24 保持；详见 PaperA_Submission_Stress_Audit.md。

- Farashahi 等作者稿 §4 Lemma 1 的界以亏格和 Artin 导子表示。
  本稿八点表、几何单值群与温和性逐项验证其所需几何非平凡条件；
  不能只凭有限群字符非平凡就跳过该条件。
- CKR22 正式版 Proposition 13、Theorem 16、Corollary 17、Remark 18 再核对：
  freeness 指标及角色幂关系检验都是已有工具。新辅助平均引理是初等循环群概率，
  不作为方法创新；具体 norm-fiber 密度是否已有等价结论仍需逐假设对照。
- Chatterjee 等的作者预印本 v3 此轮阅读到定义、Lemma 3.5 及 Theorem 4.1：
  该定理要求 n>2m，四次扩张和两项条件 n=4,m=2 不满足；
  primitive 指全乘法群本原，与本稿范数核中的精确阶 d 有区别。
  这里采用的是作者预印本编号，正式版编号及其他定理尚须逐项核对。
  来源：[作者全文](https://arxiv.org/pdf/2401.01819)。
- Picard 主除子独立性的反馈建议不成立。主除子类为零，本文检验的是
  函数域乘法群模幂的独立性；不增加一条错误的 Picard 引理。

下一步范围限定为最接近三组文献的直接推论检验，比较对象、全部假设与定量误差，
而不是宣称已经穷尽所有文献或因为参数表面不同就证明原创性。

## 双满阶全维闭合：新增内容及优先权边界

Proposition 5.25 以 γ∈C_B、γ+γ⁻¹∈C_A、a=(1+γ)⁻¹ 使 1+a=a^(t²)。
实际 Lang 拉回 z_U^A=w₀⁻¹、z_V^B=y^t/x，全几何单值群和四点导子
均有正文证明；两角色筛与完整整数覆盖关闭全 s≥2 双满阶存在。
Weil、Lang、本原角色指标及小因子上界为经典工具，不声称这些机制首次出现。
本轮未完成互反迹条件的最新文献等价核查，具体应用的优先权仍未确认。
下一步须比较 primitive reciprocal traces、规定范数的本原点和 primitive pairs，
逐一核对字段、阶、范数、特征和小参数范围。


## 最新校正：叙事与直接推论检验（2026-10-12）

以前关于“互反迹尚未核查”的记录现由
PaperA_Submission_Narrative_and_Priority_Audit.md §2 更新：
Cohen 2003 §4 已有迹一/互反迹 Möbius 归约，不能将其机制列为原创。
关于 quartic norm kernel 与 projective primitive points 的旧表述也需收紧：
相应乘法分量确有重合，不能仅用“对象名称不同”排除 Hachenberger。
本轮读取其正式出版商预览与作者2016报告，未取得正式全文；
仅能证明本稿迹一子族总迹为零，正规基存在结论本身不提供这些点。
具体定理的首次性仍未确认。

新审计报告给出 CKR22 正式版 Theorems 16、20、Corollary 17 的完整参数代入，
包括任意素数筛分拆的失败证明；另核对 AN22 v1 Theorem 3.2 的宽松指标版本。
Sharma–Sarma–Laishram 2024 本轮仍限于机构元数据、摘要及作者出版目录；
没有取得正式全文，不排除其其他结果。所有判断均按阅读深度标注。
