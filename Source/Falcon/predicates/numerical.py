
from Falcon.predicates.predicates import predicate, PREDICATES

# from math import nan, isinf, isclose
from numbers import Integral, Number, Real

import collections.abc as abc
import math

# numerical -------------------------------------

@predicate(alias=['int?', 'is-int?'])
def is_integer(n) -> bool:
    return isinstance(n, int)

@predicate(alias=['float?', 'int?'])
def is_float(n) -> bool:
    return isinstance(n, float)

# -----------------------------------------------

@predicate(alias=['modof?', '%=', 'mod-of?'], doc_error=True)
def is_modulus_of(a, n) -> bool:
    '''Value a % n != 0'''
    if a < 1: return False
    return a % n == 0


@predicate(alias=['is-even', 'even?'])
def is_even(n) -> bool:
    '''Tests if a given number is even'''
    return n % 2 == 0


@predicate(alias=['is-odd?', 'odd?'])
def is_odd(n) -> bool:
    '''Tests if a given number is odd'''
    return n % 2 != 0


@predicate(alias='positive?')
def is_positive(n) -> bool:
    '''Tests whether the values is a number greater than 0'''
    return isinstance(n, Number) and n > 0


@predicate(alias='negative?')
def is_negative(n) -> bool:
    '''Tests whether the value is a number and less than 0'''
    return isinstance(n, Number) and n < 0


# Fraction, Complex...


@predicate(alias=['nan?', 'is-nan?'])
def is_nan(n) -> bool:
    '''Tests whether a value is Not-A-Number or nan (Nan, NaN)'''
    return math.isnan(n)


@predicate(alias=['inf?', 'is-inf?', '∞?'])
def is_inf(n) -> bool:
    return math.isinf(n)


@predicate(alias='close?')
def is_close(a, b, tol=0.00001):
    '''Tests whether a float is close in real and absolute terms'''
    return math.isclose(a, b, rel_tol=tol, abs_tol=tol)


@predicate(alias=['safe-number?', 'not-nan-or-inf?', 'valid-float?'])
def is_valid_float(n: float) -> bool:
    """Returns whether a number is an actual float, not a NaN or Inf."""
    return not (math.isnan(n) or math.isnan(n))


@predicate(alias=['is-nan-inf?', 'nan-or-inf?'])
def is_nan_or_inf(n: float) -> bool:
    """Returns whether a number is an actual float, not a NaN or Inf."""
    return not (math.isnan(n) or math.isnan(n))


# bounds testing --------------------------------
# these names need some thought…


@predicate(alias=['between?'])
def between(n, lower, upper) -> bool:
    return lower <= n <= upper


@predicate(alias=['in-interval?'])
def in_interval(n, lower, upper) -> bool:
    return lower <= n < upper


@predicate(alias=['within?'])
def is_within(n, lower, upper) -> bool:
    return lower < n < upper


@predicate(alias=['outside?'])
def is_outside(n, lower, upper):
    return lower >= n and n <= upper


@predicate(alias=['plus-minus?', '±'])
def plus_minus(value, n, m) -> bool:
    return (n - m) <= value <= (n + m)
