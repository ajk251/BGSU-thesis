
from predicates.predicates import predicate, PREDICATES

# from math import nan, isinf, isclose
from numbers import Integral, Number, Real

import collections.abc as abc
import math

# numerical -------------------------------------

@predicate(alias=['modof?', '%=', 'mod-of?'])
def is_modulus_of(b, n) -> bool:
    '''Tests b % n == 0'''
    return b % n == 0


@predicate(alias=['is-even', 'even?'])
def is_even(n) -> bool:
    '''Tests if a given number is even'''
    return n % 2 == 0


@predicate(alias=['is-odd', 'odd?'])
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


@predicate(alias=['int?', 'integer?', 'ℤ?'])
def is_int(n) -> bool:
    '''Tests if a given value is an integer'''
    return isinstance(n, int) or isinstance(n, Integral)


@predicate(alias=['float?', 'real?', 'ℝ?'])
def is_float(n) -> bool:
    '''Tests if a given value is an float'''
    return isinstance(n, float) or isinstance(n, Real)


@predicate(alias='number?')
def is_number(n) -> bool:
    '''Test whether a number is a sub-class of Number'''
    return isinstance(n, Number)

# Fraction, Complex...


@predicate(alias='nan?')
def is_nan(n) -> bool:
    '''Tests whether a value is Not-A-Number or nan (Nan, NaN)'''
    return math.isnan(n)


@predicate(alias='close?')
def is_close(a, b, tol=0.00001):
    '''Tests whether a float is close in real and absolute terms'''
    return math.isclose(a, b, rel_tol=tol, abs_tol=tol)

# bounds testing --------------------------------
# these names need some thought…


@predicate(alias=['between?', 'in[]?'])
def between(n, lower, upper) -> bool:
    return lower <= n <= upper


@predicate(alias=['in[)?'])
def in_interval(n, lower, upper) -> bool:
    return lower <= n < upper


@predicate(alias=['in()?'])
def is_within(n, lower, upper) -> bool:
    return lower < n < upper


@predicate(alias=['outside?', 'out)('])
def is_outside(n, lower, upper):
    return lower >= n and n <= upper
