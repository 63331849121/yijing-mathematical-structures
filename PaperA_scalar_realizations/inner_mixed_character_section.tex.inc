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

