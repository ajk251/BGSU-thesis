
from abc import ABC
from typing import Any, Dict, Tuple

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

# ---------------------------------------------------------
# An abstract base class for class-based domains

class DomainBase(ABC):

    def __iter__(self):
        raise NotImplementedError('__iter__ must be implemented')

    def __call__(self, test_case: Tuple[Any, ...], **kwargs: Dict[Any, Any]):
        raise NotImplementedError('__call__ must be implemented')
