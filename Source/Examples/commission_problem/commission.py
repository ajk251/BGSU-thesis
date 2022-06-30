
from typing import Dict, Generator, List, Tuple
from operator import mul
from random import randrange

import matplotlib.pyplot as plt

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

    assert locks is not None and 0 <= locks <= lock_max,     f"Number of locks must an integer greater or equal to 0 and less than {lock_max}"
    assert stocks is not None and 0 <= stocks <= stock_max,  f"Number of stocks must an integer greater or equal to 0 and less than {stock_max}"
    assert barrels is not None and 0 <= locks <= barrel_max, f"Number of barrels must an integer greater or equal to 0 and less than {barrel_max}"

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
def sales_values(n=100, test_outside: bool = False) -> Generator[Tuple[int, int, int], None, None]:

    if test_outside:
        yield (-1, -1, -1)
        yield (0, 0, 0)

        for _ in range(n - 2):
            yield (randrange(-10, lock_max + 10), randrange(-10, stock_max + 10), randrange(-10, barrel_max + 10))

    else:
        for i in range(n):
            yield (randrange(1, lock_max), randrange(1, stock_max), randrange(1, barrel_max))


# predicates ------------------------------------
# the partition predicate --------

@predicate(alias=['valid-sales?'])
def valid_sales(l: int, s: int, b: int) -> bool:
    return not (all(map(lambda v: isinstance(v, int), (l,s,b))) and \
           0 <= l <= lock_max and \
           0 <= s <= stock_max and \
           0 <= b <= barrel_max)


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

@predicate(alias=['low-commission?'], is_group=True)
def low_commission(c: float) -> bool:
    pass


@predicate(alias=['medium-commission?'], is_group=True)
def medium_commission() -> bool:
    pass


@predicate(alias=['high-commission?'], is_group=True)
def high_commission() -> bool:
    pass


# -----------------------------------------------

# plot total-sales vs commission
# plot l,s,b and commission as bubble in 3d

# commissions : Dict[str, List[Tuple[int, int, int]]]

def plot_commission(l: int, s: int, b: int):

    fig, ax = plt.subplots(1, 1, figsize=(12, 12))




    # fig.save('commission-plot.jpg')



# for l,s,b in sales_values(10, False):
#     c =  dot((lock_cost, stock_cost, barrel_cost), (l, s, b))
#     print(l, s, b, c, commission(l, s, b))

# print('-'*20)

# for l,s,b in sales_values(10, True):
#     print(l, s, b)
