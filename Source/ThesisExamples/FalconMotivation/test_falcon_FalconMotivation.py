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
# from: FalconMotivation.fcn
# on 2022 Jul 28 Thu 17:23:06

values = permutations_of(values=[-1, 0, 1, 2, 3, 4, 5], repeat=3)

def test_groupby_classify_ttHa():

    results = defaultdict(list)
    n_cases = defaultdict(int)

    for side1, side2, side3 in values:

        try:
            result = classify(side1, side2, side3)
        except Exception as e:
            result = e

        if not_triangle(side1, side2, side3):
            assert eq(result, Triangle.not_triangle)
            results['Not-a-Triangle'].append(result)
            n_cases['Not-a-Triangle'] += 1
        elif all_equal(side1, side2, side3):
            assert eq(result, Triangle.equilateral)
            results['Equilateral'].append(result)
            n_cases['Equilateral'] += 1
        elif all_different(side1, side2, side3):
            assert eq(result, Triangle.scalene)
            results['Scalene'].append(result)
            n_cases['Scalene'] += 1
        elif two_equal(side1, side2, side3):
            assert eq(result, Triangle.isosceles)
            results['Isosceles'].append(result)
            n_cases['Isosceles'] += 1
        else:
            raise FalconError('Failed to meet at least one group')

    for group, n in n_cases.items():
        assert n >= 1, f"'{group}' not meet the min number of examples"
