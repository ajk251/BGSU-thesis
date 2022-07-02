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

# This file was generated automatically by falcon.
# from: commission.fcn
# on 2022 Jul 02 Sat 18:23:28

sales = linear_sales()

too_low = lambda l,s,b: l <= 0 and s <= 0 and b <= 0
too_high = lambda l,s,b: l > 100 and s > 100 and b > 100

def test_commission_4a():

    cases = defaultdict(list)
    results = defaultdict(list)

    for locks, stocks, barrels in sales:

        try:
            result = commission(locks, stocks, barrels)
        except Exception as e:
            result = e

        if valid_sales(locks, stocks, barrels):
            assert is_error(result)
            cases['invalid'].append((locks, stocks, barrels))
            results['invalid'].append(result)
        elif low_sales(locks, stocks, barrels):
            cases['low'].append((locks, stocks, barrels))
            results['low'].append(result)
        elif medium_sales(locks, stocks, barrels):
            cases['medium'].append((locks, stocks, barrels))
            results['medium'].append(result)
        elif high_sales(locks, stocks, barrels):
            cases['high'].append((locks, stocks, barrels))
            results['high'].append(result)
        else:
            raise FalconError('Failed to meet at least one group')

    assert low_commission(results['low'])
    assert medium_commission(results['medium'])
    assert high_commission(results['high'])

    plot_commission(cases, results)


def test_commission_QYP():

    cases = defaultdict(list)
    results = defaultdict(list)

    for locks, stocks, barrels in sales:

        try:
            result = commission(locks, stocks, barrels)
        except Exception as e:
            result = e

        if too_low(locks, stocks, barrels) or too_high(locks, stocks, barrels):
            assert is_error(result)
            cases['invalid'].append((locks, stocks, barrels))
            results['invalid'].append(result)
        elif low_sales(locks, stocks, barrels):
            assert low-commission+examples?(result)
            cases['low'].append((locks, stocks, barrels))
            results['low'].append(result)
        elif medium_sales(locks, stocks, barrels):
            cases['medium'].append((locks, stocks, barrels))
            results['medium'].append(result)
        elif high_sales(locks, stocks, barrels):
            cases['high'].append((locks, stocks, barrels))
            results['high'].append(result)
        else:
            raise FalconError('Failed to meet at least one group')

    assert medium_commission(results['medium'])
    assert high_commission(results['high'])

    plot_commission(cases, results)
