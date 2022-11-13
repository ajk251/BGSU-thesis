
from copy import deepcopy
from itertools import product
from math import isinf, isnan, isclose, inf, nan, pi
from numbers import Number
from random import choices, uniform

from Falcon.predicates import predicate, on_fail_false
from Falcon.domains import domain

# from Tests.ComplexNumber import Complex, ComplexError
from ComplexNumber import Complex, ComplexError

# --------------------------------------------------------

# validity
#   valid floats ∧ no inf or nan
#   valid string representation
#   equals
#   not equals
#   if they are equal, then they cannot be unequal & vice-versa
#   adds/sub/mult
#   can't divide
#   is-same, not-same

# From here: https://www.brainkart.com/article/Basic-Algebraic-Properties-of-Complex-Numbers_39091/
# closure           C₁ + C₂ == ℂ
# closure           C₁ * C₂ == ℂ
# commutative₊      C₁ + C₂ == C₂ + C₁
# commutative⨯      C₁ * C₂ == C₂ * C₁
# associative₊      (C₁ + C₂) + C₃ == C₁ + (C₂ + C₃)
# associative⨯      (C₁ * C₂) + C₃ == C₁ * (C₂ + C₃)
# additive id       C + 0 == 0 + C is ℂ ∧ C == C ∧ C === C
# multiplicative id C * 1 == 1 * C is ℂ ∧ C == C ∧ C === C
# additive inverse  C₁ + ⁻C₂ == ⁻C₁ + C₂        ￫ z value has to be found!
# mult inverse      C + ~z == 1                 ￫ z value has to be found!
# distributive      C₁(C₂ + C₃) == C₁C₂ + C₁C₃ ∧ (C₁ + C₂) + C₃ == C₁C₃ + C₁C₂


# I found my own copy-paste mistakes doing this!
# and my negative was wrong
# and I needed isclose for the distributive! The floats accumulate errors


# -----------------------------------------------

@domain(alias=['ℝ²', 'Reals2'])
def Reals2(lower: float = -1000.0, upper: float = 1_000.0, n: int = 100):
    """Yields a tuple of random values, ie (ℝ~uniform, ℝ~uniform)."""

    for _ in range(n):
        yield uniform(lower, upper), uniform(lower, upper)


@domain(alias=['ℂ', 'Complex'])
def ComplexDomain(lower: float = -1_000.0, upper: float = 1_000.0, n: int = 100):
    """Yields a Complex number value"""

    for _ in range(n):
        yield Complex(uniform(lower, upper), uniform(lower, upper))


@domain(alias=['ComplexT&S', 'Complex-TestSolution'])
def ComplexTestSolution():
    """Yields (a,b), Complex, or test solution"""
    values = [(1.0, 1.0, Complex(1.0, 1.0)),
              (11., -1., Complex(11., -1.)),
              (-10., 1., Complex(-10., 1.)),
              (0.0, 0.0, Complex(0.0, 0.0)),
              (1, None, Complex(1, None)),                # these should fail None, ints, nan, inf
              (None, None, Complex(None, None)),
              (1.0, None, Complex(1, None)),
              (inf, inf, Complex(inf, inf)),
              (inf, nan, Complex(inf, nan)),
              (-inf, nan, Complex(-inf, nan)),
              (nan, nan, Complex(nan, nan)),
              (1, 1, Complex(1, 1))]

    for case in values:
        yield case


@domain(alias=['ComplexTest'])
def ComplexTestDomain():
    """Takes a test set of values and uses the cartesian product."""

    values = [1.0,
              0.0,
              349581234123900987620918723404.0,
              23452352345981029487612837649182376419827364912837.1,
              -2352346245323651468435164131685464316846.1,
              1,
              0,
              inf,
              nan,
              pi]

    for a, b in product(values, values):
        yield a, b


