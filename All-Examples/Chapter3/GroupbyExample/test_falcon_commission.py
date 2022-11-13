from Falcon.algorithms import *
from Falcon.domains import *
from Falcon.macros import *
from Falcon.predicates import *
from Falcon.utilities.utls import call
from Falcon.utilities.TestLogWriter import write_to_log
from Falcon.utilities import FalconError

from collections import defaultdict

import pytest

from commission import *

# This file was generated automatically by Falcon.
# from: commission.fcn
# on 2022 Nov 13 Sun 14:09:03

sales = sales_values()

def test_groupby_commission_33F():

    cases = defaultdict(list)
    results = defaultdict(list)
    n_cases = defaultdict(int)

    for locks, stocks, barrels in sales:

        try:
            result = commission(locks, stocks, barrels)
        except Exception as e:
            result = e

        if too_low(locks, stocks, barrels) or too_high(locks, stocks, barrels):
            assert raises_error(result), "Tests that the error is an Exception"
            cases['invalid'].append((locks, stocks, barrels))
            results['invalid'].append(result)
            n_cases['invalid'] += 1
        elif low_sales(locks, stocks, barrels):
            assert low_commission(result), "Group 'low' predicate 'low_commission' has failed"
            cases['low'].append((locks, stocks, barrels))
            results['low'].append(result)
            n_cases['low'] += 1
        elif medium_sales(locks, stocks, barrels):
            assert medium_commission(result), "Group 'medium' predicate 'medium_commission' has failed"
            cases['medium'].append((locks, stocks, barrels))
            results['medium'].append(result)
            n_cases['medium'] += 1
        elif high_sales(locks, stocks, barrels):
            assert high_commission(result), "Group 'high' predicate 'high_commission' has failed"
            cases['high'].append((locks, stocks, barrels))
            results['high'].append(result)
            n_cases['high'] += 1
        else:
            raise FalconError('Failed to meet at least one group')


    for group, n in n_cases.items():
        assert n >= 1, f"'{group}' not meet the min number of examples"

    plot_commission(cases, results)
