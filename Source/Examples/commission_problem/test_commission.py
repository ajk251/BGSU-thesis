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
# on 2022 Jul 02 Sat 20:39:58

sales = sales_values()
linear_sales = linear_sales()

# too_low = lambda l,s,b: l <= 1 or s <= 1 or b <= 1
# too_high = lambda l,s,b: l >= lock_max or s >= stock_max or b >= barrel_max

def test_commission_I5():

    cases = defaultdict(list)
    results = defaultdict(list)

    for locks, stocks, barrels in linear_sales:

        try:
            result = commission(locks, stocks, barrels)
        except Exception as e:
            result = e

        if valid_sales(locks, stocks, barrels):
            assert is_error(result)
            cases['invalid'].append((locks, stocks, barrels))
            results['invalid'].append(result)
        elif low_sales(locks, stocks, barrels):
            assert low_commission(result)
            cases['low'].append((locks, stocks, barrels))
            results['low'].append(result)
        elif medium_sales(locks, stocks, barrels):
            assert medium_commission(result)
            cases['medium'].append((locks, stocks, barrels))
            results['medium'].append(result)
        elif high_sales(locks, stocks, barrels):
            assert high_commission(result)
            cases['high'].append((locks, stocks, barrels))
            results['high'].append(result)
        else:
            raise FalconError('Failed to meet at least one group')


    plot_commission(cases, results)


def test_commission_GSgH():

    cases = defaultdict(list)
    results = defaultdict(list)

    for locks, stocks, barrels in sales:

        try:
            result = commission(locks, stocks, barrels)
        except Exception as e:
            result = e

        if too_low(locks, stocks, barrels) or too_high(locks, stocks, barrels):
            print(f'WRONG      {locks},{stocks},{barrels} -> {result}')
            assert is_error(result)
            cases['invalid'].append((locks, stocks, barrels))
            results['invalid'].append(result)
        elif low_sales(locks, stocks, barrels):
            print(f'LOW {locks},{stocks},{barrels} -> {result}')
            cases['low'].append((locks, stocks, barrels))
            results['low'].append(result)
        elif medium_sales(locks, stocks, barrels):
            print(f'MEDIUM {locks},{stocks},{barrels} -> {result}')
            assert medium_commission(result)
            cases['medium'].append((locks, stocks, barrels))
            results['medium'].append(result)
        elif high_sales(locks, stocks, barrels):
            print(f'HIGH {locks},{stocks},{barrels} -> {result}')
            assert high_commission(result)
            cases['high'].append((locks, stocks, barrels))
            results['high'].append(result)
        else:
            raise FalconError('Failed to meet at least one group')

    assert low_commission_group(results['low'], 5)

    plot_commission(cases, results)


# test_commission_I5()
test_commission_GSgH()