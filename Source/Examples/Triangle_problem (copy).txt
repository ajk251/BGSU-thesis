

from enum import Enum
from typing import Tuple

from domains.domains import domain
from predicates.predicates import predicate, onfail_false

Triangle = Enum('Triangle', 'equilateral, isosceles, scalene, not_triangle')


class TriangleError(Exception):
    pass


def classify(a: int, b: int, c: int) -> Triangle:

    is_triangle = lambda a_,b_,c_: (a < b+c) and (b < a+c) and (c < a+b)
    integers    = lambda a_,b_,c_: isinstance(a_, int) and isinstance(b_, int) and isinstance(c_, int)
    is_valid    = lambda a_,b_,c_: (a_ > 0) and (b_ > 0) and (c_ > 0)

    assert integers(a, b, c), "All values must be integers"

    if not is_triangle(a, b, c): # and not is_valid(a, b, c):
        # print('sides too short ', end='')
        return Triangle.not_triangle
    elif not is_valid(a, b, c):
        # print('not a valid triangle ', end='')
        return Triangle.not_triangle
    elif a == b and b == c:
        return Triangle.equilateral
    elif a != b and b != c and c != a:
        return Triangle.scalene
    elif a == b or b == c or a == c:
        return Triangle.isosceles

    raise TriangleError(f'Could not classify input a ￫ {a}, b ￫ {b}, c ￫ {c}')


# ---------------------------------------------------------


@predicate(alias=['!ints+?', '!positive-integers?', 'not-positive-ints?', 'positive-ints?'])
@onfail_false
def not_positive_integers(a: int, b: int, c: int) -> bool:
    """Tests that all values are positive integers"""
    return any(map(lambda n: (not isinstance(n, int)) or (not n > 0), (a, b, c)))

    # if (not isinstance(a, int)) or (not a >= 1):
    #     return False
    # elif (not isinstance(b, int)) or (not b >= 1):
    #     return False
    # elif (not isinstance(c, int)) or (not c >= 1):
    #     return False
    #
    # return True


@predicate(alias=['no-triangle-theorem?', 'not-satisfy-triangle-theorem?'])
@onfail_false
def not_satisfy_triangle_theorem(a: int, b: int, c: int) -> bool:
    """The Triangle Theorem, ie. sᵢ < s₂+s₃, for all sides"""
    return not ((a < b+c) and (b < a+c) and (c < a+b))


# these ---------------------------------------------------

@predicate(alias=['not-triangle?'])
@onfail_false
def not_triangle(a: int, b: int, c: int) -> bool:
    """Tests that three inputs do not form a valid triangle"""
    result =  any(map(lambda n: (not isinstance(n, int)) or (not n > 0), (a, b, c)))
    result &= not ((a < b+c) and (b < a+c) and (c < a+b))

    return result


@predicate(alias=['all-equal?'])
@onfail_false
def all_equal(a: int, b: int, c: int) -> bool:
    return a == b and b == c


@predicate(alias=['two-equal?'])
@onfail_false
def two_equal(a: int, b: int, c: int) -> bool:
    return a == b or b == c or a == c


@predicate(alias=['all-diff?', 'all-different?'])
@onfail_false
def all_different(a: int, b: int, c: int) -> bool:
    return a != b and b != c and a != c


# Test the groups -------------------------------
# by is the right type for that partition? ------

@predicate(alias=['is-not-triangle?'])
@onfail_false
def is_not_triangle(value):
    return value == Triangle.not_triangle


@predicate(alias=['is-equilateral?'])
@onfail_false
def is_equilateral(value):
    return value == Triangle.equilateral


@predicate(alias=['is-scalene?'])
@onfail_false
def is_scalene(value):
    return value == Triangle.scalene


@predicate(alias=['is-isosceles?'])
@onfail_false
def is_isosceles(value):
    return value == Triangle.isosceles


# Domain --------------------------------------------------

@domain(alias=['TriangleValues'])
def critical_values() -> Tuple[int, ...]:
    return (-1, 0, 1, 2, 3, 4, 5)


print(not_triangle(-1, -1, -1))
