
from predicates import predicate, predicates

# from math import nan, isinf, isclose
from numbers import Integral, Number, Real

import collections.abc as abc
import math


# numerical -------------------------------------

@predicate(alias='modof?', complement=True)
def is_modof(b, n) -> bool:
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

# system ----------------------------------------

@predicate(alias='same?')
def is_same(a, b) -> bool:
    '''Tests whether two objects are the same based on memory location'''
    return id(a) == id(b)

@predicate(alias='unique?')
def is_unique(a, b) -> bool:
    '''Tests whether two objects are unique based on memory location'''
    return id(a) != id(b)



# object ----------------------------------------


# https://docs.python.org/3/library/collections.abc.html#module-collections.abc


@predicate(alias='sequence?')
def is_sequence(s) -> bool:
    return isinstance(s, abc.Sequence) #or issubclass(s, abc.Sequence)





# ===============================================

for name, fn in predicates.items():
    print(f'{name}: \t{fn.__name__}')

# print(predicates)

print('\n', '*'*25)
print('sequence? ', predicates['sequence?']([1,2,3]))
print('sequence? ', predicates['sequence?'](4))


print('nan?: ', predicates['nan?'](4))
print('nan?: ', predicates['nan?'](4.3))
# print('nan?: ', predicates['nan?']('a'))

print('close?: ', predicates['close?'](0.000000001, 0.0))