

from itertools import product


ALGORITHMS = {}


def algorithm(_fn=None, *, alias=None):

    def function(func):

        # don't really need the function itself...
        values = func.__name__

        if isinstance(alias, (list, tuple)):
            for name in alias:
                ALGORITHMS[name] = values
        elif alias:
            ALGORITHMS[alias] = values

        ALGORITHMS[func.__name__] = values

        return func

    return function if _fn is None else function(_fn)


# ---------------------------------------------------------

@algorithm(alias=['⨯', 'X', 'product', 'cartesian'])
def cartesian_product(*args):
    return product(*args)

