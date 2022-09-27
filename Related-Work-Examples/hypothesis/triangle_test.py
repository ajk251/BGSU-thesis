
import triangle
from triangle import classify, Triangle, TriangleError
from triangle import positive_integers, satisfy_triangle_theorem, is_equilateral, is_scalene, is_isosceles

from hypothesis import given
from hypothesis import example, given, strategies as st


# test branches ---------------------------------

@given(st.integers(), st.integers(), st.integers())
def test_triangle(a: int, b: int, c: int):

    result = triangle.classify(a, b, c)

    if result == Triangle.not_triangle:
        assert (not positive_integers(a, b, c)) or (not satisfy_triangle_theorem(a, b, c))
    elif result == Triangle.equilateral:
        assert is_equilateral(a, b, c)
    elif result == Triangle.scalene:
        assert is_scalene(a, b, c)
    else:
        assert is_isosceles(a, b, c)

