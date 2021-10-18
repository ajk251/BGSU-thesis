
from functools import partial, wraps

predicates = dict()

#help from: https://realpython.com/primer-on-python-decorators/


# TODO: add complement option
#       add underscore to dash -ify option
#       check whether the name already exists
#       wrap the functions so they don't fail, just return False

def register(fn):
    predicates[fn.__name__] = fn
    return fn

# use the toolz complement!
def complement(fn):
    def invert(*args, **kwargs):
        return not partial(fn, *args, **kwargs)
    return invert

def predicate(_fn=None, *, alias=None, complement=False):

    def function(func):

        if isinstance(alias, (list, tuple)):
            for name in alias:
                predicates[name] = func
        elif alias:
            predicates[alias] = func

        predicates[func.__name__] = func

        # use toolz to do this...
        if complement:
            predicates['!' + func.__name__] = func
    
        return func
    
    return function if _fn is None else function(_fn)

