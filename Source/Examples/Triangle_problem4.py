
from enum import Enum


# this is for TSTL =======================+++++++++++++++++

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


# TSTL tests -----------------------------------

def test_classify(side_a: int, side_b: int, side_c: int):

    is_triangle = lambda a,b,c: (a < b+c) and (b < a+c) and (c < a+b)
    integers    = lambda a,b,c: isinstance(a, int) and isinstance(b, int) and isinstance(c, int)
    is_valid    = lambda a,b,c: (a > 0) and (b > 0) and (c > 0)

    sides = frozenset((side_a, side_b, side_c))             # a set only holds unquie items

    all_equal = lambda sides_: len(sides_) == 1
    two_equal = lambda sides_: len(sides_) == 2
    all_diff  = lambda sides_: len(sides_) == 3

    kind = classify(side_a, side_b, side_c)

    if (not is_triangle(side_a, side_b, side_c)) or (not is_valid(side_a, side_b, side_c)) or (not integers(side_a, side_b, side_c)):
        return kind == Triangle.not_triangle
    elif all_equal(sides):
        return kind == Triangle.equilateral
    elif all_diff(sides):
        return kind == Triangle.scalene
    elif two_equal(sides):
        return kind == Triangle.isosceles

    return False