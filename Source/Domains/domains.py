


DOMAINS = {}


def domain(_fn=None, *, alias=None):

    def func(fn):

        if isinstance(alias, (tuple, list)):
            for name in alias:
                DOMAINS[name] = fn.__name__
        elif alias:
            DOMAINS[alias] = fn.__name__

        DOMAINS[fn.__name__] = fn.__name__

        return fn

    return func if _fn is None else func(_fn)
