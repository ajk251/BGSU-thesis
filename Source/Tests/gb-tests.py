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
# on 2022 Jul 10 Sun 20:18:08

X = integers()

def test_addg_XBeDc():

    results = defaultdict(list)

    for xᵢ in X:

        try:
            result = addg(xᵢ)
        except Exception as e:
            result = e

        if is_float(xᵢ):
            assert is_float(result, float), "Group 'a' predicate 'is_float' has failed"
            results['a'].append(result)
        elif is_integer(xᵢ):
            assert is_integer(result, int), "Group 'b' predicate 'is_integer' has failed"
            results['b'].append(result)
        elif is_positive(xᵢ):
            assert is_positive(result), "Tests whether the values is a number greater than 0"
            results['c'].append(result)
        elif gt(xᵢ):
            assert gt(result, 1), "Group 'd' predicate 'gt' has failed"
            results['d'].append(result)
        else:
            raise FalconError('Failed to meet at least one group')


    plot_results(results)


def test_addf_zmBH():

    results = defaultdict(list)

    for xvaluesᵢ in Xvalues:

        try:
            result = addf(xvaluesᵢ)
        except Exception as e:
            result = e

        if is_float(xvaluesᵢ) or is_integer(xvaluesᵢ):
            assert is_float(result), "Group 'a' predicate 'is_float' has failed"
            results['a'].append(result)
        elif is_integer(xvaluesᵢ):
            assert is_integer(result), "Group 'b' predicate 'is_integer' has failed"
            results['b'].append(result)
        elif is_positive(xvaluesᵢ):
            assert is_positive(result), "Tests whether the values is a number greater than 0"
            results['c'].append(result)
        elif between(xvaluesᵢ):
            assert between(result, 0, 1), "Group 'd' predicate 'between' has failed"
            results['d'].append(result)
        elif ge(xvaluesᵢ):
            assert ge(result, 1), "Group 'e' predicate 'ge' has failed"
            results['e'].append(result)
        elif raises_error(xvaluesᵢ):
            assert raises_error(result, InvalidInputError), "Tests that the error is an instance of the specified type"
            results['error'].append(result)
        else:
            raise FalconError('Failed to meet at least one group')

