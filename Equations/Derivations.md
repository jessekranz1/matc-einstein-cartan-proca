# Derivations for the Reduced Einstein–Cartan–Proca EFT

## 1. Effective Action

We work in natural units:

\[
G = c = \hbar = 1
\]

with metric signature:

\[
(+,-,-,-)
\]

The effective Einstein–Cartan–Proca action is:

\[
S = \int d^4x \sqrt{-g}
\left[
\frac{M_{Pl}^2}{2}R
-
\frac14 F_{\mu\nu}F^{\mu\nu}
+
\frac12 M_A^2 A_\mu A^\mu
+
\frac12 \partial_\mu \phi \partial^\mu \phi
-
V(\phi)
+
\frac{\alpha}{M_*}\phi F\tilde F
\right]
\]

where:

\[
F_{\mu\nu} = \partial_\mu A_\nu - \partial_\nu A_\mu
\]

and

\[
\tilde F^{\mu\nu}
=
\frac12
\epsilon^{\mu\nu\alpha\beta}
F_{\alpha\beta}
\]

---

## 2. Axial-Vector Equation of Motion

Variation with respect to \(A_\mu\) yields:

\[
\nabla^\nu F_{\nu\mu}
+
M_A^2 A_\mu
=
-
\frac{2\alpha}{M_*}
\tilde F_{\mu\nu}
\partial^\nu \phi
\]

In a homogeneous minisuperspace truncation:

\[
\partial_\mu \phi = (\dot\phi,0,0,0)
\]

Therefore only:

\[
\tilde F^{\mu 0}
\]

contributes dynamically.

This significantly simplifies the numerical implementation.

---

## 3. Continuity Equation

The energy balance equation becomes:

\[
\dot \rho_A
+
3H(\rho_A+p_A)
=
Q
\]

where the source term is:

\[
Q
=
\frac{\alpha}{M_*}
\dot\phi
F\tilde F
\]

This source transfers energy from the scalar sector into the axial-vector sector.

---

## 4. Emergent Scaling Law

Near the high-curvature phase:

\[
\rho_A
\propto
a^{-(6+\delta)}
\]

with:

\[
\delta > 0
\]

interpreted as the nonlinear damping efficiency.

The BKL shear scales as:

\[
\sigma^2 \propto a^{-6}
\]

Therefore the condition:

\[
\delta > 0
\]

is sufficient for axial-torsion dominance over chaotic shear growth.

---

## 5. Stability Island

The reduced EFT remains viable only inside the perturbative stability window:

\[
\alpha_c < \alpha < \alpha_{max}
\]

where:

- \(\alpha_c\) is the minimum coupling needed for BKL suppression.
- \(\alpha_{max}\) is the hyperbolicity ceiling.

Outside this window:

- Under-damped regime:

\[
\alpha < \alpha_c
\]

leads to standard BKL collapse.

- Over-driven regime:

\[
\alpha > \alpha_{max}
\]

triggers gradient instabilities and loss of hyperbolicity.
