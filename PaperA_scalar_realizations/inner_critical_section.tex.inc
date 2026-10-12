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


