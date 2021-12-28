


from collections import namedtuple
from typing import Union

PREDICATES = dict()

# use this instead!
Value = namedtuple('Value', 'name,symbol,is_error')

#help from: https://realpython.com/primer-on-python-decorators/

# TODO: add complement option, ala toolz
#       add underscore to dash -ify option
#       check whether the name already exists
#       wrap the functions so they don't fail, just return False
#       add arg analysis to predicate, ie breakdown of args


NullString = Union[None, str]

def predicate(_fn=None, *, alias=None, symbol: NullString = None, is_error=False):

    def function(func):

        # don't really need the function itself...
        values = (func.__name__, symbol)#, is_error)

        if isinstance(alias, (list, tuple)):
            for name in alias:
                PREDICATES[name] = values
        elif alias:
            PREDICATES[alias] = values

        PREDICATES[func.__name__] = values
    
        return func
    
    return function if _fn is None else function(_fn)
