# ChinaXiv submission draft — Paper A (narrative and priority review, 2026-10-12)

Revision: paperA-general-preprint-2026-10-12-proof-audit. Local preparation draft.

## 1. Title

EN: Affine companion groups in characteristic two: scalar realizations and density

ZH: 特征二中的仿射伴随群：标量实现与密度

## 2. Author

Baohua Li (Independent Researcher; People's Republic of China)

## 3. Abstract

EN:

We study scalar realizations of affine companion groups in characteristic two. For q=2^n, d | q-1, and k=(q-1)/d, we give an exact Möbius formula and an explicit error for the number of a satisfying a, 1+a in C_d and <a,1+a>=C_d. At the quartic norm boundary t=2^s, s>=2, and d=(t+1)(t^2+1), the full-family joint-generation count is |R_d|=theta_2(d)(t+1)^2+O(t^(3/2) 2^omega(d)), where theta_2(d)=product over p|d of (1-p^(-2)). Each norm fiber has O(t) points. On every nonexceptional fiber, we give an explicit O(t) main term with a norm-dependent coefficient and a square-root-scale error; exceptional fibers are bounded separately. Exact local averaging over all t+1 fibers yields the quadratic full-family main term. The number D_d of slopes with ord(a)=ord(1+a)=d obeys D_d~(phi(d)/d)^2(t+1)^2, with an explicit error, and is positive for every s>=2. This exact-order pair is a standard (t-1)-primitive-pair object; we do not claim its first formulation. Our contribution is the norm-fiber density analysis, its companion-group interpretation, and the all-dimensional existence proof. We also determine affine generation criteria and prove the optimal uniform index exponent 1/4; further sections treat spread statistics and a nonlinear example generating A_16. Lean checks only the stated triality and field-Singer results; the density and existence arguments use classical curve bounds and exact arithmetic.

ZH:

本文研究特征二中仿射伴随群的标量实现。对 q=2^n、d | q-1 和 k=(q-1)/d，本文给出满足 a、1+a∈C_d 且 <a,1+a>=C_d 的斜率数的精确 Möbius 公式及显式误差。对四次范数边界 t=2^s（s≥2）、d=(t+1)(t²+1)，全参数族的联合生成数为 |R_d|=θ₂(d)(t+1)²+O(t^(3/2)·2^ω(d))，其中 θ₂(d)=∏_{p|d}(1-p⁻²)。每个范数纤维均有 O(t) 个点。对每个非例外纤维，本文给出主项为 O(t)、系数依赖范数参数且带平方根级误差的显式公式；例外纤维另行控制。对全部 t+1 个纤维作精确局部平均，得到二次尺度的全族主项。两项阶均为 d 的斜率数 D_d 渐近于 (φ(d)/d)²(t+1)²，有显式误差，并且每个 s≥2 都为正。该相邻精确阶对是标准的 (t−1)-primitive-pair 对象；本文不声称首次提出其计数。本文的贡献是范数纤维上的密度分析、其与仿射伴随群实现的联系，以及全维存在性证明。本文还给出仿射生成判据并证明统一指数界的最优幂次为 1/4；其他部分讨论展的统计及一个生成 A₁₆ 的非线性例子。Lean 仅核验文中指定的 triality 与域上 Singer 结论；密度和存在性证明使用经典曲线界及精确算术。
## 4. Keywords

EN: affine companion group; scalar realization; prescribed multiplicative order;
norm fiber; character sum; complete mapping; oriented spread

ZH: 仿射伴随群；标量实现；指定乘法阶；范数纤维；角色和；完整映射；定向展

## 5. Classification (draft)

数学 — 数论（有限域） / 代数学（有限群） / 组合数学

## 6. Source and research scope

Theorem 5.24 retains the quadratic double-order count and proves
both exact orders for every s>=2. Proposition 5.25 gives a trace-one
subfamily with conductor four. The complete partition is: s=2..32
by exact field certificates, s=33..113 by exact divisor upper bounds
and the four-point estimate, and s>=114 by a uniform odd-integer bound.
The special subfamily is empty at s=3,5; it is not claimed to work
in every dimension. Its linear count is separate from the quadratic
full-family count. The proof is outside the Lean formalization.

The exact-order pair is a standard (t-1)-primitive pair.
The reciprocal-trace/Frobenius change of variable is attributed to
Cohen (2003), Section 4. The contribution presented here is the
effective count on the specific norm fibers and its companion-group
application. Specific priority is unconfirmed; the latest literature
comparison records the full-text coverage explicitly.

Lean scope: function-level triality, field-Singer generation,
and a conditional tau-collapse interface. No Lean rerun was performed
for this editorial revision. Classical curve bounds and exact certificates
are paper-proof dependencies; they are not claimed as formally verified.

## 7. Preparation records

- PaperA_revised.tex and both abstracts are synchronized with this form.
- PaperA_Submission_Narrative_and_Priority_Audit.md records attribution,
  parameter comparisons and the remaining full-text literature checks.
- Submission_Narrative_Final_Audit.json records this source's compilation.
- PaperA_revised_sha256.json identifies the complete current file set.

The existing editor remains open. No separate PDF export, page-count
confirmation or visual page inspection is claimed for this revision.
No external submission or deposit has been performed.
