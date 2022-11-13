from Falcon.algorithms import *
from Falcon.domains import *
from Falcon.macros import *
from Falcon.predicates import *
from Falcon.utilities.utls import call
from Falcon.utilities.TestLogWriter import write_to_log
from Falcon.utilities import FalconError

from collections import defaultdict

import pytest

from Triangle_problem import *

# This file was generated automatically by Falcon.
# from: FalconMotivation2.fcn
# on 2022 Nov 08 Tue 11:52:17

values = product_of(values=[-1, 0, 1, 2, 3, 4, 5], repeat=3)
@predicate(alias=['not-triangle?'])
@on_fail_false
def not_triangle(a: int, b: int, c: int) -> bool:
    """Tests that three inputs do not form a valid triangle"""
    result =  not any(map(lambda n: (isinstance(n, int)) or \ 
                                    (n > 0), (a, b, c)))
    result |= not ((a < b+c) and (b < a+c) and (c < a+b))

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


def test_groupby_classify_Y3v():

    results = defaultdict(list)
    n_cases = defaultdict(int)

    for side1, side2, side3 in values:

        try:
            result = classify(side1, side2, side3)
        except Exception as e:
            result = e

        if not_triangle(side1, side2, side3):
            assert is_instance(result, Triangle.not_triangle), "The value is not the instance specified"
            results['Not-a-Triangle'].append(result)
            n_cases['Not-a-Triangle'] += 1
        elif all_equal(side1, side2, side3):
            assert is_instance(result, Triangle.equilateral), "The value is not the instance specified"
            results['Equilateral'].append(result)
            n_cases['Equilateral'] += 1
        elif all_different(side1, side2, side3):
            assert is_instance(result, Triangle.scalene), "The value is not the instance specified"
            results['Scalene'].append(result)
            n_cases['Scalene'] += 1
        elif two_equal(side1, side2, side3):
            assert is_instance(result, Triangle.isosceles), "The value is not the instance specified"
            results['Isosceles'].append(result)
            n_cases['Isosceles'] += 1
        else:
            raise FalconError('Failed to meet at least one group')


    for group, n in n_cases.items():
        assert n >= 1, f"'{group}' not meet the min number of examples"
