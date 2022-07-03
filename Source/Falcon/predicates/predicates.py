
from collections import namedtuple
from enum import Enum
from functools import wraps
from typing import Union

PREDICATES = dict()

# use this instead!
Value = namedtuple('Value', 'name,symbol,is_symbolic,is_error,is_group,only_values')
# PredicateFn = namedtuple('PredicateFn', 'name,symbol,is_symbolic,is_error,is_group,only_values')

# help from: https://realpython.com/primer-on-python-decorators/
# TODO: check whether the name already exists
#       wrap the functions so they don't fail, just return False
#       add arg analysis to predicate, ie breakdown of args
#		if error, wrap and return ([Error|None], [True|False])

# TODO: change all the names & stuff to PredicateFn

NullString = Union[None, str]

# note: is_error implies calls should be expanded, ie fn(f, args)
#       is_group implies tests should be in the aggregate
#       only_values implies ... something ...


def predicate(_fn=None, *, alias=None, symbol: NullString = None, is_error: bool = False, is_group: bool = False, only_values=False):
    """Function decorator to define predicates for Falcon."""

    def function(func):

        is_symbolic = True if symbol is not None else False

        # don't really need the function itself...
        # values = (func.__name__, symbol, is_error, is_group)
        values = Value(func.__name__, symbol, is_symbolic, is_error, is_group, only_values)
        # predicate = PredicateFn(func.__name__, symbol, is_symbolic, is_error, is_group, only_values)
        if isinstance(alias, (list, tuple)):
            for name in alias:
                PREDICATES[name] = values
        elif alias:
            PREDICATES[alias] = values

        PREDICATES[func.__name__] = values

        return func
    
    return function if _fn is None else function(_fn)

# -----------------------------------------------
# better name? no_fail, pure, bool_pure, ???


def on_fail_false(fn) -> bool:
    """Decorator to wrap a predicate, ensure that it *only* returns a Boolean, even in the case of failure."""

    @wraps(fn)
    def call_fn(*args, **kwargs):
        """Decorates a predicate. If the predicate fails, it returns False"""

        try:
            result = fn(*args, **kwargs)
        except Exception as error:
            result = False

        return result

    return call_fn


# -----------------------------------------------
# for future use. Rather than a predicate returning a boolean, it returns a tribool/trit

# Disposition = Enum('Disposition', 'true,false,failure')


# def disposition(fn) -> Disposition:
#     """Decorator to wrap a predicate, ensure that it *only* returns true, false, or failure."""
#
#     @wraps(fn)
#     def call_fn(*args, **kwargs):
#         """Decorates a predicate. If the predicate fails, it returns False"""
#
#         try:
#             outcome = fn(*args, **kwargs)
#             result = Disposition.true if outcome else Disposition.false
#         except:
#             result = Disposition.failure
#
#         return result
#     return call_fn
