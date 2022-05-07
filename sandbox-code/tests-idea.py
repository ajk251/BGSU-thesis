

from collections import namedtuple
import functools
from typing import Union
import pytest


PREDICATES = dict()

# use this instead!
Value = namedtuple('Value', 'name,symbol,is_error')

#help from: https://realpython.com/primer-on-python-decorators/

# TODO: check whether the name already exists
#       wrap the functions so they don't fail, just return False
#       add arg analysis to predicate, ie breakdown of args
#		if error, wrap and return ([Error|None], [True|False])


NullString = Union[None, str]

def predicate(_fn=None, *, alias=None, symbol: NullString = None, is_error=False):

    def function(func):

        # don't really need the function itself...
        values = (func.__name__, symbol, is_error)

        if isinstance(alias, (list, tuple)):
            for name in alias:
                PREDICATES[name] = values
        elif alias:
            PREDICATES[alias] = values

        PREDICATES[func.__name__] = values
    
        return func

    print('called predicate')
    
    return function if _fn is None else function(_fn)

def debug(func):
    """Print the function signature and return value"""
    @functools.wraps(func)
    def wrapper_debug(*args, **kwargs):
        args_repr = [repr(a) for a in args]                      # 1
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]  # 2
        signature = ", ".join(args_repr + kwargs_repr)           # 3
        print(f"Calling {func.__name__}({signature})")

        try:
            print('calling...')
            value = func(*args, **kwargs)
        except Exception as e:
            value = e 
        # finally:
        #     if error is AssertionError:
        #         return True
        #     return False

        # print(f"{func.__name__!r} returned {value!r}")           # 4
        return value
    return wrapper_debug



# is_error          ￫ is it an error or list of errors
# is_error_type     ￫ is


@predicate(alias='even')
def even(n):
    return n % 2 == 0


@predicate(alias='assertion?', is_error=True)
def catch_assertion(error):
    return isinstance(error, AssertionError)



def call(fn, *args, **kwargs):

    try:
        value = fn(*args, **kwargs)
    except Exception as error:
        value = error

    # print('returning ', value, type(value))
    
    return value


# ------------------------------------------------------------

def add(x,y):
    assert x > 1, "x must be greater than 1"
    assert y > 1, "y must be greater than 1"
    return x + y


# catch_assertion( debug(add(1, 1)))


# X = range(2, 10)
# Y = range(2, 10)

# for x,y in zip(X,Y):
    
    
#     assert add(x,y) > 2
#     assert even(add(x,y))

#     print(add(x,y))

print('in predicates: ', PREDICATES.items())

assert catch_assertion(call(add, 1, 1))