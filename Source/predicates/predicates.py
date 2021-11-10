
import operator as op
from abc import ABC
from typing import Union

PREDICATES = dict()

#help from: https://realpython.com/primer-on-python-decorators/

# TODO: add complement option, ala toolz
#       add underscore to dash -ify option
#       check whether the name already exists
#       wrap the functions so they don't fail, just return False
#       add arg analysis to predicate, ie breakdown of args

# def register(fn):
#     PREDICATES[fn.__name__] = fn
#     return fn

NullString = Union[None, str]


def predicate(_fn=None, *, alias=None, symbolic: NullString = None):

    def function(func):

        if isinstance(alias, (list, tuple)):
            for name in alias:
                PREDICATES[name] = func
        elif alias:
            PREDICATES[alias] = func

        PREDICATES[func.__name__] = (func, symbolic)
    
        return func
    
    return function if _fn is None else function(_fn)


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



print("BOOM")
