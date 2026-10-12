\subsection*{Finite certificates for the inner critical theorem}
\label{app:inner-cert}
Theorem~\ref{thm:inner-all} uses the analytic argument for $s\ge33$
and the following complete finite certificate for $2\le s\le32$.
A hexadecimal integer encodes a binary polynomial with its least
significant bit the constant coefficient. Each row means
\[
 E=\mathbb F_2[X]/(M_s),\qquad
 L=E[Z]/(Z^2+(1+b+w)Z+b),\qquad a=Z.
\]
Thus only $M_s,b,w$ need be specified; all field operations are exact.
\begin{center}\small
\begin{tabular}{r|lll}
$s$ & $M_s$ (hex) & $b$ (hex) & $w$ (hex)\\\hline
2 & \texttt{13} & \texttt{8} & \texttt{1}\\
3 & \texttt{43} & \texttt{6} & \texttt{3b}\\
4 & \texttt{11b} & \texttt{2f} & \texttt{1}\\
5 & \texttt{409} & \texttt{9b} & \texttt{2c9}\\
6 & \texttt{1009} & \texttt{c78} & \texttt{8e5}\\
7 & \texttt{4021} & \texttt{3e8a} & \texttt{1}\\
8 & \texttt{1002b} & \texttt{2878} & \texttt{689}\\
9 & \texttt{40009} & \texttt{303be} & \texttt{12d39}\\
10 & \texttt{100009} & \texttt{a3085} & \texttt{1}\\
11 & \texttt{400003} & \texttt{662cc} & \texttt{3205f9}\\
12 & \texttt{100001b} & \texttt{d0842d} & \texttt{1}\\
13 & \texttt{400001b} & \texttt{32f9317} & \texttt{1}\\
14 & \texttt{10000003} & \texttt{15a3baa} & \texttt{6c6a1f9}\\
15 & \texttt{40000003} & \texttt{317d6a85} & \texttt{36559252}\\
16 & \texttt{10000008d} & \texttt{4893e13d} & \texttt{2e37b719}\\
17 & \texttt{40000001b} & \texttt{dcbd299} & \texttt{91607c0b}\\
\end{tabular}
\end{center}

\begin{center}\small
\begin{tabular}{r|lll}
$s$ & $M_s$ (hex) & $b$ (hex) & $w$ (hex)\\\hline
18 & \texttt{1000000035} & \texttt{78c0283c4} & \texttt{1}\\
19 & \texttt{4000000063} & \texttt{1153a3d1ef} & \texttt{16004f10d3}\\
20 & \texttt{10000000039} & \texttt{1f9215dca7} & \texttt{1}\\
21 & \texttt{40000000027} & \texttt{2657c0cd035} & \texttt{374caba3695}\\
22 & \texttt{100000000021} & \texttt{fe622270c1c} & \texttt{1}\\
23 & \texttt{400000000003} & \texttt{17c45ffbd76} & \texttt{29bd79b1ae4}\\
24 & \texttt{100000000002d} & \texttt{fed891dbe6c9} & \texttt{ec7a6a1920af}\\
25 & \texttt{400000000001d} & \texttt{2907b6c341c09} & \texttt{1}\\
26 & \texttt{10000000000009} & \texttt{c6d27ccd2b0df} & \texttt{432bf4829f702}\\
27 & \texttt{4000000000007d} & \texttt{28047cef28c34e} & \texttt{1}\\
28 & \texttt{100000000000095} & \texttt{a586528c5b1c9} & \texttt{1}\\
29 & \texttt{400000000000063} & \texttt{243f16ec4e21119} & \texttt{1}\\
30 & \texttt{1000000000000003} & \texttt{8c388b10c413f59} & \texttt{1}\\
31 & \texttt{4000000000000069} & \texttt{12dfcd22c3b1728b} & \texttt{1}\\
32 & \texttt{1000000000000001b} & \texttt{ae3111b3bb81428f} & \texttt{c171e75cc47c2b2e}\\
\end{tabular}
\end{center}

The ancillary file \path{inner_critical_certificates.json} also records
the full factorizations of $A,B$, every nonidentity residue
$a^{d/p}$ for a prime $p\mid d$, and recursive Lucas primality
certificates for those primes. Verification consists of the following
finite identities, carried out by \path{verify_inner_critical.py}.
The additional \path{verify_inner_symmetry.py} checks the
four-torsion identities and rational Lang-fiber multiplier at
all 31 certificate points, and enumerates every primitive-norm
fiber for $s=2,\ldots,6$. It checks four-point orbits, order
preservation, divisibility by four and the exact integer
multiplicity distributions underlying the character symmetries.
The new verification logs and runtime metadata are supplied with
the ancillary files; these finite checks supplement the paper
proof of Proposition~\ref{prop:inner-four-torsion}.
First, $M_s$ has degree $n=2s$, and
\[
 X^{2^n}\equiv X\pmod {M_s},\qquad
 \gcd(M_s,X^{2^{n/r}}-X)=1\quad(r\mid n\text{ prime}),
\]
which certify irreducibility. Second, $b^A=w^A=1$,
$b^{A/p}\ne1$ for every prime $p\mid A$, $c=1+b+w\ne0$,
and $\operatorname{Tr}_{E/\mathbb F_2}(b/c^2)=1$.
Third, in the quadratic field one checks
\[
 a^d=(1+a)^d=1,\quad a^B=b,\quad(1+a)^B=w,\quad
 a^{d/p}\ne1\quad(p\mid d\text{ prime}).
\]
Primality is certified without probable-prime assumptions: the base
case is $2$; for an integer $p>2$ one supplies a complete recursively
certified factorization of $p-1$ and an integer $v$ with
$v^{p-1}\equiv1\pmod p$ and
$\gcd(v^{(p-1)/r}-1,p)=1$ for every prime $r\mid p-1$.
For any prime divisor $\ell$ of $p$, these conditions force the order
of $v$ modulo $\ell$ to be $p-1$, hence $\ell\ge p$ and $p$ is prime.
The independent verifier uses different field multiplication and
powering implementations from the certificate finder; it requires
only the Python standard library, run without the \texttt{-O} flag.

The small-prime list used in the analytic constant is
\[
\begin{gathered}
5,13,17,29,37,41,53,61,73,89,97,101,\\
109,113,137,149,157,173,181,193,197,229,233,241.
\end{gathered}
\]
Their product is
$6045408114863853991373345088496297320256672385$;
the integer comparison is $256^{24}<32^8$ times this product.
The verifier checks this comparison as well.

As a separate small-field audit, multiplicative-subgroup enumeration
and polynomial gcds with the M\"obius sieve agree on the following
counts. Here $N_d^{\mathrm{prim}}$ has the meaning in
Theorem~\ref{thm:inner-primitive-count}.
\[
\begin{array}{c|r|r|r|r|r}
s&d&T_d&|\mathcal R_d|&N_d^{\mathrm{prim}}&D_d\\\hline
2&85&24&24&16&8\\
3&585&86&72&48&24\\
4&4369&240&240&224&208\\
5&33825&1214&960&520&240\\
6&266305&4104&3960&2928&1992
\end{array}
\]
The data also verify the genus-one Hasse bounds on every primitive
norm fiber in this small range. They confirm that the diagonal
$b=w$ gives no realizing slope for $s=3,5$.
These supplementary counts do not replace the general proof.
The present all-dimensional theorem uses the classical Weil bound
and a finite exact certificate, and is outside the Lean formalization.

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