def ComplexTestValues(n: int = 100):
    """Takes a set of values, returning two tuple of values, upto n values"""

    values = [1.0, 0.0,
              349581234123900987620918723404.0,
              23452352345981029487612837649182376419827364912837.1,
              -2352346245323651468435164131685464316846.1,
              1, 0, inf, nan, pi]

    i = 0

    while i < n:
        c1 = choices(values, k=2)
        c2 = choices(values, k=2)
        yield c1, c2
        i += 1


# -----------------------------------------------
# for special tests


# @predicate(alias=['complex-test-error?'], is_error=True)
# def complex_test_error_kind(fn, args, a, b):
#     print('here!')
#     return True


@predicate(alias=['agrees?'])
@on_fail_false
def complex_agree(a, b, C: Complex) -> bool:
    """Tests whether the values Complex(a, b) == C, for ComplexTestSolution, and assumes C is valid & well-formed"""

    n = Complex(a, b)

    return n == C and isinstance(n, Complex) and \
           isinstance(n.real, float) and isinstance(n.imaginary, float) and \
           not (isinf(n.real) and isinf(n.imaginary)) and not (isnan(n.real) and isnan(n.imaginary))


# -----------------------------------------------

# unary functions
@predicate(alias=['additive-id?'])
@on_fail_false
def property_additive_identity(a: Complex):
    """C + 0 == 0 + C is ℂ"""
    zero = Complex(0.0, 0.0)
    return isinstance(a + zero, Complex) and isinstance(zero + a, Complex) and (a + zero == zero + a)


@predicate(alias=['multiplicative-id?', 'mult-id?'])
@on_fail_false
def property_multiplicative_identity(a: Complex):
    """C * 1 == 1 * C is ℂ"""
    one = Complex(1.0, 1.0)
    return isinstance(a * one, Complex) and isinstance(one * a, Complex) and (a * one == one * a)


@predicate(alias=['additive-inverse?'])
@on_fail_false
def property_additive_inverse(a: Complex):
    """⁻z + z == z + ⁻z == 0"""
    return (-a + a) == Complex(0.0, 0.0) and (a + -a) == Complex(0.0, 0.0)


# these are binary functions --------------------
@predicate(alias=['closure-additive?', 'closure+?'])
@on_fail_false
def property_closure_add(a: Complex, b: Complex):
    """C₁ + C₂ == ℂ"""
    return isinstance(a + b, Complex)


@predicate(alias=['closure-multiply?', 'closure*?'])
@on_fail_false
def property_closure_multiply(a: Complex, b: Complex):
    """C₁ * C₂ == ℂ"""
    return isinstance(a * b, Complex)


# binary predicates -----------------------------
@predicate(alias=['commutative+?', 'comm+?'])
@on_fail_false
def property_commutative_add(a: Complex, b: Complex):
    """C₁ + C₂ == C₂ + C₁"""
    return a + b == b + a


@predicate(alias=['commutative*?', 'comm*?'])
@on_fail_false
def property_commutative_multiply(a: Complex, b: Complex):
    """C₁ ⨯ C₂ == C₂ ⨯ C₁"""
    return a * b == b * a


@predicate(alias=['multiplicative-inverse?', 'mult-inverse?'])
@on_fail_false
def property_multiplicative_inverse(a: Complex, b: Complex):
    """C + ~z == 1, where z is C¯¹"""
    return a * ~b == Complex(1.0, 1.0)

# these take 3 args -----------------------------

@predicate(alias=['associative+?'])
@on_fail_false
def property_associative_add(a: Complex, b: Complex, c: Complex):
    """(C₁ + C₂) + C₃ == C₁ + (C₂ + C₃)"""
    return ((a + b) + c) == (a + (b + c))


@predicate(alias=['associative*?'])
@on_fail_false
def property_associative_multiply(a: Complex, b: Complex, c: Complex):
    """(C₁ + C₂) + C₃ == C₁ + (C₂ + C₃)"""
    return ((a * b) * c) == a * ((b * c))


