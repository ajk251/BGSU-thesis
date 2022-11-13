
from triangle import classify, Triangle, TriangleError
from triangle import is_equilateral, is_isosceles, is_scalene, satisfy_triangle_theorem

from hypothesis import given, HealthCheck, strategies as st

# -----------------------------------------------

# HealthCheck.filter_too_much = False


@given(st.integers().filter(lambda n: satisfy_triangle_theorem(n, n, n) and is_equilateral(n, n, n)))
def test_equilateral(n):
    assert classify(n, n, n) == Triangle.equilateral


@given(st.tuples(st.integers(), st.integers(), st.integers()).filter(lambda sides: not satisfy_triangle_theorem(*sides)))
def test_not_a_triangle(sides):
    assert classify(*sides) == Triangle.not_triangle


# @given(st.tuples(st.integers(), st.integers()).filter(lambda sides: satisfy_triangle_theorem(sides[0], sides[1], sides[1]) and is_isosceles(sides[0], sides[1], sides[1])))
@given(st.tuples(st.integers(), st.integers()).filter(lambda sides: satisfy_triangle_theorem(sides[0], sides[1], sides[1]) and is_isosceles(sides[0], sides[1], sides[1])))
def test_isosceles(sides):
    a, b = sides
    assert classify(a, b, b) == Triangle.isosceles


@given(st.tuples(st.integers(), st.integers(), st.integers()).filter(lambda sides: satisfy_triangle_theorem(*sides) and is_scalene(*sides)))
def test_scalene(sides):
    assert classify(*sides) == Triangle.scalene
