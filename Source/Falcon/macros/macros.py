
MACROS = {}


def macro(_fn=None, *, name=None):

    def func(fn):

        if isinstance(name, (str)):
            MACROS[name] = (fn, fn.__name__)

        # TODO: add error or something

        return fn

    return func if _fn is None else func(_fn)

