
from collections import namedtuple
from itertools import permutations, product, combinations, tee
import itertools
from math import factorial
from random import choice


A = ('a1', 'a2', 'a3')
B = ('b1', 'b2')
C = ('c1', 'c2', 'c3')

# ---------------------------

# transform into arg_pack, ie args/kwargs
# count permutations

def nCr(n, r):
    return int(factorial(n) / (factorial(r) * factorial(n - r)))

# ---------------------------

# need max - & raise warning if too close

def r_ca(N, v, *arrays):
    # based on: Two-stage algorithms for covering array construction, Algorithm 1
    # use a weight based system…

    # TODO: make iterable?

    assert len(arrays) == len(v), 'Length of arrays must match'

    cov = set()         # the covering array

    while len(cov) < N:

        a = tuple(choice(f) for f in arrays)
        cov.add(a)

    return cov


# ---------------------------

Param = namedtuple('Param', 'F, q')

# Should produce:
# a1 b1 c1
# a1 b2 c2
# a2 b1 c3
# a2 b2 c1
# a3 b1 c2
# a3 b2 c3
# a1 b2 c3 
# a2 b1 c2
# a3 b1 c1

def param_product(m, n, A, B):
    # return (m, i) & (n, j) for each
    return product([Param(m, i) for i in range(len(A))], [Param(n, j) for j in range(len(B))])

def ipo(*arrays):

    T = product(arrays[0], arrays[1])

    #  = set()         # covering array
    #horizontal growth
    # for p in arrays[1:]:

    
    pass



# -----------------------------------------------

# c1 = ca(A, B, C)
# print('size: ', len(c1), '\n', c1)

# r1 = r_ca(12, (3,2,3), A, B, C)
# print('size: ', len(r1), '\n', r1)

print(tuple(product(A,B)))

print('-'*25)