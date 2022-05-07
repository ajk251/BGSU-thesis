
from collections import namedtuple
import collections
from itertools import product, repeat
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


def param_product(m, n, A, B):
    # return (m, i) & (n, j) for each
    return product([Param(m, i) for i in range(len(A))], [Param(n, j) for j in range(len(B))])

def covers(t, p) -> int:
    c = 0
    c += 1 if p[0] in t else 0
    c += 1 if p[1] in t else 0
    return c

def is_covered(t, p) -> bool:
    return p[0] in t and p[1] in t

def extend(t, v):
    return t + (v,)

def repeats(collection):

    while True:
        yield from collection

# -------------------------------------

def ipo(*Fs):

    T = list(product(Fs[0], Fs[1]))
    # Q = tuple(len(F) for F in Fs)

    AP = set()
    R  = set()                  # To Remove, eg can't modify AP while iterating
    
    for F in Fs[2:]:
        AP = AP.union(set(product(Fs[0], F)))
        AP = AP.union(set(product(Fs[1], F)))

    print(f'AP |{len(AP)}|:\n', AP, '\n')

    # Horizontal growth -----
    Tʹ = set() # list()
    j = 0                       # the index of the T tuples

    for F in Fs[2:]:
        for t,v in zip(T, repeats(F)):
            tʹ = extend(t, v)

            if covers(tʹ, t) >= 2:
                Tʹ.add(tʹ)
                R.add(t)
            
            j = (j+1) % len(F)

    AP = AP.difference(R)       # knock some out of the way
        
    # remove covered
    for t in Tʹ:
        for ap in AP:
            if is_covered(t, ap):
                # print(t)
                R.add(ap)

    AP = AP.difference(R)

    print('Tʹ:\n', Tʹ)
    # print('R:\n', R)
    # print('AP:\n', AP)
    print('Uncovered: ', AP)

    # Vertical Growth -------

    # how to know which F is missing???
    # way too hacky...
    
    # for u in AP:
    #     for v in Fs[1]:
    #         # print(v, u)
    #         tʹ = (u[0], v, u[1])
    #         print('tʹ: ', tʹ)
    #         if tʹ not in Tʹ:
    #             Tʹ.add(tʹ)
    #             break

    for u,v in zip(AP, repeats(Fs[1])):
        tʹ = (u[0], v, u[1])
        print('tʹ: ', tʹ)
        if tʹ not in Tʹ:
            Tʹ.add(tʹ)
            # break


    # print('Tʹ:\n', Tʹ)

    return Tʹ



# -----------------------------------------------

# c1 = ca(A, B, C)
# print('size: ', len(c1), '\n', c1)

# r1 = r_ca(12, (3,2,3), A, B, C)
# print('size: ', len(r1), '\n', r1)

# print(tuple(product(A,B)))

# Should produce:
# a1 b1 c1
# a1 b2 c2
# a2 b1 c3
# a2 b2 c1
# a3 b1 c2
# a3 b2 c3
# a1 b2 c3 
# a2 b1 c2 
# a3 b1 c1 .

print('-'*25)

test_ca = {('a1', 'b1', 'c1'),
           ('a1', 'b2', 'c2'),
           ('a2', 'b1', 'c3'),
           ('a2', 'b2', 'c1'),
           ('a3', 'b1', 'c2'),
           ('a3', 'b2', 'c3'),
           ('a1', 'b2', 'c3'), 
           ('a2', 'b1', 'c2'),
           ('a3', 'b1', 'c1')}

ca = ipo(A, B, C)

for a in ca:
    print(a, ' ', a in test_ca)

print(len(test_ca), len(ca))
print(test_ca == ca)

print('-'*25)