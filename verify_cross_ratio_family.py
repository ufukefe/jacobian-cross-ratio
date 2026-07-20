"""Independent exact verifier for the fixed-generic-degree Jacobian family.

The script reconstructs the family from its defining frame and checks finite
symbolic identities. It does not replace the geometric proof in proof.md.
"""

import sympy as sp

x, y, z = sp.symbols("x y z")
lam, mu = sp.symbols("lambda mu", nonzero=True)
t1, t2, t3, d = sp.symbols("t1 t2 t3 d")


def frame_map(parameter, X=x, Y=y, Z=z):
    """Return the polynomial map F_parameter = (A, B, C)."""
    C = 2 * X - (3 * Y + 4 * (1 + parameter)) * X**2 - X**3 * Z
    T = Y + 1 / X
    g3 = C * (1 + C) * (1 + parameter * C)
    B = sp.cancel(2 / X - 3 * g3 * T**2 + 4 * T)
    A = sp.cancel((g3 * T**3 - 2 * T**2 + T * B) / 2)
    return tuple(sp.expand(value) for value in (A, B, C))


def is_zero(expression):
    """Test an exact rational-polynomial identity."""
    return sp.cancel(sp.expand(expression)) == 0


A, B, C = frame_map(lam)
checks = []

# Polynomiality after cancellation.
checks.extend(
    [
        ("A polynomial", sp.Poly(A, x, y, z, lam) is not None),
        ("B polynomial", sp.Poly(B, x, y, z, lam) is not None),
        ("C polynomial", sp.Poly(C, x, y, z, lam) is not None),
    ]
)

# Constant Jacobian determinant.
jacobian = sp.Matrix(
    [
        [sp.diff(A, variable) for variable in (x, y, z)],
        [sp.diff(B, variable) for variable in (x, y, z)],
        [sp.diff(C, variable) for variable in (x, y, z)],
    ]
)
checks.append(("det DF_lambda = -2", is_zero(jacobian.det() + 2)))

# A symbolic triple collision. This formula excludes isolated parameter values
# at which the displayed parametrization has a zero denominator; lambda=2 is
# the concrete example used in the README.
points_xy = [
    (-1 / lam, lam),
    (1 / (2 * lam + 1), -2 * lam),
    ((lam + 1) / (lam * (2 * lam + 1)), -2 * lam),
]
points = []
for X, Y in points_xy:
    W = 2 * X - (3 * Y + 4 * (1 + lam)) * X**2
    Z = sp.factor((W - 1) / X**3)  # Forces C=1 exactly.
    points.append((X, Y, Z))

for index, (X, Y, Z) in enumerate(points, start=1):
    image = tuple(
        sp.factor(sp.cancel(value.subs({x: X, y: Y, z: Z})))
        for value in (A, B, C)
    )
    checks.append(
        (f"collision {index}", image == (0, -2 * lam, 1))
    )

roots = [sp.factor(Y + 1 / X) for X, Y, _ in points]
checks.append(
    ("correct roots", roots == [0, 1, -lam / (lam + 1)])
)

# Explicit lambda <-> 1/lambda equivalence.
A_inverse, B_inverse, C_inverse = frame_map(1 / lam)
A_scaled, B_scaled, C_scaled = frame_map(
    lam, x / lam, lam * y, lam**2 * z
)
checks.extend(
    [
        ("lambda inversion a", is_zero(A_inverse - A_scaled / lam**2)),
        ("lambda inversion b", is_zero(B_inverse - B_scaled / lam)),
        ("lambda inversion c", is_zero(C_inverse - lam * C_scaled)),
    ]
)


def J(parameter):
    """Symmetric cross-ratio invariant, up to an irrelevant constant factor."""
    return (
        (parameter**2 - parameter + 1) ** 3
        / (parameter**2 * (parameter - 1) ** 2)
    )


orbit = [
    lam,
    1 / lam,
    1 - lam,
    1 / (1 - lam),
    lam / (lam - 1),
    (lam - 1) / lam,
]
for index, candidate in enumerate(orbit, start=1):
    checks.append(
        (f"J orbit {index}", is_zero(J(candidate) - J(lam)))
    )

numerator = sp.factor(
    sp.together(J(mu) - J(lam)).as_numer_denom()[0]
)
expected_factorization = -(
    (lam - mu)
    * (lam * mu - 1)
    * (lam + mu - 1)
    * (lam * mu - lam + 1)
    * (lam * mu - lam - mu)
    * (lam * mu - mu + 1)
)
checks.append(
    (
        "J factorization",
        is_zero(numerator - expected_factorization),
    )
)

# Algebra used in the auxiliary-coordinate elimination discussion.
direction_matrix = sp.Matrix(
    [
        [d * t1**3, 3 * d * t1**2, -1],
        [d * t2**3, 3 * d * t2**2, -1],
        [d * t3**3, 3 * d * t3**2, -1],
    ]
)
expected_direction_determinant = -3 * d**2 * (
    (t1 - t2)
    * (t1 - t3)
    * (t2 - t3)
    * (t1 * t2 + t1 * t3 + t2 * t3)
)
checks.append(
    (
        "direction determinant",
        is_zero(direction_matrix.det() - expected_direction_determinant),
    )
)

# Degeneration of the fiber cubic at the two nonzero roots of gamma_lambda.
T, a, b, c = sp.symbols("T a b c")
R = c * (1 + c) * (1 + lam * c) * T**3 - 2 * T**2 + b * T - 2 * a
checks.extend(
    [
        (
            "degeneration c=-1",
            is_zero(R.subs(c, -1) - (-2 * T**2 + b * T - 2 * a)),
        ),
        (
            "degeneration c=-1/lambda",
            is_zero(
                R.subs(c, -1 / lam) - (-2 * T**2 + b * T - 2 * a)
            ),
        ),
        (
            "quadratic discriminant",
            sp.discriminant(-2 * T**2 + b * T - 2 * a, T)
            == b**2 - 16 * a,
        ),
    ]
)

for name, passed in checks:
    print(("PASS" if passed else "FAIL"), "-", name)

failed = [name for name, passed in checks if not passed]
if failed:
    raise AssertionError(f"Failed checks: {failed}")

print("Correct collision points:", points)
print("Correct roots:", roots)
print("J difference numerator:", numerator)
print(f"ALL {len(checks)} INDEPENDENT CHECKS PASSED")
