
from math import isinf, isnan, isclose
from numbers import Number

from ComplexNumber import Complex

from functools import wraps

def fail_false(fn):
    @wraps(fn)
    def call_fn(*args, **kwargs):

        try:
            result = fn(*args, **kwargs)
        except Exception as error:
            result = False
        
        return result
    return call_fn


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

# unary functions
@fail_false
def property_additive_identity(a):
    """C + 0 == 0 + C is ℂ"""
    zero = Complex(0.0, 0.0)
    return isinstance(a + zero, Complex) and isinstance(zero + a, Complex) and (a + zero == zero + a)

@fail_false
def property_multiplicative_identity(a):
    """C * 1 == 1 * C is ℂ"""
    one = Complex(1.0, 1.0)
    return isinstance(a * one, Complex) and isinstance(one * a, Complex) and (a * one == one * a)

@fail_false
def property_additive_inverse(a):
    """⁻z + z == z + ⁻z == 0"""
    return (-a + a) == Complex(0.0, 0.0) and (a + -a) == Complex(0.0, 0.0)

# these are binary functions
@fail_false
def property_closure_add(a, b):
    """C₁ + C₂ == ℂ"""
    return isinstance(a + b, Complex)

@fail_false
def property_closure_multiply(a, b):
    """C₁ * C₂ == ℂ"""
    return isinstance(a * b, Complex)

@fail_false
def property_commutative_add(a, b):
    """C₁ + C₂ == C₂ + C₁"""
    return a + b == b + a

@fail_false
def property_commutative_multiply(a, b):
    """C₁ ⨯ C₂ == C₂ ⨯ C₁"""
    return a * b == b * a

@fail_false
def property_multiplicative_inverse(a, b):
    """C + ~z == 1, where z is C¯¹"""
    return a * ~b == Complex(1.0, 1.0)

# these take 3 args
@fail_false
def property_associative_add(a, b, c):
    """(C₁ + C₂) + C₃ == C₁ + (C₂ + C₃)"""
    return ((a + b) + c) == a + ((b + c))

@fail_false
def property_associative_multiply(a, b, c):
    """(C₁ + C₂) + C₃ == C₁ + (C₂ + C₃)"""
    return ((a * b) * c) == a * ((b * c))

@fail_false
def property_distributive(a, b, c):
    """C₁(C₂ + C₃) == C₁C₂ + C₁C₃ ∧ (C₁ + C₂) + C₃ == C₁C₃ + C₁C₂"""
    c1 = (a + b) * c
    c2 = c*b + c*a
    c3 = a * (b + c)
    c4 = a*b + a*c
    return isclose(c1.real, c2.real) and isclose(c1.imaginary, c2.imaginary) and \
           isclose(c3.real, c4.real) and isclose(c3.imaginary, c4.imaginary) 

# --------------------------------

def valid_complex(complex_number):
    return isinstance(complex_number, Number) and \
           isinstance(complex_number, Complex)

def valid_number(complex_number):
    # ensures it is a Complex, to fail gracefully
    return isinstance(complex_number, Complex) and \
           isinstance(complex_number.real, float) and \
           isinstance(complex_number.imaginary, float) and \
           not (isinf(complex_number.real) and isinf(complex_number.imaginary)) and \
           not (isnan(complex_number.real) and isnan(complex_number.imaginary))

@fail_false
def complex_equal(a, b):
    return Complex(a[0] + a[0], b[1] + b[1]) == Complex(a[0] + a[0], b[1] + b[1])

@fail_false
def complex_not_equal(a, b):
    return Complex(a[0] + a[0], b[1] + b[1]) != Complex(a[0] + a[0], b[1] + b[1])

@fail_false
def complex_add(a, b):
    return (Complex(a[0], a[1]) + Complex(b[0], b[1])) == Complex(a[0] + b[0], a[1] + b[1])

@fail_false
def complex_sub(a, b):
    return (Complex(a[0], a[1]) - Complex(b[0], b[1])) == Complex(a[0] - b[0], a[1] - b[1])

@fail_false
def complex_mult(a, b):
    return (Complex(a[0], a[1]) * Complex(b[0], b[1])) == Complex(a[0] * b[0], a[1] * b[1])

@fail_false
def complex_div(a, b):
    # I don't think this is right…
    (Complex(a[0], a[1]) / Complex(b[0], b[1])) == Complex(a[0] / a[0], b[1] / b[1])

@fail_false
def complex_radd(a, b):
    a += b
    return a

@fail_false
def complex_rsub(a, b):
    print(id(a))
    l = id(a)
    a -= b
    print(id(a))
    return id(l) == id(a)

@fail_false
def complex_rmul(a, b):
    a *= b
    return a
