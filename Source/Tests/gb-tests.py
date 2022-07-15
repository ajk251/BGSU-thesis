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
# from: Tests/groupby-tests.fcn
# on 2022 Jul 15 Fri 14:49:06

X = integers()

def test_addg_HY():

    results = defaultdict(list)
    n_cases = defaultdict(int)

    for xᵢ in X:

        try:
            result = addg(xᵢ)
        except Exception as e:
            result = e

        if is_float(xᵢ):
            assert is_float(result, float), "Group 'a' predicate 'is_float' has failed"
            results['a'].append(result)
            n_cases['a'] += 1
        elif is_integer(xᵢ):
            assert is_integer(result, int), "Group 'b' predicate 'is_integer' has failed"
            results['b'].append(result)
            n_cases['b'] += 1
        elif is_positive(xᵢ):
            assert is_positive(result), "Tests whether the values is a number greater than 0"
            results['c'].append(result)
            n_cases['c'] += 1
        elif gt(xᵢ):
            assert gt(result, 1), "Group 'd' predicate 'gt' has failed"
            results['d'].append(result)
            n_cases['d'] += 1
        else:
            raise FalconError('Failed to meet at least one group')

    for group, n in n_cases.items():
        assert n >= 1, f"'{group}' not meet the min number of examples"

    plot_results(results)


def test_addf_YCkc():

    results = defaultdict(list)
    n_cases = defaultdict(int)

    for xvaluesᵢ in Xvalues:

        try:
            result = addf(xvaluesᵢ)
        except Exception as e:
            result = e

        if is_float(xvaluesᵢ) or is_integer(xvaluesᵢ):
            assert is_float(result)
            results['a'].append(result)
            n_cases['a'] += 1
        elif is_integer(xvaluesᵢ):
            assert is_integer(result)
            results['b'].append(result)
            n_cases['b'] += 1
        elif is_positive(xvaluesᵢ):
            assert is_positive(result)
            results['c'].append(result)
            n_cases['c'] += 1
        elif between(xvaluesᵢ):
            assert between(result, 0, 1)
            results['d'].append(result)
            n_cases['d'] += 1
        elif ge(xvaluesᵢ):
            assert ge(result, 1)
            results['e'].append(result)
            n_cases['e'] += 1
        elif raises_error(xvaluesᵢ):
            assert raises_error(result, InvalidInputError)
            results['error'].append(result)
            n_cases['error'] += 1
        else:
            raise FalconError('Failed to meet at least one group')

    for group, n in n_cases.items():
        assert n >= 1, f"'{group}' not meet the min number of examples"
