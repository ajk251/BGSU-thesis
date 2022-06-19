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
from test_functions import add, add2, sub
from test_functions import *

# This file was generated automatically by falcon.
# from: Tests/satisfy-tests.fcn
# on 2022 Jun 19 Sun 07:41:17

X = integers(-10, 10, n=100)
Y = integers(-10, 10, n=100)

def test_add_CIChG():

    for xᵢ, yᵢ in zip(X, Y):

        try:
            result = add(xᵢ, yᵢ)
        except Exception as error:
            result = error

        count = 0

        if is_integer(result):
            count += 1
        if is_float(result):
            count += 1
        if result < 4:
            count += 1
        if is_none(result):
            count += 1
        if is_error_and_contains(result, ZeroDivisionError, "0"):
            count += 1

        assert count >= 1, f"The minimum number of predicates has not been met - met: {count}, min: 1  [with {result}]"
        assert count > 4, f"Exceed number of predicates met - met: {count}, max: 4"
