

from enum import Enum
from typing import Tuple

from Falcon.domains import domain
from Falcon.predicates.predicates import predicate, on_fail_false

Triangle = Enum('Triangle', 'equilateral, isosceles, scalene, not_triangle')


class TriangleError(Exception):
    pass


def classify(a: int, b: int, c: int) -> Triangle:

    assert isinstance(a_, int) and isinstance(b_, int) and isinstance(c_, int), "All values must be integers"

    if not ((a_ + b_ > c_) and (b_ + c_ > a_) and (c_ + a_ > b_)):
        return Triangle.not_triangle
    elif not ((a_ > 0) and (b_ > 0) and (c_ > 0)):
        return Triangle.not_triangle
    elif a == b and b == c:
        return Triangle.equilateral
    elif a != b and b != c and c != a:
        return Triangle.scalene
    elif a == b or b == c or a == c:
        return Triangle.isosceles

    raise TriangleError(f'Could not classify input a ￫ {a}, b ￫ {b}, c ￫ {c}')

# ---------------------------------------------------------

@predicate(alias=['not-triangle?'])
@on_fail_false
def not_triangle(a: int, b: int, c: int) -> bool:
    """Tests that three inputs do not form a valid triangle"""

    result =  isinstance(a, int) and isinstance(b, int) and isinstance(c, int)
    result &= (a > 0) and (b > 0) and (c > 0)
    result &= (a + b > c) and (b + c > a) and (c + a > b)

    return not result


@predicate(alias=['all-equal?'])
@on_fail_false
def all_equal(a: int, b: int, c: int) -> bool:
    return a == b == c


@predicate(alias=['two-equal?'])
@on_fail_false
def two_equal(a: int, b: int, c: int) -> bool:
    return a == b or b == c or a == c


@predicate(alias=['all-diff?', 'all-different?'])
@on_fail_false
def all_different(a: int, b: int, c: int) -> bool:
    return a != b and b != c and a != c

