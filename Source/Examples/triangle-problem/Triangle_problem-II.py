
from Falcon.predicates import predicate, on_fail_false

@predicate(alias=['not-triangle?'])
@on_fail_false
def not_triangle(a: int, b: int, c: int) -> bool:
    """Tests that three inputs do not form a valid triangle"""

    result =  any(map(lambda n: (not isinstance(n, int)) or (not n > 0), (a, b, c)))
    result &= not ((a < b+c) and (b < a+c) and (c < a+b))
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