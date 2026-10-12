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


