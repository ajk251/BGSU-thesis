
from collections import defaultdict, namedtuple
from itertools import combinations_with_replacement, product
from numbers import Number
from typing import Union, Tuple
from operator import eq, ne



# -----------------------------------------------------------------------------
# This project comes from Software Testing: A craftsman's approach. It is the lock, 
# stock, and barrels problem. I assume the the calculation isn't trival for the 
# purposes of testing it, ie calculate(x,y,z) == test_caclulation(x,y,z) isn't
# feasible.

# the challenge with this is how to test it.

# -----------------------------------------------------------------------------
# right from the problem

def commision(nlocks: int, nstocks: int, nbarrels: int):

    inner = lambda xs,ys: sum(x*y for x,y in zip(xs,ys))

    assert nlocks <= 70,   'Exceeded lock sales inventory'
    assert nstocks <= 80,  'Exceeded stock sales inventory'
    assert nbarrels <= 90, 'Exceeded barrels sales inventory'

    assert nlocks >= 1,   'Must sell more than 1 lock'
    assert nstocks >= 1,  'Must sell more than 1 stock'
    assert nbarrels >= 1, 'Must sell more than 1 barrel'
    
    # the costs
    lock   = 45
    stock  = 30
    barrel = 25

    # sales = lock * nlocks + stocks * nstocks + nbarrels * barrel
    sales = inner([lock, stock, barrel], [nlocks, nstocks, nbarrels])

    if sales > 1800:
        commission = inner([.1, .15, .2], [1_000, 800, (sales-1_800)])
    elif sales > 1000:
        commission = inner([.1, .15], [1_000, (sales-1_000)])
    else:
        commission = 0.1 * sales

    return commission


# -----------------------------------------------------------------------------

def test(function, cases):

    pass

# =============================================================================

print(commision(1,1,1))
print(commision(70,80,90))