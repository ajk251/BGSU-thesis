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
# from: Tests/groupby-tests.fcn
# on 2022 Jun 30 Thu 11:44:03

X = integers()

def test_addg_lYS():

    for xᵢ in X:

        try:
            result = addg(xᵢ)
        except Exception as e:
            result = e

        if is_float(xᵢ):
            assert is_float(result, float)
        elif is_integer(xᵢ):
            assert is_integer(result, int)
        elif is_positive(xᵢ):
            assert is_positive(result)
        elif gt(xᵢ):
            assert gt(result)
        else:
            raise FalconError('Failed to meet at least one group')



def test_addf_JJQ():

    for xvaluesᵢ in Xvalues:

        try:
            result = addf(xvaluesᵢ)
        except Exception as e:
            result = e

        if is_float(xvaluesᵢ) or is_integer(xvaluesᵢ):
            assert is_float(result)
        elif is_integer(xvaluesᵢ):
            assert is_integer(result)
        elif is_positive(xvaluesᵢ):
            assert is_positive(result)
        elif between(xvaluesᵢ):
            assert between(result)
        elif ge(xvaluesᵢ):
            assert ge(result)
        elif raises_error(xvaluesᵢ):
            assert raises_error(result)
        else:
            raise FalconError('Failed to meet at least one group')

