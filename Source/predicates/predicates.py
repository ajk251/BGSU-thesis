
from collections import namedtuple
from functools import wraps
from typing import Union

PREDICATES = dict()

# use this instead!
Value = namedtuple('Value', 'name,symbol,is_error')

#help from: https://realpython.com/primer-on-python-decorators/

# TODO: check whether the name already exists
#       wrap the functions so they don't fail, just return False
#       add arg analysis to predicate, ie breakdown of args
#		if error, wrap and return ([Error|None], [True|False])


NullString = Union[None, str]

# note: is_error implies calls should be expanded, ie fn(f, args)
#       is_group implies tests should be in the aggregate

def predicate(_fn=None, *, alias=None, symbol: NullString = None, is_error: bool = False, is_group: bool = False):
    """Function decorator to define predicates for Falcon."""

    def function(func):

        # don't really need the function itself...
        values = (func.__name__, symbol, is_error, is_group)

        if isinstance(alias, (list, tuple)):
            for name in alias:
                PREDICATES[name] = values
        elif alias:
            PREDICATES[alias] = values

        PREDICATES[func.__name__] = values
    
        return func
    
    return function if _fn is None else function(_fn)


def onfail_false(fn) -> bool:
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
