
from typing import Tuple
from operator import mul

lock_cost   = 45            # prices
stock_cost  = 30
barrel_cost = 25

lock_max   = 70             # maximum number of units that can be sold / month
stock_max  = 80
barrel_max = 90

def commission(locks: int, stocks: int, barrels: int) -> float:

    assert locks is not None and 0 <= locks <= lock_max,     f"Number of locks must an integer greater or equal to 0 and less than {lock_max}"
    assert stocks is not None and 0 <= stocks <= stock_max,  f"Number of stocks must an integer greater or equal to 0 and less than {stock_max}"
    assert barrels is not None and 0 <= locks <= barrel_max, f"Number of barrels must an integer greater or equal to 0 and less than {barrel_max}"

    sales = (lock_cost * locks) + (stock_cost * stocks) + (barrel_cost * barrels)
    c = 0.10 * sales        # commission

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
    return sum(map(mul, x, y))


# predicates ------------------------------------

def valid_sales(l,s, b) -> bool:
    return all(map(lambda v: isinstance(v, int), (l,s,b))) and \
           0 <= l <= lock_max and \
           0 <= s <= stock_max and \
           0 <= b <= barrel_max


def low_sales(l, s, b) -> bool:
    sales = dot((l,s,b), (lock_cost, stock_cost, barrel_cost))
    return sales < 1_000


def medium_sales(l, s, b) -> bool:
    sales = dot((l,s,b), (lock_cost, stock_cost, barrel_cost))
    return sales <= 1_800


def high_sales(l, s, b) -> bool:
    sales = dot((l,s,b), (lock_cost, stock_cost, barrel_cost))
    return sales > 1_800
