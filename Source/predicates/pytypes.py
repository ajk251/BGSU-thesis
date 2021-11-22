
from predicates.predicates import predicate

from abc import ABC
from decimal import Decimal
from fractions import Fraction

import numbers
import types


# use:
#   https://docs.python.org/3/library/types.html#module-types
#   https://docs.python.org/3/library/types.html#module-types

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
    return isinstance(s, ABC.Sequence) #or issubclass(s, abc.Sequence)

# numbers ---------------------------------------

# I'm not sure how redundant some of this is...


@predicate(alias=['number?'])
def is_number(n):
    return isinstance(n, numbers.Number)


@predicate(alias=['is-int?', 'int?'])
def is_integer(n) -> bool:
    return isinstance(n, numbers.Integral) and isinstance(n, int)


@predicate(alias=['is-real?', 'is-float?', 'float?'])
def is_float(n) -> bool:
    return isinstance(n, numbers.Real) and isinstance(n, float)


@predicate(alias=['floating-int?', 'real-int?'])
def is_float_int(n) -> bool:
    return float.is_integer(n)


@predicate(alias=['is-fraction?', 'is/?', 'fraction?'])
def is_fraction(n):
    return isinstance(n, numbers.Rational) and isinstance(n, Fraction)


@predicate(alias=['is-complex?', 'complex?'])
def is_complex(n) -> bool:
    return isinstance(n, numbers.Complex) and isinstance(n, complex)


@predicate(alias=['is-decimal?', 'decimal?'])
def is_decimal(n):
    return isinstance(n, Decimal)


# generic types ---------------------------------

@predicate(alias=['function?'])
def is_function(fn) -> bool:
    return isinstance(fn, types.FunctionType) or isinstance(fn, types.LambdaType)


@predicate(alias='func?')
def is_pyfunc(fn) -> bool:
    return isinstance(fn, types.FunctionType)


@predicate(alias=['λ?', 'lambda?'])
def is_lambda(fn) -> bool:
    return isinstance(fn, types.LambdaType)


@predicate(alias=['callable?'])
def is_callable(obj):
    return callable(obj)
