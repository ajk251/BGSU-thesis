
from Triangle_problem import *

from Falcon.domains import domain
from Falcon.predicates.predicates import predicate, on_fail_false


@predicate(alias=['no-triangle-theorem?', 'not-satisfy-triangle-theorem?'])
@on_fail_false
def not_satisfy_triangle_theorem(a: int, b: int, c: int) -> bool:
    """The Triangle Theorem, ie. sᵢ < s₂+s₃, for all sides"""
    return not ((a < b+c) and (b < a+c) and (c < a+b))


@predicate(alias=['not-triangle?'])
@on_fail_false
def not_triangle(a: int, b: int, c: int) -> bool:
    """Tests that three inputs do not form a valid triangle"""
    result =  any(map(lambda n: (not isinstance(n, int)) or (not n > 0), (a, b, c)))
    result &= not ((a < b+c) and (b < a+c) and (c < a+b))

    return result


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

@predicate(alias=['is-not-triangle?'])
@on_fail_false
def is_not_triangle(value):
    return value == Triangle.not_triangle


@predicate(alias=['is-equilateral?'])
@on_fail_false
def is_equilateral(value):
    return value == Triangle.equilateral


@predicate(alias=['is-scalene?'])
@on_fail_false
def is_scalene(value):
    return value == Triangle.scalene


@predicate(alias=['is-isosceles?'])
@on_fail_false
def is_isosceles(value):
    return value == Triangle.isosceles


# Domain --------------------------------------------------

@domain(alias=['TriangleValues'])
def critical_values() -> Tuple[int, ...]:
    return (-1, 0, 1, 2, 3, 4, 5)
