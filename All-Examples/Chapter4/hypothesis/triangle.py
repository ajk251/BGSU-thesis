
from collections import defaultdict
from enum import Enum
from itertools import chain, product
from typing import Type

Triangle = Enum('Triangle', 'equilateral, isosceles, scalene, not_triangle')
# Triangle = Type('Triangle', 'equilateral, isosceles, scalene, not_triangle')

class TriangleError(Exception): pass

def classify(a: int, b: int, c: int) -> Triangle:

    assert isinstance(a, int) and isinstance(b, int) and isinstance(c, int), "All values must be integers"

    if not ((a <= b+c) and (b <= a+c) and (c <= a+b)):
        return Triangle.not_triangle
    elif not ((a > 0) and (b > 0) and (c > 0)):
        # print('not a valid triangle ', end='')
        return Triangle.not_triangle
    elif a == b == c:
        return Triangle.equilateral
    elif a != b and b != c and c != a:
        return Triangle.scalene
    elif a == b or b == c or a == c:
        return Triangle.isosceles

    raise TriangleError(f'Could not classify input a ￫ {a}, b ￫ {b}, c ￫ {c}')

# ---------------------------------------------------------

def positive_integers(a: int, b: int, c: int) -> bool:
    """Tests that all values are positive integers"""
    if not (isinstance(a, int) and a > 0):
        return False

    if not (isinstance(b, int) and b > 0):
        return False

    if not (isinstance(c, int) and c > 0):
        return False

    return True


def satisfy_triangle_theorem(a: int, b: int, c: int) -> bool:
    """The Triangle Theorem, ie. sᵢ < s₂+s₃, for all sides"""
    return (a <= b+c) and (b <= a+c) and (c <= a+b)


def is_equilateral(a: int, b: int, c: int) -> bool:
    """Triangle where all sides are equal"""
    return a == b and b == c


def is_isosceles(a: int, b: int, c: int) -> bool:
    """Triangle where two sides are equal"""
    return a == b or b == c or a == c


def is_scalene(a: int, b: int, c: int) -> bool:
    """Triangle where 3 sides are different"""
    return a != b and b != c and a != c
 