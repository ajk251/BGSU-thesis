
from math import dist
from random import random, uniform

from abc import ABC


class DomainBase(ABC):

    def __iter__(self):
        raise NotImplementedError('__iter__ must be implemented')

    def __call__(self):
        raise NotImplementedError('__call__ must be implemented')


# ART as a Domain?

class ART_R2(DomainBase):

    def __init__(self, x: float= 0.0, y: float= 0.0, max_values = 1000, min_distance: float = 10.0,
                 lb=-1000.0, ub = 1000.0, max_candidates=100):

        self.current = (x, y)
        self.last = None
        self.limits = (lb, ub)

        self.max_candidates = max_candidates       # the max number to produce each round
        self.max_values = max_values               # the max number to generate
        self.min_distance = min_distance

        self.args = {'show-dist': False}

    def __iter__(self):

        self.last = self.current
        temp = self.current

        i = 0

        while i <= self.max_values:

            for _ in range(self.max_candidates):

                temp = tuple((uniform(self.limits[0], self.limits[1]), uniform(self.limits[0], self.limits[1])))

                if dist(temp, self.last)  > self.min_distance:
                    # if self.args['show-dist']:
                    #     print('Distance: ', dist(temp, self.last))
                    break

            yield temp

            i += 1

    def __call__(self):

        print('ha!')

        # self.args['show-dist'] = show_distance



art2 = ART_R2(max_values=10)

for x,y in art2:

    print(x,y)

    if random() <= 0.5:
        # art2(show_distance=True if random() <= 0.5 else False)
        art2()
