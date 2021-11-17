
import operator as op
from abc import ABC


from predicates.predicates import predicate

# basic -----------------------------------------


@predicate(alias=['in', 'in?', '∋', '∍'], symbolic='in')
def is_in(value, container) -> bool:
    return op.contains(container, value)


@predicate(alias=['!in', '¬in', '∌'], symbolic='not in')
def not_in(value, container) -> bool:
    return not op.contains(container, value)

# compare ---------------------------------------


@predicate(alias=['='], symbolic='==')
def eq(a, b) -> bool:
    return op.eq(a, b)


@predicate(alias=['!=', '¬=', '≠'], symbolic='!=')
def ne(a, b) -> bool:
    return op.ne(a, b)


@predicate(alias='<', symbolic='<')
def lt(a, b) -> bool:
    return op.lt(a, b)


@predicate(alias='>', symbolic='>')
def gt(a, b) -> bool:
    return op.gt(a, b)


@predicate(alias=['<=', '≤'], symbolic='<=')
def le(a, b) -> bool:
    return op.le(a, b)


@predicate(alias=['>=', '≥'], symbolic='>=')
def ge(a, b) -> bool:
    return op.ge(a, b)


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

