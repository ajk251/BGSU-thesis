

from abc import ABC
from enum import Enum
from random import random, randint


DomainTypes = Enum('DomainTypes', 'uint32, uint64, int32, int64, float32, float64, discrete')

# =========================================================

class Domain(ABC):

    # def __instancecheck__(cls: ABCMeta, instance: Any) -> Any:
    #     return super().__instancecheck__(instance)

    def __repr__(self):
        return ''

    def __call__(self):
        pass

    def __iter__(self):
        pass


# ---------------------------------------------------------

# TODO: get bounds!

class Naturals(Domain):

    # unsigned int
    # natural - 0 to _
    kind = DomainTypes.uint64

    def __init__(self, lb: int=0, ub: int=100) -> None:

        assert lb >= 0, 'Domain must be greater than 0'

        self._lb = int(lb)
        self._ub = int(ub)


    def __call__(self):
        return randint(self._lb, self._ub)

    def __iter__(self):
        # yield extreme values if in bounds
        yield from range(self._lb, self._ub)

    def extremes(self):
        pass

    def random(self, n=100):

        for _ in range(n):
            yield randint(self._lb, self._ub)

    def xrandom(self, n=100):
        # extreme values + random, n = xvalues - n_random
        pass


# ---------------------------------------------------------

class Reals(Domain):

    # floating-point number
    kind = DomainTypes.float64

    def __init__(self, lb: float, ub: float) -> None:
        
        self._lb = float(lb)
        self._ub = float(ub)

    def __call__(self):
        pass

    def __iter__(self):
        pass


# ---------------------------------------------------------

class Integer(Domain):

    kind = DomainTypes.int64

    def __init__(self, lb: int, ub: int ) -> None:
        
        self._lb = int(lb)
        self._ub = int(ub)

    def __call__(self):
        pass

    def __iter__(self):
        pass


for n in Naturals(0, 25):
    print(n)

for n in Naturals(0, 100).random(10):
    print(n)