@predicate(alias=['distributive?'])
@on_fail_false
def property_distributive(a: Complex, b: Complex, c: Complex):
    """C₁(C₂ + C₃) == C₁C₂ + C₁C₃ ∧ (C₁ + C₂) + C₃ == C₁C₃ + C₁C₂"""
    c1 = (a + b) * c
    c2 = c*b + c*a
    c3 = a * (b + c)
    c4 = a*b + a*c
    return isclose(c1.real, c2.real) and isclose(c1.imaginary, c2.imaginary) and \
           isclose(c3.real, c4.real) and isclose(c3.imaginary, c4.imaginary) 

# properties ------------------------------------

@predicate(alias=['ℂ?', 'complex-num?', 'complex-number?'])
@on_fail_false
def valid_complex(complex_number: Complex):
    return isinstance(complex_number, Number) and \
           isinstance(complex_number, Complex)


@predicate(alias=['valid-complex?'])
@on_fail_false
def valid_number(complex_number: Complex):
    # ensures it is a Complex, to fail gracefully
    return isinstance(complex_number.real, float) and isinstance(complex_number.imaginary, float) and \
           not (isinf(complex_number.real) or isinf(complex_number.imaginary)) and \
           not (isnan(complex_number.real) or isnan(complex_number.imaginary))


# math tests ------------------------------------
@predicate(alias=['complex=?', 'complex-eq?'])
@on_fail_false
def complex_equal(a: Complex, b: Complex):
    return a.real == b.real and a.imaginary == b.imaginary


@predicate(alias=['complex!=?', 'complex≠?', 'complex-ne?'])
@on_fail_false
def complex_not_equal(a: Complex, b: Complex):
    # return Complex(a[0] + a[1], b[0] + b[1]) != Complex(a[0] + a[1], b[0] + b[1])
    return a.real == b.real or a.imaginary == b.imaginary


@predicate(alias=['complex+?'])
@on_fail_false
def complex_add(a: Complex, b: Complex):
    return (Complex(a[0], a[1]) + Complex(b[0], b[1])) == Complex(b[0] + a[0], b[1] + a[1])


@predicate(alias=['complex-?'])
@on_fail_false
def complex_sub(a: Complex, b: Complex):
    return (Complex(a[0], a[1]) - Complex(b[0], b[1])) == Complex(a[0] - b[0], a[1] - b[1])


@predicate(alias=['complex*?', 'complex•'])
@on_fail_false
def complex_mult(a: Complex, b: Complex):
    return (Complex(a[0], a[1]) * Complex(b[0], b[1])) == Complex(a[0] * b[0], a[1] * b[1])


@predicate(alias=['complex-div?', 'complex÷?'])
@on_fail_false
def complex_div(a: Complex, b: Complex):
    return (Complex(a[0], a[1]) / Complex(b[0], b[1])) == Complex(a[0] / b[0], a[1] / b[1])


# Note: id() does not work here ￫ id() changes after operation

@predicate(alias=['complex+=?', 'complex-ra?'])
@on_fail_false
def complex_radd(a: Complex, b: Complex):
    o = deepcopy(a)
    a += b
    return o == Complex(a.real + b.real, a.imaginary + b.imaginary)


@predicate(alias=['complex-=?', 'complex-rs?'])
@on_fail_false
def complex_rsub(a: Complex, b: Complex):
    o = deepcopy(a)
    a -= b
    return o == Complex(a.real - b.real, a.imaginary - b.imaginary)


@predicate(alias=['complex*=?', 'complex-rm?'])
@on_fail_false
def complex_rmul(a: Complex, b: Complex):
    o = deepcopy(a)
    a *= b
    return o == Complex(a.real * b.real, a.imaginary * b.imaginary)


# @predicate(alias=['complex-self?'], is_error=True)
# def complex_div(*args):
#     return True

@on_fail_false
def raises_error(error, error_type) -> bool:
    """Tests that the error is an instance of the specified type"""
    return isinstance(error, error_type)
