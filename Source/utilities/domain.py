
import random

# from math import inf
from random import randint, uniform, normalvariate
# from typing import Union
# from sys import float_info


import more_itertools as mi


# tranche
# discrete

# Numeric → mi.numeric_range
#   → for things that are number like, eg DateTime - have an add method


class DomainBase():
    
    def __init__(self, seed=None):

        random.seed(seed)

class NumericDomainBase(DomainBase):

    def __init__(self, lower_bound, upper_bound, step, seed=None):

        super().__init__(seed)

        self.lb = lower_bound
        self.ub = upper_bound
        self.step = step

# -----------------------------------------------
    
class Naturals(NumericDomainBase):

    def __init__(self, lower_bound, upper_bound, step=1, seed=None):
        super().__init__(lower_bound, upper_bound, step, seed=seed)

    def __iter__(self):

        n :int = self.lb

        while True:
            yield n
            n += self.step

            if n >= self.ub: break
        

class RandomNaturals(NumericDomainBase):

    def __init__(self, lower_bound, upper_bound, step=None, N=100, seed=None):
        super().__init__(lower_bound, upper_bound, step, seed=seed)
        self.N = N

    def __iter__(self):
        yield from (randint(self.lb, self.ub) for _ in range(self.N))

# -----------------------------------------------

class Reals(NumericDomainBase):

    def __init__(self, lower_bound, upper_bound, step=1.0, seed=None):
        super().__init__(lower_bound, upper_bound, step, seed=seed)

    def __iter__(self):

        n: float = self.lb
        i: int = 0

        while True:
            
            n = self.lb + (i * self.step)
            yield n

            if n >= self.ub: break
            i += 1


class RandomReals(NumericDomainBase):

    def __init__(self, lower_bound, upper_bound, step=None, N=100, seed=None):
        super().__init__(lower_bound, upper_bound, step, seed=seed)
        self.N : int = N

    def __iter__(self):
        yield from (uniform(self.lb, self.ub) for _ in range(self.N))

# ---------------------------------

# TODO: make the builder just a generator...somehow it is getting clobbered and has to be defined 

class Tranche(DomainBase):

    def __init__(self, tranches, seed=None):
                                  
        super().__init__(seed)
        self.tranches = tranches

    def __iter__(self):

        for tranche in self.tranches:
            yield from tranche


    @classmethod
    def make_from_bounds(cls, bounds, sizes, builder=uniform, seed=None):


        random.seed(seed)
        tranches = []

        for b,n in zip(bounds, sizes):
            l,u = b
            tranches.append(tuple(builder(l,u) for _ in range(n)))

        return Tranche(tranches, seed=seed)

    @classmethod
    def make_from_intervals(cls, intervals, sizes, builder=uniform, seed=None):

        assert len(intervals) - 1 == len(sizes) , "'sizes' must be 1 smaller than 'intervals'"
        
        random.seed(seed)
        tranches = []
        
        for p,n in zip(mi.pairwise(intervals), sizes):
            l,u = p
            tranches.append(tuple(builder(l,u) for _ in range(n)))

        return Tranche(tranches, seed)


    @classmethod
    def make_from_distributions(cls, dists, values, sizes, seed=None):
        # dist(value) for _ in size

        assert len(dists) == len(values) == len(sizes), '"dists, values, & sizes" must be the same size'

        random.seed(seed)
        tranches = []
        
        for dist, value, n in zip(dists, values, sizes):
            tranches.append(tuple(dist(*value) for _ in range(n)))

        return Tranche(tranches, seed=None)


# =========================================================


I = Naturals(0, 100, 5)
R = RandomNaturals(0, 100, N=10)

for i in I:
    print(i)

print('-'* 25)

for i in R:
    print(i)

print('-'* 25)

R = Reals(0., 25., 1.5)
rR = RandomReals(0., 25., N=10)

for r in R:
    print(r)

print('-'* 25)

for r in rR:
    print(r)


print('-'* 25)

T = Tranche([[0,1,2], ['a', 'b', 'c']])

for t in T:
    print(t)

print('-'* 25)

T1 = Tranche.make_from_intervals([0, 10, 100, 1000], [3,3,3])

for t in T1:
    print(t)

print('-'* 25)

T2 = Tranche.make_from_bounds([(0, 10), (10, 100), (100, 1000)], [3,3,3])

for t in T2:
    print(t)

print('-'* 25)

T3 = Tranche.make_from_distributions([uniform, normalvariate, normalvariate], [(-5, 0), (0, 1), (100, 10)], [5, 5, 10])

for t in T3:
    print(t)