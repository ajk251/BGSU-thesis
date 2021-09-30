
from abc import abstractclassmethod
from functools import partial, wraps

from typing import Any


# Predicates:
#   unary  → just single args, is-zero? n
#   binary → take two values,  is-lt? 2 3
#   predicate-fn (hold state) → (is_instance? int)(4)

# see:
#   https://docs.python.org/3/library/typing

# note: from numbers import Number, Number
# https://stackoverflow.com/questions/60616802/how-to-type-hint-a-generic-numeric-type-in-python


class AbstractPredicate:

    def __init__(self, fn, *args):
        self._fn = partial(fn, *args) #wraps(fn)

    # @abstractclassmethod
    # def __call__(self, value) -> bool:
    #     raise NotImplementedError

    @abstractclassmethod
    def __and__(self, other):
        raise NotImplementedError

    @abstractclassmethod
    def __or__(self, other):
        raise NotImplementedError

    @abstractclassmethod
    def __xor__(self, other):
        raise NotImplementedError

 
# ---------------------------------------------------------

class UnaryPredicate(AbstractPredicate):

    def __call__(self, value: Any) -> bool:
        return self._fn(value)

    def __repr__(self):
        return f'<UnaryPredicate>' # {self._fn.__name__}>'


class BinaryPredicate(AbstractPredicate):

    def __call__(self, a: Any, b: Any) -> bool:
        return self._fn(a,b)


class Predicate(AbstractPredicate):

    def __call__(self, *args, **kwargs):
        return self._fn(*args, **kwargs)

# ---------------------------------------------------------


def is_instanceof(obj: Any, instance: Any):
    '''Is the instance an instance of the class obj'''
    return isinstance(obj, instance)

def is_mod_of(n, seq):
    return len(seq) % n == 0

import operator as op


is_instance = BinaryPredicate(is_instanceof)
is_lt = BinaryPredicate(op.lt)
is_length_gt_0 = BinaryPredicate(lambda seq: len(seq) > 0)
is_true = UnaryPredicate(lambda obj: bool(obj))

is_modof3 = UnaryPredicate(is_mod_of, 3)
is_integer = UnaryPredicate(isinstance, int)

print(is_instance)

# print(is_instance(int, 2))

print(is_integer(3))
print(is_integer(3.2))
print(is_modof3([1,2,3]))