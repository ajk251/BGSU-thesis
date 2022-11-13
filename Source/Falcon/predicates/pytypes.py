
from Falcon.predicates.predicates import predicate

from abc import ABC
from decimal import Decimal
from fractions import Fraction
from numbers import Integral, Number, Real

import numbers
import types


# use:
#   https://docs.python.org/3/library/types.html#module-types
#   https://docs.python.org/3/library/types.html#module-types

# system ----------------------------------------

@predicate(alias=['is-None?', 'is-none?', 'None?', 'none?'], doc_error=True)
def is_none(value) -> bool:
    """Value must be None"""
    return value is None


@predicate(alias=['not-none?', 'not-None?'], doc_error=True)
def is_not_none(value):
    """Value must not be None"""
    return value is not None



@predicate(alias='same?')
def is_same(a, b) -> bool:
    """Tests whether two objects are the same based on memory location"""
    return id(a) == id(b)


@predicate(alias='unique?')
def is_unique(a, b) -> bool:
    """Tests whether two objects are unique based on memory location"""
    return id(a) != id(b)

# object ----------------------------------------
# https://docs.python.org/3/library/collections.abc.html#module-collections.abc


@predicate(alias='sequence?')
def is_sequence(s) -> bool:
    return isinstance(s, ABC.Sequence) #or issubclass(s, abc.Sequence)

# Basic types -----------------------------------


@predicate(alias='is-tuple?')
def is_tuple(sequence) -> bool:
    return isinstance(sequence, tuple)


@predicate(alias='is-list?')
def is_list(sequence) -> bool:
    return isinstance(sequence, list)


@predicate(alias='is-dict?')
def is_dict(d) -> bool:
    return isinstance(d, dict)


@predicate(alias=['is-str?', 'is-string?'])
def is_string(s) -> bool:
    return isinstance(s, str)

# numbers ---------------------------------------

# I'm not sure how redundant some of this is...


@predicate(alias=['int?', 'integer?', 'is-int?', 'ℤ?'])
def is_int(n) -> bool:
    '''Tests if a given value is an integer'''
    return isinstance(n, int) or isinstance(n, Integral)


@predicate(alias=['is-real?', 'is-float?', 'float?', 'real?', 'ℝ'])
def is_float(n) -> bool:
    return isinstance(n, numbers.Real) and isinstance(n, float)


@predicate(alias=['floating-int?', 'real-int?', 'real-or-int?'])
def is_float_or_int(n) -> bool:
    return float.is_integer(n)


@predicate(alias='number?')
def is_number(n) -> bool:
    '''Test whether a number is a sub-class of Number'''
    return isinstance(n, Number)


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
