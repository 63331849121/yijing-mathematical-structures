\paragraph{Additional double-order certificates.}
The file \path{inner_double_order_certificates.json} uses the same
$M_s,b$ as the preceding table and replaces $w$ by $b^{e_s}$, with
the following exponents. The root $a=Z$ of
$Z^2+(1+b+b^{e_s})Z+b$ and its translate $1+a$ both have exact
order $d$, for every $2\le s\le32$.
\begin{center}\small
\begin{tabular}{rr|rr}
$s$&$e_s$&$s$&$e_s$\\\hline
2&1&18&1\\
3&4&19&5\\
4&1&20&1\\
5&4&21&5\\
6&3&22&1\\
7&1&23&8\\
8&4&24&4\\
9&26&25&1\\
10&1&26&3\\
11&7&27&1\\
12&1&28&1\\
13&1&29&1\\
14&8&30&1\\
15&4&31&1\\
16&4&32&3\\
17&7&&\\
\end{tabular}
\end{center}
The independent \path{verify_inner_mixed.py} checks irreducibility,
the trace, both norms and both nonidentity residues
$a^{d/p},(1+a)^{d/p}$ for every prime $p\mid d$. It uses the
complete factorizations and recursive Lucas certificates of
\path{inner_critical_certificates.json}; all new residues and all
norm-fiber counts for $s=2,\ldots,6$ are recorded in
\path{inner_mixed_verification.json}. It also checks the corrected
mixed Lang functions and trace multipliers at the 31 certificate points.
These computations establish precisely the stated finite range.
Together with Proposition~\ref{prop:inner-diagonal-double} for $s\ge33$,
they complete the all-dimensional double full-order theorem.
The new verifier \path{verify_inner_double_all.py} independently
rechecks all 31 double-order certificates, including their recursive
Lucas primality proofs, without calling a certificate finder.

\subsection*{Integer bounds for double full-order existence}
The bound in Proposition~\ref{prop:inner-diagonal-double} is positive
when $\sqrt t\ge4W(d)$. We cover $33\le s\le113$ by exact divisor
upper bounds, and $s\ge114$ by a uniform inequality for odd integers.
No large residual factor is assumed to be prime.

For the uniform bound let $P$ be the product of all 53 odd primes
less than $256$, namely
\[
\begin{gathered}
3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,\\
89,97,101,103,107,109,113,127,131,137,139,149,151,157,163,167,173,\\
179,181,191,193,197,199,211,223,227,229,233,239,241,251.
\end{gathered}
\]
The exact integer comparison $256^{53}<4096^8P$ gives, for every
odd $n$,
\[
 \frac{W(n)^8}{n}
 =\prod_{p^e\parallel n}\frac{256}{p^e}
 \le\prod_{3\le p<256}\frac{256}{p}
 =\frac{256^{53}}{P}<4096^8.
\]
Here the product on the right is over primes: each factor for a
prime at least $256$ is at most one, and adding missing smaller
prime factors only increases the bound. Thus $W(n)<4096n^{1/8}$.
For $s\ge114$, $d<2t^3$ and $t>2^{113}$ prove the sufficient
condition, as computed in Proposition~\ref{prop:inner-diagonal-double}.

For each $33\le s\le113$, divide $A$ and $B$ by every prime at
most $4096$, with its full multiplicity. Let $j_A,j_B$ be the
numbers of distinct small factors and $R_A,R_B$ the residuals.
All prime factors of each residual exceed $4096$. If
$4097^{k_A}\le R_A<4097^{k_A+1}$ and similarly for $B$, then
\[
 \omega(d)=\omega(A)+\omega(B)
    \le r_s:=j_A+k_A+j_B+k_B.
\]
The following table lists all 81 bounds; each satisfies
$s\ge4+2r_s$, so $\sqrt t\ge4\,2^{r_s}\ge4W(d)$.
\begin{center}\small
\begin{tabular}{rr|rr|rr}
$s$&$r_s$&$s$&$r_s$&$s$&$r_s$\\\hline
33&11&60&15&87&24\\
34&9&61&16&88&21\\
35&13&62&15&89&23\\
36&11&63&21&90&27\\
37&11&64&15&91&26\\
38&11&65&20&92&23\\
39&13&66&19&93&25\\
40&9&67&18&94&24\\
41&11&68&16&95&26\\
42&14&69&19&96&24\\
43&12&70&20&97&26\\
44&11&71&18&98&26\\
45&17&72&19&99&29\\
46&13&73&20&100&26\\
47&13&74&19&101&26\\
48&12&75&23&102&27\\
49&15&76&19&103&26\\
50&14&77&23&104&25\\
51&15&78&22&105&32\\
52&12&79&21&106&27\\
53&14&80&19&107&28\\
54&16&81&23&108&29\\
55&16&82&21&109&27\\
56&13&83&22&110&29\\
57&16&84&23&111&30\\
58&15&85&24&112&27\\
59&15&86&22&113&29\\
\end{tabular}
\end{center}
The full small factorizations, residual integers and their integer
power bounds are supplied in
\path{inner_double_omega_certificates.json}. The independent verifier
\path{verify_inner_double_all.py} reconstructs every small prime by
deterministic trial division, checks the exact products and all 81
inequalities, and checks $256^{53}<4096^8P$.
Its results, log and runtime information are
\path{inner_double_all_verification.json},
\path{inner_double_all_run.log} and
\path{double_all_verification_environment.json}.
It also exhaustively checks the trace-one subfamily for $2\le s\le6$:
its counts are respectively $8,0,16,0,24$. In particular the
all-dimensional claim is for $D_d$, not for $\Delta_t$.
The disjoint ranges $2\le s\le32$, $33\le s\le113$, and
$s\ge114$ cover every integer $s\ge2$.
