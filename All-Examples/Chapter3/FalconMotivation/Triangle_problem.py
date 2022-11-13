

from enum import Enum
from typing import Tuple

from Falcon.domains import domain
from Falcon.predicates.predicates import predicate, on_fail_false

Triangle = Enum('Triangle', 'equilateral, isosceles, scalene, not_triangle')


class TriangleError(Exception):
    pass

def classify(a: int, b: int, c: int) -> Triangle:

    assert isinstance(a, int) and isinstance(b, int) and isinstance(c, int), "All values must be integers"

    if not ((a + b > c) and (b + c > a) and (c + a > b)):
        return Triangle.not_triangle
    elif not ((a > 0) and (b > 0) and (c > 0)):
        return Triangle.not_triangle
    elif a == b and b == c:
        return Triangle.equilateral
    elif a != b and b != c and c != a:
        return Triangle.scalene
    elif a == b or b == c or a == c:
        return Triangle.isosceles

    raise TriangleError(f'Could not classify input a ￫ {a}, b ￫ {b}, c ￫ {c}')

# def classify(a: int, b: int, c: int) -> Triangle:

#     is_valid    = lambda a_,b_,c_: (a_ > 0) and (b_ > 0) and (c_ > 0)
#     is_triangle = lambda a_,b_,c_: (a_ + b_ > c_) and (b_ + c_ > a_) and (c_ + a_ > b_)
#     integers    = lambda a_,b_,c_: isinstance(a_, int) and isinstance(b_, int) and isinstance(c_, int)

#     assert integers(a, b, c), "All values must be integers"

#     if (not is_triangle(a, b, c)):
#         return Triangle.not_triangle
#     elif not is_valid(a, b, c):
#         return Triangle.not_triangle
#     elif a == b and b == c:
#         return Triangle.equilateral
#     elif a != b and b != c and c != a:
#         return Triangle.scalene
#     elif a == b or b == c or a == c:
#         return Triangle.isosceles

#     raise TriangleError(f'Could not classify input a ￫ {a}, b ￫ {b}, c ￫ {c}')

# ---------------------------------------------------------

# @predicate(alias=['no-triangle-theorem?', 'not-satisfy-triangle-theorem?'])
# @on_fail_false
# def not_satisfy_triangle_theorem(a: int, b: int, c: int) -> bool:
#     """The Triangle Theorem, ie. sᵢ < s₂+s₃, for all sides"""
#     # return not ((a < b+c) and (b < a+c) and (c < a+b))            # This is wrong!
#     return (a >= b + c) and (b >= a + c) and (c >= a + b)


# these ---------------------------------------------------

@predicate(alias=['not-triangle?'])
@on_fail_false
def not_triangle(a: int, b: int, c: int) -> bool:
    """Tests that three inputs do not form a valid triangle"""
    # result =  not any(map(lambda n: (isinstance(n, int)) or (n > 0), (a, b, c)))

    result =  isinstance(a, int) and isinstance(b, int) and isinstance(c, int)
    result &= (a > 0) and (b > 0) and (c > 0)
    result &= (a + b > c) and (b + c > a) and (c + a > b)
    # result |= not ((a < b+c) and (b < a+c) and (c < a+b))
    # result |= max(a,b,c) < (a + b + c - max(a,b,c))

    return not result


@predicate(alias=['all-equal?'])
@on_fail_false
def all_equal(a: int, b: int, c: int) -> bool:
    return a == b and b == c


@predicate(alias=['two-equal?'])
@on_fail_false
def two_equal(a: int, b: int, c: int) -> bool:
    return a == b or b == c or a == c


@predicate(alias=['all-diff?', 'all-different?'])
@on_fail_false
def all_different(a: int, b: int, c: int) -> bool:
    return a != b and b != c and a != c


# Test the groups -------------------------------
# by is the right type for that partition? ------

# @predicate(alias=['is-not-triangle?'])
# @on_fail_false
# def is_not_triangle(value):
#     return value == Triangle.not_triangle


# @predicate(alias=['is-equilateral?'])
# @on_fail_false
# def is_equilateral(value):
#     return value == Triangle.equilateral


# @predicate(alias=['is-scalene?'])
# @on_fail_false
# def is_scalene(value):
#     return value == Triangle.scalene


# @predicate(alias=['is-isosceles?'])
# @on_fail_false
# def is_isosceles(value):
#     return value == Triangle.isosceles


# Domain --------------------------------------------------

# @domain(alias=['TriangleValues'])
# def critical_values() -> Tuple[int, ...]:
#     return (-1, 0, 1, 2, 3, 4, 5)
