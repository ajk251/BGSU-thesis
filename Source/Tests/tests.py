from algorithms.algorithms import *
from domains import *
from macros import *
from predicates import *
from utilities.utls import call
from utilities.TestLogWriter import write_to_log
from utilities import FalconError

from collections import defaultdict
import unittest

import pytest

# This file was generated automatically by falcon.
# from: Tests/groupby-tests.fcn
# on 2022 Jun 03 Fri 01:01:29

X = integers()

def test_groupby_addg():

    groups = defaultdict(list)
    results = defaultdict(list)

    for xᵢ in X:

        try:
            result = addg(xᵢ)
        except Exception as e:
            result = e

        if is_float(xᵢ):
            assert is_a(result)
            groups['a'].append((xᵢ,))
            results['a'].append(result)
        elif is_integer(xᵢ):
            groups['b'].append((xᵢ,))
            results['b'].append(result)
        elif is_positive(xᵢ):
            assert is_odd(result)
            groups['c'].append((xᵢ,))
            results['c'].append(result)
        elif >(xᵢ):
            assert is_inf(result)
            groups['d'].append((xᵢ,))
            results['d'].append(result)
        else:
            FalconError('Failed to meet at least one group')

        assert is_any(results['b'], int)

    plot_results(groups, results)


def test_groupby_addf():

    groups = defaultdict(list)
    results = defaultdict(list)

    for xvaluesᵢ in Xvalues:

        try:
            result = addf(xvaluesᵢ)
        except Exception as e:
            result = e

        if is_float(xvaluesᵢ) or is_integer(xvaluesᵢ):
            groups['a'].append((xvaluesᵢ,))
            results['a'].append(result)
        elif is_integer(xvaluesᵢ):
            groups['b'].append((xvaluesᵢ,))
            results['b'].append(result)
        elif is_positive(xvaluesᵢ):
            groups['c'].append((xvaluesᵢ,))
            results['c'].append(result)
        elif between(result, 0, 1):
            groups['d'].append((xvaluesᵢ,))
            results['d'].append(result)
        elif xvaluesᵢ >= 1:
            groups['e'].append((xvaluesᵢ,))
            results['e'].append(result)
        elif catch_error(result, InvalidInputError):
            groups['error'].append((xvaluesᵢ,))
            results['error'].append(result)
        else:
            FalconError('Failed to meet at least one group')

