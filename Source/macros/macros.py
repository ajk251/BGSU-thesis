
MACROS = {}


def macro(_fn=None, *, alias=None):

    def func(fn):

        if isinstance(alias, (tuple, list)):
            for name in alias:
                MACROS[name] = fn.__name__
        elif alias:
            MACROS[alias] = fn.__name__

        MACROS[fn.__name__] = fn.__name__

        return fn

    return func if _fn is None else func(_fn)

