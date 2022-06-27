
from Falcon.domains.domains import domain, DomainBase

from math import dist
from random import uniform


@domain(alias=['ART', 'Art', 'ARTDomain'])
class ART(DomainBase):

    def __init__(self, n_dims: int = 2, num_values: int = 100, min_distance: float = 10.0,
                 lb: float = -1000.0, ub: float = 1000.0, max_candidates: int = 100):

        self.n_dims = n_dims
        self.current = tuple(0.0 for _ in range(self.n_dims))
        self.last = None
        self.limits = (lb, ub)

        self.max_candidates = max_candidates        # the max number to produce each round
        self.max_values = num_values                # the max number to generate
        self.min_distance = min_distance            # the minimum separation between candidates

    def __iter__(self):

        self.last = self.current
        temp = self.current
        r = lambda : uniform(self.limits[0], self.limits[1])

        i = 0

        while i <= self.max_values:

            # generate candidate values, upto the max
            for _ in range(self.max_candidates):

                temp = tuple((r() for _ in range(self.n_dims)))

                # found it, yield it
                if dist(temp, self.last) > self.min_distance:
                    break

            yield temp

            i += 1
