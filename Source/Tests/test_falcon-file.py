from Falcon.algorithms import *
from Falcon.domains import *
from Falcon.macros import *
from Falcon.predicates import *
from Falcon.utilities.utls import call
from Falcon.utilities.TestLogWriter import write_to_log
from Falcon.utilities import FalconError

from collections import defaultdict
import unittest

import pytest

# This file was generated automatically by falcon.
# from: Tests/winnow_tests3.fcn
# on 2022 Jun 18 Sat 19:20:24

X = integers(0, 100)
Y = integers(0, 100)

def test_winnow_fn():

    groups = defaultdict(list)

    for xᵢ, yᵢ in zip(X, Y):

        try:
            result = fn(xᵢ, yᵢ)
        except Exception as e:
            result = e

        if is_integer(result):
            groups['a'].append((result, (xᵢ, yᵢ)))
        if between(result, 0, 1):
            groups['b'].append((result, (xᵢ, yᵢ)))
        if is_float(result):
            groups['c'].append((result, (xᵢ, yᵢ)))
        if result > 2:
            groups['d'].append((result, (xᵢ, yᵢ)))

        assert cardnality_gt(groups['a'], 1)
        assert cardnality_plus_minus_n(groups['b'], 100, 10)
        assert cardnality_lt(groups['c'], 3)
        assert cardnality_gt(groups['d'], 1)

        assert count <= 1, f"The minimum number of predicates has not been met - met: {count}, min: 1"

        follow_up_func(groups)
