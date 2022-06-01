
from math import dist
from random import random
from domains.domains import domain, DomainBase

from random import uniform


# TODO: Depreciate - ART is better

@domain(alias=['Art'])
class ARTR2(DomainBase):

    def __init__(self, x: float = 0.0, y: float = 0.0, max_values: int = 1000, min_distance: float = 10.0,
                 lb: float = -1000.0, ub: float = 1000.0, max_candidates: int = 100):

        self.current = (x, y)
        self.last = None
        self.limits = (lb, ub)

        self.max_candidates = max_candidates        # the max number to produce each round
        self.max_values = max_values                # the max number to generate
        self.min_distance = min_distance            # the minimum separation between candidates

        self.args = {'show-dist': False}

    def __iter__(self):

        self.last = self.current
        temp = self.current

        i = 0

        while i <= self.max_values:

            for _ in range(self.max_candidates):

                temp = tuple((uniform(self.limits[0], self.limits[1]), uniform(self.limits[0], self.limits[1])))

                if dist(temp, self.last)  > self.min_distance:
                    if self.args['show-dist']:
                        print('Distance: ', dist(temp, self.last))
                    break

            yield temp

            i += 1

    def __call__(self, show_distance=False):

        # test_case & passed

        print('ha!')

        self.args['show-dist'] = show_distance



