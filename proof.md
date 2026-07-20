# Proof sketch: a cross-ratio obstruction

This note is **unrefereed**. It separates the exact symbolic identities checked by `verify_cross_ratio_family.py` from the geometric argument.

## 1. Definition and the frame determinant

Fix

\[
\lambda\in\mathbb C\setminus\{0,1\}.
\]

Set

\[
\begin{aligned}
w_\lambda(x,y)&=2x-\bigl(3y+4(1+\lambda)\bigr)x^2,\\
c&=w_\lambda(x,y)-x^3z,\\
t&=y+\frac1x,\\
g_\lambda(c)&=c(1+c)(1+\lambda c),\\
b&=\frac2x-3g_\lambda(c)t^2+4t,\\
2a&=g_\lambda(c)t^3-2t^2+tb.
\end{aligned}
\]

After cancellation, \(a,b,c\) are polynomials in \(x,y,z\). Define

\[
F_\lambda=(a,b,c):\mathbb C^3\to\mathbb C^3.
\]

Introduce \(r=2/x\) and

\[
h(t,c)=g_\lambda(c)t^3-2t^2.
\]

Then

\[
b=r-h_t(t,c),\qquad 2a=h(t,c)+tb.
\]

A direct Jacobian calculation gives

\[
\det\frac{\partial(t,r,c)}{\partial(x,y,z)}=-2x
\]

and

\[
\det\frac{\partial(a,b,c)}{\partial(t,r,c)}=\frac r2=\frac1x.
\]

Therefore

\[
\det DF_\lambda=-2.
\]

These identities, together with polynomiality, are checked exactly in the verifier.

## 2. Fiber dictionary

For a target \(q=(a,b,c)\), define

\[
R_q(T)=g_\lambda(c)T^3-2T^2+bT-2a.
\]

The defining identities imply

\[
R_q(t)=0,
\qquad
R_q'(t)=3g_\lambda(c)t^2-4t+b=\frac2x.
\]

Hence every preimage with \(x\ne0\) determines a **simple** root of \(R_q\). Conversely, every simple root \(t\) reconstructs a unique point:

