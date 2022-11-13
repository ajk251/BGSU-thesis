from math import dist
from random import random

# ART as a Domain?

class ART_R2:

    def __init__(self, x: float= 0.0, y: float= 0.0, max_values = 1000, min_distance: float = 10.0,
                 lb=-1000.0, ub = 1000.0, max_candidates=100):

        self.current = (x, y)
        self.llimit = lb
        self.ulimit = ub

        self.max_candidates = max_candidates       # the max number to produce each round
        self.max_values = max_values               # the max number to generate
        self.min_distance = min_distance



    def __iter__(self):

        temp = self.current

        for _ in range(self.max_candidates):
            
            temp = tuple(random(self.llimit, self.ulimit), random(self.llimit, self.ulimit))

            if dist(temp) > self.min_distance:
                break
                
        yield temp


art2 = ART_R2(max_candidates=10)

for x,y in art2:
    print(x,y)