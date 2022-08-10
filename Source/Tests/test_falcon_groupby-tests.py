from Falcon.algorithms import *
from Falcon.domains import *
from Falcon.macros import *
from Falcon.predicates import *
from Falcon.utilities.utls import call
from Falcon.utilities.TestLogWriter import write_to_log
from Falcon.utilities import FalconError

from collections import defaultdict

import pytest


# This file was generated automatically by Falcon.
# from: groupby-tests.fcn
# on 2022 Aug 10 Wed 19:30:40

X = integers()

def test_groupby_addg_Uffte():

    results = defaultdict(list)
    n_cases = defaultdict(int)

    for xᵢ in X:

        try:
            result = addg(xᵢ)
        except Exception as e:
            result = e

        if between(xᵢ, 0, 1) or is_outside(xᵢ, -1, 1):
            assert is_a(result, float), "The value is not any of instances specified"
            results['a'].append(result)
            n_cases['a'] += 1
        elif is_int(xᵢ):
            results['b'].append(result)
            n_cases['b'] += 1
        elif is_positive(xᵢ):
            assert is_odd(result), "Tests if a given number is odd"
            results['c'].append(result)
            n_cases['c'] += 1
        elif gt(xᵢ, 1):
            assert is_inf(result), "Group 'd' predicate 'is_inf' has failed"
            results['d'].append(result)
            n_cases['d'] += 1
        else:
            raise FalconError('Failed to meet at least one group')

    assert is_any(results['b'], int)

    for group, n in n_cases.items():
        assert n >= 1, f"'{group}' not meet the min number of examples"

    plot_results(results)