\[
x=\frac2{R_q'(t)},
\qquad
y=t-\frac{R_q'(t)}2,
\qquad
z=\frac{w_\lambda(x,y)-c}{x^3}.
\]

Thus simple roots of \(R_q\) are in bijection with the \(x\ne0\) part of the fiber.

On the flat stratum \(x=0\), direct cancellation gives

\[
F_\lambda(0,y,z)
=
\bigl(z+q_\lambda(y),\,y,\,0\bigr),
\]

where

\[
q_\lambda(y)
=4y^2+12(1+\lambda)y+16\lambda^2+24\lambda+16.
\]

Therefore the whole plane \(\{c=0\}\) is covered.

For a generic target, \(R_q\) is a cubic with three simple roots, so \(F_\lambda\) has generic degree \(3\).

## 3. The omitted set

Write

\[
\operatorname{Omit}(F_\lambda)
=\mathbb C^3\setminus F_\lambda(\mathbb C^3).
\]

There are three cases.

### 3.1. Away from the roots of \(g_\lambda\)

Assume

\[
c\notin\left\{0,-1,-\frac1\lambda\right\}.
\]

Then \(g_\lambda(c)\ne0\), so \(R_q\) is cubic. A cubic has no simple root exactly when it is a cube:

\[
R_q(T)=g_\lambda(c)(T-\tau)^3.
\]

Comparing coefficients yields

\[
\tau=\frac2{3g_\lambda(c)},
\qquad
b=\frac4{3g_\lambda(c)},
\qquad
a=\frac4{27g_\lambda(c)^2}.
\]

This gives the omitted component

\[
\Gamma_\lambda
=V\!\left(12a-b^2,\;3b\,g_\lambda(c)-4\right).
\]

### 3.2. At \(c=-1\) and \(c=-1/\lambda\)

At either nonzero root \(c_*\) of \(\gamma_\lambda(c)=(1+c)(1+\lambda c)\), the cubic term vanishes and

\[
R_q(T)=-2T^2+bT-2a.
\]

This quadratic has no simple root exactly when its discriminant vanishes:

\[
b^2-16a=0.
\]

Since \(c_*\ne0\), the flat stratum does not supply an additional preimage. Hence two more omitted components are

\[
K_{-1}=V(c+1,b^2-16a),
\]

and

\[
K_{-1/\lambda}=V\!\left(c+\frac1\lambda,b^2-16a\right).
\]

### 3.3. At \(c=0\)

The flat stratum covers every target with \(c=0\), so no omitted component occurs there.

Consequently

\[
\boxed{
\operatorname{Omit}(F_\lambda)
=
\Gamma_\lambda\sqcup K_{-1}\sqcup K_{-1/\lambda}.
}
\]

## 4. The intrinsic punctured-rational component

Each \(K_{c_*}\) is isomorphic to \(\mathbb A^1\): use \(b\) as a coordinate and set \(a=b^2/16\). Therefore

\[
\mathcal O(K_{c_*})^*=\mathbb C^*.
\]

For \(\Gamma_\lambda\), the equations solve \(a,b\) as rational functions of \(c\), giving

\[
\mathcal O(\Gamma_\lambda)
\cong
\mathbb C\left[c,\frac1{c(1+c)(1+\lambda c)}\right].
\]

Thus

\[
\Gamma_\lambda
\cong
\mathbb A^1\setminus
\left\{0,-1,-\frac1\lambda\right\}
\cong
\mathbb P^1\setminus
\left\{\infty,0,-1,-\frac1\lambda\right\}.
\]

Its coordinate ring has nonconstant units, so \(\Gamma_\lambda\) cannot be isomorphic to either affine-line component. It is therefore intrinsically distinguished inside the omitted set.

## 5. Equivalence forces equality of the cross-ratio invariant

Say that \(F_\lambda\) and \(F_\mu\) are polynomially equivalent if

\[
F_\mu=\Phi\circ F_\lambda\circ\Psi
\]

for polynomial automorphisms \(\Phi,\Psi\) of \(\mathbb C^3\).

Then

\[
\operatorname{Omit}(F_\mu)
=
\Phi\bigl(\operatorname{Omit}(F_\lambda)\bigr).
\]

Because \(\Gamma\) is the unique omitted component with nonconstant units, \(\Phi\) restricts to an isomorphism

\[
\Gamma_\lambda\cong\Gamma_\mu.
\]

An isomorphism of smooth affine curves extends uniquely to an isomorphism of their smooth projective completions. Hence there is a Möbius transformation carrying

\[
\left\{\infty,0,-1,-\frac1\lambda\right\}
\]

to

\[
\left\{\infty,0,-1,-\frac1\mu\right\}.
\]

The six anharmonic transforms of the parameter are

\[
\lambda,\quad
\frac1\lambda,\quad
1-\lambda,\quad
\frac1{1-\lambda},\quad
\frac\lambda{\lambda-1},\quad
\frac{\lambda-1}\lambda.
\]

They are separated by the symmetric cross-ratio invariant

\[
J(\lambda)
=
\frac{(\lambda^2-\lambda+1)^3}
{\lambda^2(\lambda-1)^2}.
\]

Indeed, the verifier checks the exact factorization

\[
\begin{aligned}
\operatorname{num}\bigl(J(\mu)-J(\lambda)\bigr)
={}&-(\lambda-\mu)(\lambda\mu-1)(\lambda+\mu-1)\\
&\cdot(\lambda\mu-\lambda+1)
(\lambda\mu-\lambda-\mu)
(\lambda\mu-\mu+1).
\end{aligned}
\]

Therefore

\[
F_\lambda\sim F_\mu
\quad\Longrightarrow\quad
J(\lambda)=J(\mu).
\]

Since \(J\) is a nonconstant rational function with finite fibers, it takes uncountably many values. Choosing one parameter from each distinct \(J\)-fiber gives uncountably many pairwise-inequivalent Keller maps, all of generic degree \(3\).

## 6. A realized symmetry

The verifier also checks the explicit equivalence

\[
F_{1/\lambda}
=
\Phi_\lambda\circ F_\lambda\circ\Psi_\lambda,
\]

where

\[
\Psi_\lambda(x,y,z)
=\left(\frac x\lambda,\lambda y,\lambda^2z\right)
\]

and

\[
\Phi_\lambda(a,b,c)
=\left(\frac a{\lambda^2},\frac b\lambda,\lambda c\right).
\]

Thus the cross-ratio invariant is not merely detecting a presentation artifact: at least one nontrivial anharmonic symmetry is realized by explicit coordinate changes.

## 7. Verification boundary

The script checks:

- cancellation to polynomial coordinates;
- \(\det DF_\lambda=-2\);
- the symbolic three-point collision used for the concrete example;
- the \(\lambda\leftrightarrow1/\lambda\) equivalence;
- invariance of \(J\) under all six anharmonic transforms;
- the full six-factor identity for \(J(\mu)-J(\lambda)\);
- degeneration of the cubic to the quadratic at \(c=-1,-1/\lambda\).

The script does **not** replace the geometric steps involving omitted sets, intrinsic component recognition, or projective completion of affine curves. Those are the human-readable steps above and should receive independent mathematical review.
