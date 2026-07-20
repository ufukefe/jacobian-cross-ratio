# Jacobian cross-ratio family

> **Status:** unrefereed research note. The exact algebraic identities in this repository are independently machine-checked; the geometric argument is written out in [`proof.md`](proof.md) for public scrutiny. The two-variable Jacobian problem is untouched.

This repository records a candidate follow-on observation about the new three-dimensional Jacobian counterexample mechanism:

> There are **uncountably many pairwise inequivalent polynomial Keller maps**
> \(F_\lambda:\mathbb C^3\to\mathbb C^3\), all with constant Jacobian \(-2\) and generic fiber cardinality \(3\).

The proposed obstruction is the cross-ratio invariant

\[
J(\lambda)=\frac{(\lambda^2-\lambda+1)^3}{\lambda^2(\lambda-1)^2}.
\]

If \(F_\lambda\) and \(F_\mu\) are equivalent under polynomial automorphisms of source and target, the omitted geometry forces

\[
J(\lambda)=J(\mu).
\]

Since \(J\) is nonconstant and has finite fibers, distinct \(J\)-values yield uncountably many inequivalent classes.

## The family

For \(\lambda\in\mathbb C\setminus\{0,1\}\), set

\[
\begin{aligned}
c &= 2x-\bigl(3y+4(1+\lambda)\bigr)x^2-x^3z,\\
t &= y+\frac1x,\\
g(c)&=c(1+c)(1+\lambda c),\\
b &= \frac2x-3g(c)t^2+4t,\\
a &= \frac{g(c)t^3-2t^2+tb}{2}.
\end{aligned}
\]

Although this presentation uses \(1/x\), all denominators cancel: \(a,b,c\in\mathbb C[x,y,z]\). Write \(F_\lambda=(a,b,c)\). Exact symbolic differentiation gives

\[
\det DF_\lambda\equiv -2.
\]

For a target \((a,b,c)\), the non-flat preimages are controlled by

\[
R(T)=c(1+c)(1+\lambda c)T^3-2T^2+bT-2a.
\]

Every simple root reconstructs one preimage, so a generic target has three preimages.

## Concrete check: \(\lambda=2\)

The following distinct points map to the same target:

\[
\left(-\frac12,2,52\right),\qquad
\left(\frac15,-4,-75\right),\qquad
\left(\frac3{10},-4,-\frac{400}{27}\right)
\]

and

\[
F_2\left(-\frac12,2,52\right)
=F_2\left(\frac15,-4,-75\right)
=F_2\left(\frac3{10},-4,-\frac{400}{27}\right)
=(0,-4,1).
\]

## Reproduce the exact checks

```bash
python -m pip install -r requirements.txt
python verify_cross_ratio_family.py
```

Expected final line:

```text
ALL 22 INDEPENDENT CHECKS PASSED
```

The number 22 is only the number of assertions in this script—not a standard benchmark. The checks include polynomiality, \(\det DF_\lambda=-2\), the explicit collision, the \(\lambda\leftrightarrow1/\lambda\) equivalence, the six cross-ratio symmetries, and the relevant degeneration identities.

## What the script does—and does not—prove

The script verifies finite symbolic identities exactly. The implication

\[
F_\lambda\sim F_\mu\Longrightarrow J(\lambda)=J(\mu)
\]

also uses algebraic geometry: the complete omitted-set description, intrinsic identification of its punctured-rational component, and extension of affine-curve isomorphisms to \(\mathbb P^1\). Those steps are presented in [`proof.md`](proof.md), not delegated to numerical testing.

## Credit and provenance

- The original explicit counterexample was announced by **Levent Alpöge**, crediting **Akhil Mathew** for the question and **Fable** for producing the example.
- The cubic reduction and higher-generic-degree construction were developed publicly by **Alexis Gallagher**, with AI assistance: [jacobianfun.org](https://jacobianfun.org/jacobian-explained).
- This repository records a candidate cross-ratio/moduli follow-on developed by **Ufuk Efe** through interaction with Fable and GPT-5.6 Sol, followed by an independent SymPy reconstruction of the finite algebraic checks.

Useful public context:

- [Jacobian counterexample explained](https://jacobianfun.org/jacobian-explained)
- [Explicit cubic model and \(S_3\) monodromy discussion](https://mathoverflow.net/questions/513387/)
- [Wolfram MathWorld: Jacobian Conjecture](https://mathworld.wolfram.com/JacobianConjecture.html)

## Review invitation

This is intentionally public and unrefereed. Please open an issue with a precise broken identity, missing hypothesis, prior reference, or gap in the geometric argument.
