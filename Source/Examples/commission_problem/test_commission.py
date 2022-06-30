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
# on 2022 Jun 30 Thu 17:56:37

sales = sales_values()

def test_commission_Kap():

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


def test_commission_KKa():

    cases = defaultdict(list)
    results = defaultdict(list)

    for locks, stocks, barrels in sales:

        try:
            result = commission(locks, stocks, barrels)
        except Exception as e:
            result = e

        if too-low?(locks, stocks, barrels) or too-high?(locks, stocks, barrels):
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
