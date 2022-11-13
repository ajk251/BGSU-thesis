
from itertools import permutations
from typing import Dict, Generator, List, Tuple
from operator import mul
from random import randrange
import warnings

import matplotlib.pyplot as plt
import pytest

from Falcon.domains import domain
from Falcon.predicates import predicate

# constants -------------------------------------

lock_cost   = 45            # prices
stock_cost  = 30
barrel_cost = 25

lock_max   = 70             # maximum number of units that can be sold / month
stock_max  = 80
barrel_max = 90

# -----------------------------------------------


def commission(locks: int, stocks: int, barrels: int) -> float:

    # it actually found an error!

    assert locks is not None and 1 <= locks <= lock_max,     f"Number of locks must an integer greater or equal to 1 and less than {lock_max}"
    assert stocks is not None and 1 <= stocks <= stock_max,  f"Number of stocks must an integer greater or equal to 1 and less than {stock_max}"
    assert barrels is not None and 1 <= barrels <= barrel_max, f"Number of barrels must an integer greater or equal to 1 and less than {barrel_max}"

    # if locks <= 0 or stocks <= 0 or barrels <= 0:
    #     return 0.0

    # sales = (lock_cost * locks) + (stock_cost * stocks) + (barrel_cost * barrels)
    sales = dot((lock_cost, stock_cost, barrel_cost), (locks, stocks, barrels))
    c = 0.10 * sales        # base commission

    # low    = 0.10           # percentages
    # medium = 0.15
    # high   = 0.20

    if sales > 1_800.0:
        c = (0.10 * 1_000) + (0.15 * 800.0) + (0.20 * (sales - 1_800.0))
    elif sales > 1000.0:
        c = (0.10 * 1_000) + (0.15 * (sales - 1_000.0))

    return c


# --------------------------------------------
# helper function

def dot(x: Tuple[int, int, int], y: Tuple[float, float, float]) -> float:
    """Computes the dot product between 2 tuples."""
    return sum(map(mul, x, y))


# domains --------------------------------------

@domain(alias='Sales')
def sales_values(n=100, low_values: int = 5) -> Generator[Tuple[int, int, int], None, None]:

    # this ensures "low" is tested
    for _ in range(low_values):
        yield (randrange(1, 10), randrange(1, 10), randrange(1, 10))

    # -10 gives some chance of -1 or 0
    for _ in range(n-low_values):
        yield (randrange(-10, lock_max+10), randrange(-10, stock_max+10), randrange(-10, barrel_max+10))


@domain(alias=['SalesProgression'])
def linear_sales():

    for l,s,b in permutations([-1, 0, 1, 2, 3], r=3):
        yield (l, s, b)

    for s in range(3, 10):
        yield (s, s, s)

    for s in range(10, 95, 5):
        yield (s, s, s)


# predicates ------------------------------------
# the partition predicate --------

@predicate(alias=['valid-sales?'])
def valid_sales(l: int, s: int, b: int) -> bool:
    return not (all(map(lambda v: isinstance(v, int), (l,s,b))) and \
           1 <= l <= lock_max and \
           1 <= s <= stock_max and \
           1 <= b <= barrel_max)


@predicate(alias='too-low?')
def too_low(l: int, s: int, b: int) -> bool:
    return l <= 0 or s <= 0 or b <= 0


@predicate(alias='too-high?')
def too_high(l: int, s: int, b: int) -> bool:
    return l > lock_max or s > stock_max or b > barrel_max


@predicate(alias=['low-sales?'])
def low_sales(l: int, s: int, b: int) -> bool:
    sales = dot((l,s,b), (lock_cost, stock_cost, barrel_cost))
    return sales < 1_000


@predicate(alias=['medium-sales?'])
def medium_sales(l: int, s: int, b: int) -> bool:
    sales = dot((l,s,b), (lock_cost, stock_cost, barrel_cost))
    return sales <= 1_800


@predicate(alias='high-sales?')
def high_sales(l: int, s: int, b: int) -> bool:
    sales = dot((l,s,b), (lock_cost, stock_cost, barrel_cost))
    return sales > 1_800


# test predicates ----------------

# use assertion error for invalid sales

@predicate(alias=['low-commission+examples?'], is_group=True)
def low_commission_group(commissions: List[float], at_least: int = 10) -> bool:
    return all((map(lambda c: ((c / 0.1) - 5.0) <= 1_000 or ((c / 0.1) + 5.0) <= 1_000, commissions))) and \
           len(commissions) >= at_least
    

@predicate(alias=['low-commission?'])
def low_commission(c: float) -> bool:
    s =  (c / 0.1)                                      # estimated sales
    return ((c / 0.1) - 5.0) <= 1_000 or ((c / 0.1) + 5.0) <= 1_000     # estimating with floats…


@predicate(alias=['medium-commission?'])
def medium_commission(c: float) -> bool:
    s =  (c / 0.15) + 334.0                             # estimated sales
    return (s - 5.0) <= 1_800 or (s + 5.0) <= 1_800     # estimating with floats…


@predicate(alias=['high-commission?'])
def high_commission(c: float) -> bool:
    s =  (c / 0.2) + 700.0                              # estimated sales
    return (s - 5.0) >= 1_800 or (s + 5.0) >= 1_800     # estimating with floats…

# -----------------------------------------------

# plot total-sales vs commission
# plot l,s,b and commission as bubble in 3d

# commissions : Dict[str, List[Tuple[int, int, int]]]

def plot_commission(cases, results, name=None):

    colors = 'ygk'
    groups = ('low', 'medium', 'high')
    fig, ax = plt.subplots(1, 1, figsize=(12, 12))

    for group, color in zip(groups, colors):

        sales = tuple(map(lambda t: dot((t[0],t[1],t[2]), (lock_cost, stock_cost, barrel_cost)), cases[group]))
        ax.scatter(sales, results[group], color=color)

    ax.set_xlabel('Total Sales')
    ax.set_ylabel('Commission')
    ax.set_title('Total sales vs Commission')
    ax.legend(['low', 'medium', 'high'])


    fig.savefig('/media/aaron/Shared2/School/BGSU-thesis/Source/Examples/commission_problem/commission-plot.png', format='png')

    # 3d plot ------------------------------

    fig = plt.figure()
    ax  = fig.add_subplot(projection='3d')

    i = 0

    for x,y,z in cases['low']:
        ax.scatter(x, y, z, color='y', s=results['low'][i] / 10)
        i += 1
    
    i = 0
    
    for x,y,z in cases['medium']:
        ax.scatter(x, y, z, color='g', s=results['medium'][i] / 10)

    i = 0

    for x,y,z in cases['high']:
        ax.scatter(x, y, z, color='b', s=results['high'][i] / 10)
        i += 1

    ax.set_xlabel('Locks')
    ax.set_ylabel('Stocks')
    ax.set_zlabel('Barrels')
    ax.set_title('Locks, Stocks, Barrels and Commission')

    fig.savefig('/media/aaron/Shared2/School/BGSU-thesis/Source/Examples/commission_problem/commission-plot-3d.png', format='png')


# # low
# print(commission(10, 10, 10), dot((10, 10, 10), (lock_cost, stock_cost, barrel_cost)))
# print(low_commission(100.0))

# # medium
# print(commission(12, 12, 12), dot((12, 12, 12), (lock_cost, stock_cost, barrel_cost)))
# print(medium_commission(130.0))

# # high
# print(commission(50, 50, 50), dot((50, 50, 50), (lock_cost, stock_cost, barrel_cost)))
# print(high_commission(860.0))
