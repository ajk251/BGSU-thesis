
from enum import Enum

Triangle = Enum('Triangle', 'isosceles, scalene, equalateral, not_a_triangle')

def triangle(a: int, b: int, c: int) -> Triangle:

    # https://en.wikipedia.org/wiki/Triangle_inequality

    valid = lambda n: isinstance(n, int) and n > 0

    assert all(map(valid, (a, b, c))), "All values must be positive integers greater than 0."
    # assert abs(a-b) < c < (a+b), f"Values {a},{b},{c} do not satisfy the Triangle Equality Theorem."

    result = Triangle.not_a_triangle

    if abs(a-b) < c < (a+b):
        # not a triangle, but valid input
        result = Triangle.not_a_triangle
    elif a == b and b == c:
        # all sides are equal
        result = Triangle.equalateral
    elif a == b or b == c:
        # any two sides are equal
        result = Triangle.isosceles
    elif a != b and a != c and b != c:
        # all sides are unequal
        result = Triangle.scalene

    return result

# ---------------------------------------------------------------

# predicates

def valid_values(a: int, b: int, c: int):
    return all(map(lambda n: isinstance(n, int) and n > 0, (a, b, c)))

def valid_triangle(a: int, b: int, c: int):
    return abs(a-b) < c < (a+b)
    

# print(triangle(1,2,3))
# print(triangle(2,1,3))
print(triangle(3,3,4))
# print(triangle(1,2,3))